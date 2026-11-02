# FH2-SaveGame-XboxOne

<p align="center">
  <img src="https://img.shields.io/badge/Forza%20Horizon%202-Xbox%20One-red.svg?style=for-the-badge" alt="Forza Horizon 2"/>
  <a href="https://azimuthforza.com/"><img src="https://img.shields.io/badge/Emulator-Azimuth-blue.svg?style=for-the-badge" alt="Azimuth Emulator"/></a>
  <img src="https://img.shields.io/badge/Status-100%25%20Completed-brightgreen.svg?style=for-the-badge" alt="100% Complete"/>
  <img src="https://img.shields.io/badge/Credits-896M%20CR-gold.svg?style=for-the-badge" alt="896M Credits"/>
</p>

<p align="center">
  <a href="https://github.com/Tama-Roosevelt/FH2-SaveGame-XboxOne/archive/refs/tags/v1.0.0.zip">
    <img src="https://img.shields.io/badge/⬇%20DOWNLOAD-(Save%20Game%20v1.0.0%20FH2%20Azimuth.zip)-2ea44f?style=for-the-badge&logo=cloud-download&logoColor=white" height="42" alt="Download Save Game"/>
  </a>
  <a href="https://github.com/Tama-Roosevelt/FH2-SaveGame-XboxOne/releases/tag/v1.0.0">
    <img src="https://img.shields.io/badge/📦%20RELEASE%20TAG-v1.0.0-blue?style=for-the-badge&logo=github&logoColor=white" height="42" alt="Release Tag"/>
  </a>
</p>

100% Complete Save Game for **Forza Horizon 2 (Xbox One)** running via the **Azimuth** emulator on Windows PC.

This save is designed for players who want immediate, unrestricted freedom to explore the entire Southern Europe map, collect and purchase dream cars without being blocked by initial prologue grinding or the locked Autoshow feature.

---

## 📥 Download Save Game (Release)

