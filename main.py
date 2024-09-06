import os
import shutil
import subprocess
import requests
import ctypes
import gc
from colorama import init, Fore, Style
from packaging import version

init(autoreset=True)

class PCPerformanceBoost:
    VERSION = "v1.0.0.8"
    GITHUB_REPO_URL = "https://api.github.com/repos/Jesewe/PCPerformanceBoost-Reload/tags"

    def __init__(self):
        self.set_console_title(f"PCPerformanceBoost | Reload")

    def set_console_title(self, title):
        ctypes.windll.kernel32.SetConsoleTitleW(title)

    def welcome_message(self):
        print(Fore.LIGHTMAGENTA_EX + "[*] Welcome to PCPerformanceBoost!")
        print(Fore.LIGHTMAGENTA_EX + "[*] This program optimizes the performance of your computer.\n")

    def check_for_updates(self):
        try:
            response = requests.get(self.GITHUB_REPO_URL)
            response.raise_for_status()
            latest_version = response.json()[0]["name"]
            if version.parse(latest_version) > version.parse(self.VERSION):
                print(Fore.LIGHTYELLOW_EX + f"[*] New version available: {latest_version}. Please update for the latest fixes and features.\n")
            else:
                print(Fore.GREEN + "[*] You are using the latest version.\n")
        except requests.RequestException as ex:
            print(Fore.RED + f"[!] Error checking for updates: {ex}")

    def perform_optimizations(self):
        self.optimize_memory()
        self.clean_cache()
        self.clean_temp_files()
        self.clean_crash_dumps()
        self.clear_dns_cache()

    def optimize_memory(self):
        try:
            gc.collect()
            print(Fore.GREEN + "[+] Memory optimization is complete.")
        except Exception as ex:
            print(Fore.RED + f"[!] Error optimizing memory: {ex}")

    def clean_cache(self):
        try:
            subprocess.run(["cleanmgr.exe", "/autoclean"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
            print(Fore.GREEN + "[+] Cache cleanup is complete.")
        except subprocess.CalledProcessError as ex:
            print(Fore.RED + f"[!] Error cleaning cache: {ex}")

    def clean_temp_files(self):
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

    def clean_crash_dumps(self):
        local_crash_dumps_path = os.path.join(os.environ.get("LOCALAPPDATA"), "CrashDumps")
        try:
            if os.path.exists(local_crash_dumps_path):
                shutil.rmtree(local_crash_dumps_path)
                print(Fore.GREEN + "[+] CrashDumps folder cleanup is complete.")
            else:
                print(Fore.CYAN + "[?] CrashDumps folder not found.")
        except Exception as ex:
            print(Fore.RED + f"[!] Error cleaning CrashDumps folder: {ex}")

    def clear_dns_cache(self):
        try:
            subprocess.run(["ipconfig", "/flushdns"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
            print(Fore.GREEN + "[+] DNS cache cleanup is complete.")
        except subprocess.CalledProcessError as ex:
            print(Fore.RED + f"[!] Error clearing DNS cache: {ex}")

    def completion_message(self):
        print(Fore.LIGHTYELLOW_EX + "\n[*] Optimization is complete.")
        input(Style.RESET_ALL + "[*] Press Enter to exit.")

    def run(self):
        self.welcome_message()
        self.check_for_updates()
        self.perform_optimizations()
        self.completion_message()


if __name__ == "__main__":
    optimizer = PCPerformanceBoost()
    optimizer.run()