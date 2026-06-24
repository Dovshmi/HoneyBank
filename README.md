# HoneyBank — Local Password Manager

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-blue)
![SQLite](https://img.shields.io/badge/Database-SQLite-003B57?logo=sqlite&logoColor=white)
![PyInstaller](https://img.shields.io/badge/Build-PyInstaller-orange)
![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey)
![License](https://img.shields.io/badge/License-GPL--3.0-green)

A lightweight desktop password manager built with Python, Tkinter, and SQLite.

HoneyBank stores login entries locally on your computer, organizes them by category and website, and includes a quick “Magic Login” workflow for filling credentials into websites.

> **Security note:** HoneyBank is a personal/educational desktop project. It uses a hashed master password, but saved site passwords are currently stored using reversible encoding rather than modern authenticated encryption. Do **not** rely on this as your primary password manager for high-value accounts until the encryption model is upgraded.

---

## Overview

HoneyBank is a local-first password manager designed around a simple workflow:

1. Open the app.
2. Unlock it with a master password.
3. Browse saved accounts by category and website.
4. Add, update, delete, or auto-fill login details.
5. Create or restore local database backups when needed.

The project does not depend on a cloud backend. Its data is stored on the user’s machine in a local SQLite database.

---

## Product Goals

- Keep password storage local and simple.
- Provide a small desktop GUI instead of a command-line-only tool.
- Make saved logins easy to organize by category and site.
- Support quick login workflows for sites that require username, password, and optionally a third field.
- Allow basic customization through themes and saved window placement.
- Keep the project readable for learning Python GUI development, SQLite, packaging, and desktop automation.

---

## Core Features

### Vault and Login Management

- Master password screen on startup.
- Local SQLite database stored under the user’s Documents folder.
- Category-based organization for saved sites.
- Add new login entries with:
  - site name
  - username
  - password
  - category
  - login URL
  - optional third login field
- Update existing username/password values.
- Delete saved login entries.
- View saved accounts in a structured tree/table interface.

### Magic Login

HoneyBank includes a guided auto-fill flow:

- Opens the saved login URL in the browser.
- Prompts the user to click the username field.
- Writes the saved username.
- Prompts the user to click the password field.
- Writes the saved password.
- Supports an optional third field for services that need another identifier.

This is handled through desktop automation libraries, so the browser and target webpage must be visible and focused during the process.

### Settings and Personalization

- Save app window position.
- Change between built-in color themes:
  - Honey
  - Pink
  - Blue Navy
  - Money Green
  - Sky Dream
  - Business
  - Night
  - Light
- Keep the small unlock window always on top.

### Backup and Restore

- Create a backup copy of the local database.
- Restore from an existing backup file.
- Backups are stored locally in the HoneyBank folder.

---

## Tech Stack

| Area | Technology |
| --- | --- |
| Language | Python |
| GUI | Tkinter / ttk |
| Database | SQLite |
| Password hashing | PBKDF2-HMAC-SHA256 |
| Desktop automation | PyAutoGUI, pynput |
| Packaging | PyInstaller |
| License | GPL-3.0 |

---

## Repository Structure

```text
HoneyBank/
├── .github/workflows/      # GitHub Actions workflow
├── Honey.ico               # Application icon
├── HoneyBank.py            # Main Tkinter desktop app
├── inputdatabase.py        # SQLite database and password helper functions
├── MordiBot.exe            # Existing compiled executable in the repo
├── README.md               # Project documentation
├── LICENSE                 # GPL-3.0 license
└── .gitignore
```

---

## Data Location

On first run, HoneyBank creates a local folder in the user’s Documents directory:

```text
~/Documents/Honeybank/
├── Data.db
└── beckup/
```

`Data.db` contains the local SQLite database. The backup folder is currently named `beckup` in the implementation, so the README uses the same spelling to match the actual project path.

---

## Security Model

HoneyBank currently uses two different protection approaches:

### Master Password

The master password is hashed using PBKDF2-HMAC-SHA256 with a random salt and 100,000 iterations.

This is a reasonable direction for verifying a master password, because the plaintext master password is not stored directly.

### Stored Site Passwords

Saved site passwords are currently transformed with string reversal and Base64-style encoding before being written to SQLite.

That is **not the same as encryption**. Anyone with access to the database and source code could reverse the process.

### Recommended Security Upgrade

For a future production-ready version, replace the reversible password transformation with authenticated encryption, for example:

- derive an encryption key from the master password using a strong KDF;
- encrypt each saved password with AES-GCM or Fernet;
- authenticate encrypted data to detect tampering;
- never display or log sensitive data to the console;
- add database migration support for old vault files.

---

## Requirements

- Windows 10/11 recommended
- Python 3.x
- pip
- Tkinter support
- Browser installed for the Magic Login flow

Python packages used by the app:

```bash
pip install pyautogui pynput pyinstaller
```

`sqlite3`, `hashlib`, `base64`, `os`, `shutil`, `threading`, and `tkinter` are part of the Python standard library in typical Windows Python installs.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/Dovshmi/HoneyBank.git
cd HoneyBank
```

Create and activate a virtual environment:

```bash
python -m venv .venv
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install pyautogui pynput pyinstaller
```

Run the app:

```bash
python HoneyBank.py
```

---

## Build a Windows Executable

You can package the app with PyInstaller:

```bash
pyinstaller --onefile --windowed --icon=Honey.ico --name HoneyBank HoneyBank.py
```

After the build finishes, the executable should be available inside:

```text
dist/HoneyBank.exe
```

If the icon causes a build issue, try building without the icon flag:

```bash
pyinstaller --onefile --windowed --name HoneyBank HoneyBank.py
```

---

## Usage Guide

### First Launch

On first launch, HoneyBank creates its local database folder and asks you to enter a master password. That first password becomes the password required to unlock the app later.

### Add a Login

1. Unlock HoneyBank.
2. Click **Sign in a new user**.
3. Select or create a category.
4. Add the site, username, password, URL, and optional special field.
5. Click **Submit**.

### Use Magic Login

1. Select a saved login entry.
2. Click **Magic login**.
3. HoneyBank opens the saved URL.
4. Click the username field when prompted.
5. Click the password field when prompted.
6. Click the optional third field if the saved login uses one.

### Create a Backup

1. Open **Settings**.
2. Click **Create a new backup file**.
3. A copy of the database is saved in the local backup folder.

### Restore a Backup

1. Open **Settings**.
2. Click **Load a backup file**.
3. Select a previous database backup.
4. Restart the app if needed.

---

## Known Limitations

- Saved passwords are not yet protected with modern encryption.
- The app currently targets local desktop usage, mainly Windows.
- Some UI labels contain typos in the current implementation.
- The database path is hardcoded to the user’s Documents folder.
- There is no formal test suite yet.
- Magic Login depends on browser focus and page layout, so it may not work consistently on every website.

---

## Roadmap

- Replace reversible password encoding with real authenticated encryption.
- Add a `requirements.txt` file.
- Add a clean release workflow for Windows builds.
- Improve UI text and layout consistency.
- Add password generator support.
- Add search/filter functionality.
- Add import/export for encrypted vault backups.
- Add automated tests for database operations.
- Add database migration/versioning support.
- Add screenshots or GIFs to demonstrate the UI.

---

## Development Notes

This project is useful for learning:

- Python desktop GUI development with Tkinter;
- SQLite database design and CRUD operations;
- master password verification with hashing;
- desktop automation with PyAutoGUI and pynput;
- packaging Python apps into Windows executables with PyInstaller.

Because this is a password-related project, future development should prioritize security improvements before adding more convenience features.

---

## License

This project is licensed under the **GNU General Public License v3.0**.

See the [`LICENSE`](LICENSE) file for details.

---

## Author

Created by **Dovshmi**.

GitHub: [@Dovshmi](https://github.com/Dovshmi)
