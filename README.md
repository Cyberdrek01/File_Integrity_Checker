# File Integrity Checker

A lightweight, cross-platform File Integrity Monitor (FIM) built in Python. It uses SHA-256 cryptographic hashing to establish a verified baseline of your file system and continuously detects unauthorized modifications, additions, or deletions — with a clean graphical interface for non-technical users.

---

## Table of Contents

- [Background](#background)
- [Problem Statement](#problem-statement)
- [Solution Overview](#solution-overview)
- [Features](#features)
- [Technical Stack](#technical-stack)
- [Installation](#installation)
  - [Option A: Run from Source](#option-a-run-from-source-developers)
  - [Option B: Download the Executable](#option-b-download-the-executable-end-users)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [License](#license)

---

## Background

File Integrity Monitoring (FIM) is a foundational cybersecurity control used to validate the state of operating system files, application binaries, and configuration files. It operates by comparing the current state of a file system against a known, verified baseline — flagging any deviation as a potential security incident.

FIM is a recommended control under multiple compliance frameworks including PCI-DSS, HIPAA, and NIST SP 800-53.

---

## Problem Statement

Modern systems face persistent threats from malware, ransomware, insider actors, and post-compromise attackers. A common post-exploitation tactic is to silently alter system files to:

- Establish persistence mechanisms
- Weaken security configurations
- Replace legitimate binaries with trojanized versions

These file-level changes are often subtle and occur entirely in the background. Without an automated mechanism to continuously verify the digital fingerprints of critical files, a compromised system may remain undetected indefinitely — leading to data exfiltration, lateral movement, or catastrophic failure.

---

## Solution Overview

This tool provides a lightweight, self-contained File Integrity Checker that rapidly detects unauthorized file system changes across a monitored directory.

**Architecture highlights:**

- **Cryptographic Engine** — Employs the SHA-256 hashing algorithm to generate immutable digital fingerprints for every file within a monitored directory.
- **Memory-Optimized Scanning** — Files are read in 8KB chunks to prevent RAM exhaustion during scans of large directories or enterprise-scale data stores.
- **Persistent Baseline** — The verified baseline (known-good state) is serialized to a local `baseline.json` file, enabling long-term monitoring that survives system reboots.
- **Graphical Interface** — A Tkinter-based GUI provides an accessible control panel to establish baselines, run verification scans, and review detailed incident reports identifying exactly which files were modified, added, or deleted.

---

## Features

- SHA-256 based file fingerprinting
- Chunked file reading for memory efficiency
- Persistent baseline storage via `baseline.json`
- GUI-driven workflow — no command-line required for end users
- Detailed change reports: modified, added, and deleted files
- Zero external dependencies — standard library only
- Standalone executable available for non-Python environments

---

## Technical Stack

| Component     | Detail                          |
|---------------|---------------------------------|
| Language      | Python 3.x                      |
| GUI Framework | Tkinter (standard library)      |
| Hashing       | SHA-256 via `hashlib`           |
| Storage       | JSON serialization via `json`   |
| Dependencies  | None — standard library only    |

---

## Installation

### Option A: Run from Source (Developers)

Requires Python 3.x installed on your system.

**1. Clone the repository:**
```bash
git clone https://github.com/Cyberdrek01/File_Integrity_Checker.git
```

**2. Navigate to the project directory:**
```bash
cd File_Integrity_Checker
```

**3. Run the application:**
```bash
python File_Integrity_Checker.py
```

---

### Option B: Download the Executable (End Users)

For users without a Python environment, a pre-compiled standalone executable is available.

1. Navigate to the [Releases](https://github.com/Cyberdrek01/File_Integrity_Checker/releases) section on the right side of this repository page.
2. Download the latest `File_Integrity_Checker.exe` file.
3. Place the executable in your desired monitoring directory and double-click to run.

No installation or Python environment is required.

---

## Usage

1. **Set a Baseline** — Select a directory to monitor and establish a baseline. The tool will hash every file and store the results in `baseline.json`.
2. **Run a Verification Scan** — At any subsequent point, run a scan against the same directory. The tool compares current file hashes against the stored baseline.
3. **Review the Incident Report** — Any files that were modified, added, or deleted since the baseline was established will be flagged and listed in the results panel.

It is recommended to establish a fresh baseline immediately after a clean system setup or a verified software deployment.

---

## Project Structure
```
File_Integrity_Checker/
├── File_Integrity_Checker.py            # Main application entry point
├── baseline.json     # Auto-generated baseline hash store (created at runtime)
└── README.md
```

---

## License

This project is licensed under the [MIT License](LICENSE). You are free to use, modify, and distribute this software in accordance with the license terms.
