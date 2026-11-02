"""
Forza Horizon 2 Save Editor Tool (for Azimuth Xbox One Emulator)
Author: Antigravity Agent
"""

import os
import sys
import shutil
import hashlib
import struct
import re
import sqlite3

BASE_USER_DIR = 'User_9000000000000'
REVISIONS_DIR = os.path.join(BASE_USER_DIR, 'revisions')
BACKUP_DIR = 'backup_original_save'

def get_latest_revision():
    if not os.path.exists(REVISIONS_DIR):
        print(f"Error: {REVISIONS_DIR} not found.")
        return None
    revs = [d for d in os.listdir(REVISIONS_DIR) if os.path.isdir(os.path.join(REVISIONS_DIR, d))]
    revs.sort()
    return revs[-1] if revs else None

def inspect_save():
    latest_rev = get_latest_revision()
    if not latest_rev:
        return
    data_path = os.path.join(REVISIONS_DIR, latest_rev, 'data')
    print("=" * 65)
    print(f"   FORZA HORIZON 2 SAVE STATUS (Revision: {latest_rev})")
    print("=" * 65)
    
    # 1. Credits & XP
    profile_path = os.path.join(data_path, 'ProfileData')
    if os.path.exists(profile_path):
        with open(profile_path, 'rb') as f:
            p_data = f.read()
        tag = b'Credits \x00\x00\x00\x00\x03\x00\x00\x00'
        idx = p_data.find(tag)
        if idx != -1:
            cr = struct.unpack('<I', p_data[idx+len(tag):idx+len(tag)+4])[0]
            print(f"  Credits (CR)          : {cr:,} CR")
            
        xp_tag = b'XP \x00\x00\x00\x00\x03\x00\x00\x00'
        xp_idx = p_data.find(xp_tag)
        if xp_idx != -1:
            xp = struct.unpack('<I', p_data[xp_idx+len(xp_tag):xp_idx+len(xp_tag)+4])[0]
            print(f"  Player XP             : {xp:,} XP")

    # 2. Wheelspins & Features from SaveState
    savestate_path = os.path.join(data_path, 'SaveState')
    if os.path.exists(savestate_path):
        with open(savestate_path, 'rb') as f:
            s_data = f.read()
        m_spin = re.search(rb'<Property Name="Spins" Value="(\d+)"/>', s_data)
        if m_spin:
            print(f"  Wheelspins            : {int(m_spin.group(1))} Spins")
        
        m_autoshow = re.search(rb'Name="IntroducedAutoshow" Value="([^"]+)"', s_data)
        if m_autoshow:
            status = "UNLOCKED" if m_autoshow.group(1) == b"true" else "LOCKED"
            print(f"  Buy Cars (Autoshow)   : {status}")

    # 3. Database Stats (Championships, Destinations, Perks)
    db_path = os.path.join(data_path, 'PlayerDatabase')
    if os.path.exists(db_path):
        with open(db_path, 'rb') as f:
            raw_db = f.read()
        try:
            con = sqlite3.connect(':memory:')
            con.deserialize(raw_db[8:])
            cur = con.cursor()
            cur.execute("SELECT count(*) FROM Career_ChampionshipsWon;")
            champs = cur.fetchone()[0]
            cur.execute("SELECT count(*) FROM Career_DestinationUnlock;")
            dests = cur.fetchone()[0]
            cur.execute("SELECT count(*) FROM PerkUnlock;")
            perks = cur.fetchone()[0]
            print(f"  Championships Won     : {champs} / 168")
            print(f"  Festival Hubs Unlocked: {dests} / 6")
            print(f"  Perks Unlocked        : {perks} / 25")
            con.close()
        except Exception as e:
            print(f"  Database read error   : {e}")

    print("=" * 65)

def modify_save(credits=None, spins=None):
    latest_rev = get_latest_revision()
    if not latest_rev:
        return
    rev_path = os.path.join(REVISIONS_DIR, latest_rev)
    data_path = os.path.join(rev_path, 'data')
    commit_path = os.path.join(rev_path, 'commit')

    # Backup if not yet backed up
    if not os.path.exists(BACKUP_DIR):
        print(f"[*] Creating backup to {BACKUP_DIR}...")
        shutil.copytree(BASE_USER_DIR, os.path.join(BACKUP_DIR, BASE_USER_DIR))
        print("[+] Backup created.")

    # Edit Credits
    if credits is not None:
        profile_path = os.path.join(data_path, 'ProfileData')
        with open(profile_path, 'rb') as f:
            data = bytearray(f.read())
        tag = b'Credits \x00\x00\x00\x00\x03\x00\x00\x00'
        idx = data.find(tag)
        if idx != -1:
            val_idx = idx + len(tag)
            old_cr = struct.unpack('<I', data[val_idx:val_idx+4])[0]
            data[val_idx:val_idx+4] = struct.pack('<I', int(credits))
            with open(profile_path, 'wb') as f:
                f.write(data)
            print(f"[+] Credits updated: {old_cr:,} -> {int(credits):,} CR")

    # Edit Wheelspins
    if spins is not None:
        savestate_path = os.path.join(data_path, 'SaveState')
        with open(savestate_path, 'rb') as f:
            s_data = f.read()
        spins_pattern = re.compile(rb'<Property Name="Spins" Value="(\d+)"/>')
        m = spins_pattern.search(s_data)
        if m:
            old_spins = int(m.group(1))
            new_tag = f'<Property Name="Spins" Value="{int(spins)}"/>'.encode('utf-8')
            s_data = spins_pattern.sub(new_tag, s_data, count=1)
            with open(savestate_path, 'wb') as f:
                f.write(s_data)
            print(f"[+] Wheelspins updated: {old_spins} -> {int(spins)} Spins")

    # Rebuild commit
    file_names = sorted(os.listdir(data_path))
    lines = ["Azimuth complete save revision v2", f"blobs {len(file_names)}"]
    for fname in file_names:
        p = os.path.join(data_path, fname)
        with open(p, 'rb') as f:
            content = f.read()
        h = hashlib.sha256(content).hexdigest()
        lines.append(f"{h} {len(content)} {fname}")
    lines.append("")
    with open(commit_path, 'wb') as f:
        f.write("\n".join(lines).encode('utf-8'))
    print(f"[+] Commit manifest updated with new SHA-256 hashes.")

def restore_backup():
    src = os.path.join(BACKUP_DIR, BASE_USER_DIR)
    if not os.path.exists(src):
        print(f"[-] No backup found at {src}")
        return
    print(f"[*] Restoring from {src}...")
    shutil.rmtree(BASE_USER_DIR)
    shutil.copytree(src, BASE_USER_DIR)
    print("[+] Successfully restored original save data.")

if __name__ == '__main__':
    if len(sys.argv) > 1:
        cmd = sys.argv[1].lower()
        if cmd == 'status':
            inspect_save()
        elif cmd == 'restore':
            restore_backup()
        elif cmd == 'set':
            cr = int(sys.argv[2]) if len(sys.argv) > 2 else None
            sp = int(sys.argv[3]) if len(sys.argv) > 3 else None
            modify_save(cr, sp)
        else:
            print("Usage: python fh2_save_tool.py [status | set <credits> <spins> | restore]")
    else:
        inspect_save()
