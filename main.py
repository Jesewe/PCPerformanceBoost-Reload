import os
import shutil
import subprocess
import requests
import ctypes
import gc
from colorama import init, Fore, Style

init(autoreset=True)

VERSION = "1.0.0.6"
UPDATE_URL = "https://raw.githubusercontent.com/Jesewe/PCPerfomanceBoost-Reload/main/latest_version.txt"

def main():
    set_console_title("PCPerformanceBoost | Reload")
    welcome_message()
    check_for_updates()
    perform_optimizations()
    completion_message()

def set_console_title(title):
    ctypes.windll.kernel32.SetConsoleTitleW(title)

def welcome_message():
    print(Fore.LIGHTMAGENTA_EX + "[*] Welcome to PCPerformanceBoost!\n")
    print(Fore.LIGHTMAGENTA_EX + "[*] This program optimizes the performance of your computer.\n")

def check_for_updates():
    try:
        response = requests.get(UPDATE_URL)
        response.raise_for_status()
        latest_version = response.text.strip()
        if latest_version != VERSION:
            print(Fore.LIGHTYELLOW_EX + f"[*] New version available: v{latest_version}. Please update for the latest fixes and features.\n")
        else:
            print(Fore.GREEN + "[*] You have the latest version installed.\n")
    except requests.RequestException as ex:
        print(Fore.RED + f"[!] Error checking for updates: {ex}")

def perform_optimizations():
    optimize_memory()
    clean_cache()
    clean_temp_files()
    clean_crash_dumps()
    clear_dns_cache()

def optimize_memory():
    try:
        gc.collect()
        print(Fore.GREEN + "[+] Memory optimization is complete.")
    except Exception as ex:
        print(Fore.RED + f"[!] Error optimizing memory: {ex}")

def clean_cache():
    try:
        subprocess.run(["cleanmgr.exe", "/autoclean"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        print(Fore.GREEN + "[+] Cache cleanup is complete.")
    except subprocess.CalledProcessError as ex:
        print(Fore.RED + f"[!] Error cleaning cache: {ex}")

def clean_temp_files():
    temp_folder_path = os.path.join(os.environ.get("TEMP"))
    for root, dirs, files in os.walk(temp_folder_path):
        for file in files:
            try:
                os.remove(os.path.join(root, file))
            except Exception:
                pass
        for directory in dirs:
            try:
                shutil.rmtree(os.path.join(root, directory))
            except Exception:
                pass
    print(Fore.GREEN + "[+] Temporary files cleanup is complete.")

def clean_crash_dumps():
    local_crash_dumps_path = os.path.join(os.environ.get("LOCALAPPDATA"), "CrashDumps")
    try:
        if os.path.exists(local_crash_dumps_path):
            shutil.rmtree(local_crash_dumps_path)
            print(Fore.GREEN + "[+] CrashDumps folder cleanup is complete.")
        else:
            print(Fore.CYAN + "[?] CrashDumps folder not found.")
    except Exception as ex:
        print(Fore.RED + f"[!] Error cleaning CrashDumps folder: {ex}")

def clear_dns_cache():
    try:
        subprocess.run(["ipconfig", "/flushdns"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        print(Fore.GREEN + "[+] DNS cache cleanup is complete.")
    except subprocess.CalledProcessError as ex:
        print(Fore.RED + f"[!] Error clearing DNS cache: {ex}")

def completion_message():
    print(Fore.LIGHTYELLOW_EX + "\n[*] Optimization is complete.")
    input(Style.RESET_ALL + "[*] Press Enter to exit.")

if __name__ == "__main__":
    main()