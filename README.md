# File Integrity Checker

A lightweight, GUI-based File Integrity Monitor built in Python. This application detects unauthorized modifications, additions, or deletions of files within a specified directory by calculating and comparing cryptographic hashes against a known good baseline.

## Features

* **Directory Scanning:** Recursively scans folders and subfolders to map all files.
* **Cryptographic Hashing:** Utilizes the SHA-256 algorithm to generate unique digital fingerprints. Reads files in 8KB chunks to ensure memory efficiency when handling large datasets.
* **Baseline Generation:** Captures the initial state of a directory and stores the hash data in a persistent JSON file.
* **Integrity Verification:** Compares the current state of the directory against the saved baseline to instantly identify:
  * Modified files (altered content)
  * Newly added files
  * Deleted or missing files
* **Graphical User Interface:** Features a clean, accessible GUI built with Tkinter, including a control panel, live status updates, and actionable alert dialogs.

## Tech Stack

* **Language:** Python 3.x
* **Libraries:** `hashlib`, `os`, `json`, `tkinter` (Standard Python libraries; no external dependencies required)

## Usage

### Running from Source

1. Clone this repository to your local machine:
   ```bash
   git clone [https://github.com/Cyberdrek01/File_Integrity_Checker.git](https://github.com/Cyberdrek01/File_Integrity_Checker.git)
2. Navigate to the project directory:

Bash 
cd File_Integrity_Checker
Run the application:

Bash
python fim.py
Application Workflow
Create a Baseline: Click "Create Baseline" and select a target folder. The application will scan the folder and generate a baseline.json file.

Verify Integrity: Click "Verify Integrity" and select the monitored folder.

Review the Report: The built-in log output will detail the precise file paths of any detected modifications, additions, or deletions.