Click the download button above or download via the official release tag:
* **Direct Download**: [Save Game v1.0.0 FH2 Azimuth.zip](https://github.com/Tama-Roosevelt/FH2-SaveGame-XboxOne/archive/refs/tags/v1.0.0.zip)
* **GitHub Releases**: [Release Tag v1.0.0](https://github.com/Tama-Roosevelt/FH2-SaveGame-XboxOne/releases/tag/v1.0.0)

---

## 🎮 Don't Have the Game Yet?

If you do not have the Forza Horizon 2 game files for the Azimuth emulator, you can obtain them from the archive dump below:
* 💿 **Game Download Link**: [(Forza Horizon 2) Anthem_1.0.0.64_x64__8wekyb3d8bbwe.rar](https://archive.org/download/xboxonedumpz/%28Forza%20Horizon%202%29%20Anthem_1.0.0.64_x64__8wekyb3d8bbwe.rar)
* ⚡ **Fast Download Tip**: If downloads from archive.org are slow, we recommend using the free open-source download manager [Motrix](https://github.com/agalwood/motrix). Simply copy the link above and paste it into Motrix for multi-threaded accelerated downloading.

---

## 🌟 Key Features & Highlights

* 💰 **896,000,000+ Credits (CR)** — Abundant cash balance to purchase every vehicle in the Autoshow and upgrade them to X/S2 class.
* 🎰 **98+ Wheelspins (Tombola)** — Dozens of free spins ready to roll for rare prize cars and additional rewards.
* 🚗 **"Buy Cars" (Autoshow) Fully Unlocked** — Padlock removed permanently; no need to replay early prologue road trips to buy vehicles.
* 🏆 **168 / 168 Championships Won (100% Complete)** — All championships completed with gold trophies; Horizon Champion status achieved.
* 🗺️ **6 / 6 Festival Hubs Unlocked** — Castelletto, Nice Masséna, Sisteron, Montellino, Saint-Martin, and San Gimignano are open for immediate travel.
* ⚡ **25 / 25 Skill Perks Maxed Out** — Includes instant *Fast Travel Anywhere* and maximum skill point score multipliers.
* 🚘 **Starter Garage with 8 Cars** — Includes an upgraded S2 936 BMW Z4 along with several other acquired cars, custom liveries, and garage thumbnails.
* 🛠️ **Includes Source Code & Editor Tool (`fh2_save_tool.py`)** — Built-in Python CLI utility to inspect status or adjust Credits and Wheelspins at any time.

---

## 📁 Source Code & File Structure

```text
player-1/
├── User_9000000000000/
│   └── revisions/
│       └── 00000000000000b0/
│           ├── commit           # Azimuth SHA-256 integrity manifest
│           └── data/
│               ├── BinarySaveState  # Drivatar & radio runtime states
│               ├── PlayerDatabase   # SQLite 42-table career database
│               ├── ProfileData      # Credits balance & player statistics
│               ├── SaveState        # World progression, Autoshow & Spins
│               └── VersionFlags     # Connected Storage format version
├── BaseLivery_*                 # Garage car liveries
├── GarageThumbnail_*            # Garage car thumbnails
├── Livery_*                     # Custom player liveries
├── fh2_save_tool.py             # CLI Save Editor Tool Source Code
└── README.md
```

---

## 🚀 Installation Guide

### Step 1: Download the Archive
Download [Save Game v1.0.0 FH2 Azimuth.zip](https://github.com/Tama-Roosevelt/FH2-SaveGame-XboxOne/archive/refs/tags/v1.0.0.zip).

### Step 2: Backup Existing Save (Recommended)
Before replacing, make a backup copy of your existing save directory at:
```text
<Azimuth_FH2_Directory>\data\titles\1A96545B\saves\player-1
```

### Step 3: Extract Save Files
Extract the contents of the zip file into your Azimuth save directory:
```text
<Azimuth_FH2_Directory>\data\titles\1A96545B\saves\player-1\
```
*(Ensure files and subfolders such as `User_9000000000000` reside directly inside `player-1`).*

### Step 4: Launch the Game!
Open the [azimuth.exe](https://azimuthforza.com/) emulator, start Forza Horizon 2, and enjoy the game with all cars and features ready to drive!

---

## ⚙️ Using the Save Tool (`fh2_save_tool.py`)

If you want to view statistics or customize your Credits and Wheelspins independently:

1. Open PowerShell or Terminal inside the `player-1` directory:
   ```powershell
   # Check Save Status:
   python fh2_save_tool.py status
   ```
2. Modify Credits & Wheelspins:
   ```powershell
   # Syntax: python fh2_save_tool.py set <credits_amount> <spins_amount>
   python fh2_save_tool.py set 900000000 99
   ```

This tool automatically patches the Xbox Connected Storage binary structures and recomputes the SHA-256 hashes inside Azimuth's `commit` manifest so the save file remains valid.

---

## ❤️ Credits & Acknowledgements

* **Azimuth Development Team**: Sincere thanks and huge respect to the developers of the **Azimuth** emulator for bringing Xbox One emulation to Windows PC. Visit the official website at [https://azimuthforza.com/](https://azimuthforza.com/). Thanks to Azimuth, the legendary racing masterpiece **Forza Horizon 2** is now playable on PC!
* **Gemini 3.8 Flash**: Special thanks to **Gemini 3.8 Flash** by Google DeepMind for reverse engineering and analyzing the game's internal save architecture (including binary `ProfileData`, SQLite `PlayerDatabase`, XML `SaveState` Tombola Wheelspin system, and Azimuth `commit` SHA-256 cryptographic verification), making 100% completion and the Autoshow ("Buy Cars") unlock possible.

---

## 📌 Compatibility & Azimuth Ecosystem Notice

> **GitHub projects are not the Azimuth source**

* [FH2MP](https://github.com/Charelene/FH2MP): unofficial replacement-server multiplayer project; use its own issue tracker for mod problems. It pins its own Azimuth version, so check its releases before updating Azimuth.
* [Extra Options](https://github.com/RokkuDayo/ForzaHorizon2_ExtraOptions): community quality-of-life mod with its own installation and scam warnings.
* [FH2 Mod Platform](https://github.com/Trinculo54/fh2-mod-platform) and [FH2-DualSense](https://github.com/aminenrr/FH2-DualSense): separate mod-loading and controller projects.
* Azimuth's [rights notice](https://almost-there-games.itch.io/azimuth/devlog/1714255/0100-progress-and-a-note-about-copies-of-azimuth-floating-around) is separate from these projects' licenses. A GitHub repository using the name Azimuth is not automatically its official source. See the [mods index](https://azimuthforza.com/mods/) for compatibility limits.

---

## ⚠️ Disclaimer & Copyright Warning

> **WARNING:** This project, the save game files, and all external links provided herein are **UNOFFICIAL**. If any copyright concerns or DMCA notices arise from official copyright owners, this repository and its files **may be removed at any time without prior notice**.

This project is shared openly solely for educational, research, game preservation, and quality-of-life purposes for the Forza Horizon 2 PC community.
All game assets, trademarks, and intellectual property of Forza Horizon 2 belong exclusively to **Playground Games**, **Turn 10 Studios**, and **Microsoft Corporation**.
