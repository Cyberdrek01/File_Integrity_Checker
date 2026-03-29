import os
import hashlib
import json
import tkinter as tk
from tkinter import filedialog, scrolledtext, messagebox

#Core Engine
def calculate_hash(file_path, algorithm='sha256'):
    hash_func=hashlib.new(algorithm)
    try:
        with open(file_path,'rb') as file:
            while True:
                chunk = file.read(8192)
                if not chunk:
                    break
                hash_func.update(chunk)
            return hash_func.hexdigest()
    except Exception:
        return None
def scan_directory(folder_path):
    file_hashes={}
    for root,dirs,files in os.walk(folder_path):
        for file in files:
            full_path = os.path.join(root,file)
            file_hash=calculate_hash(full_path)
            if file_hash:
                file_hashes[full_path] = file_hash

    return file_hashes

#Saving & Loading
def create_baseline(folder_path, baseline_file="baseline.json"):
    log_to_screen(f"[*] Scanning '{folder_path}'...")
    update_status("Scanning directory... please wait.")

    current_state=scan_directory(folder_path)

    with open(baseline_file,"w")as file:
        json.dump(current_state,file,indent=4)

    log_to_screen(f"[+] SUCCESS: Baseline created!\n    Saved {len(current_state)} files to '{baseline_file}'.\n")
    update_status("Ready")

    messagebox.showinfo("Success", f"Baseline successfully created for {len(current_state)} files!")

def verify_files(folder_path,baseline_file="baseline.json"):
    if not os.path.exists(baseline_file):
        messagebox.showerror("Error", "No baseline found! Please create a baseline first.")
        return

    log_to_screen(f"[*] Verifying files in '{folder_path}'...")
    update_status("Verifying files... please wait.")

    with open(baseline_file,"r")as file:
        saved_baseline=json.load(file)

    current_state=scan_directory(folder_path)

    modified=[]
    added=[]
    deleted=[]

    for filepath, original_hash in saved_baseline.items():
        if filepath in current_state:
            if original_hash!=current_state[filepath]:
                modified.append(filepath)
        else:
            deleted.append(filepath)

    for filepath in current_state:
        if filepath not in saved_baseline:
            added.append(filepath)

    log_to_screen("\n"+"="*45)
    log_to_screen(f"            Integrity Check Report          ")
    log_to_screen("="*45)

    if not modified and not added and not deleted:
        log_to_screen("\n[+] STATUS: SECURE. No changes detected.")
        messagebox.showinfo("Secure", "All files match the baseline. No changes detected.")
    else:
        if modified:
            log_to_screen(f"\n[!] MODIFIED FILES DETECTED:")
            for f in modified: log_to_screen(f"    ->{f}")
        if added:
            log_to_screen(f"[!] NEW FILES ADDED:")
            for f in added: log_to_screen(f"    ->{f}")
        if deleted:
            log_to_screen(f"[!] FILES DELETED:")
            for f in deleted: log_to_screen(f"    ->{f}")

        messagebox.showwarning("Changes Detected!","Modifications were found in the monitored folder. Check the log for details.")
    log_to_screen("-"*50+"\n")
    update_status("Ready")

#GUI

def log_to_screen(message):
    output_box.config(state=tk.NORMAL)
    output_box.insert(tk.END, message+"\n")
    output_box.see(tk.END)
    output_box.config(state=tk.DISABLED)
def update_status(message):
    status_var.set(f"Status: {message}")
    root.update()

def action_create_baseline():
    folder_selected=filedialog.askdirectory(title="Select Folder to Baseline")
    if(folder_selected):
        create_baseline(folder_selected)

def action_verify_integrity():
    folder_selected=filedialog.askdirectory(title="Select Folder to Verify")
    if(folder_selected):
        verify_files(folder_selected)

def action_clear_screen():
    output_box.config(state=tk.NORMAL)
    output_box.delete('1.0', tk.END)
    output_box.config(state=tk.DISABLED)

#Window setup

root=tk.Tk()
root.title("File Integrity Monitor")
root.geometry("800x600")
root.configure(bg="#2b2b2b")

title_label=tk.Label(root,text="File Integrity Checker", font=("Arial", 16), bg="#2b2b2b", fg="white")
title_label.pack(pady=10)

button_frame=tk.Frame(root,bg="#2b2b2b")
button_frame.pack(pady=5)

btn_baseline=tk.Button(button_frame,text="1. Create baseline",font=("Arial", 10, "bold"), bg="#4CAF50", fg="white", width=20,command=action_create_baseline)
btn_baseline.grid(row=0,column=0,padx=10)

btn_verify=tk.Button(button_frame, text="2. Verify Integrity",font=("Arial", 10, "bold"), bg="#2196F3", fg="white", width=20, command=action_verify_integrity)
btn_verify.grid(row=0,column=1,padx=10)

btn_clear=tk.Button(root,text="Clear Output",font=("Arial",9),bg="#f44336",fg="white", command=action_clear_screen)
btn_clear.pack(pady=5)

#output box

output_box=scrolledtext.ScrolledText(root,width=70, height=20,font=("Consolas",10),bg="#1e1e1e",fg="#00ff00")
output_box.pack(pady=10)
output_box.config(state=tk.DISABLED)

log_to_screen("System Ready. Select an action above.")

status_var = tk.StringVar()
status_var.set("Status: Ready")
status_bar = tk.Label(root, textvariable=status_var, font=("Segoe UI", 9), bg="#007acc", fg="white", anchor="w", padx=10)
status_bar.pack(side="bottom", fill="x")

log_to_screen("System Ready. Select an action from the Control Panel.")

if __name__ == "__main__":
    root.mainloop()
