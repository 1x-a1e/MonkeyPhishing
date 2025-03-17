import json
from colorama import Fore

from assets.getInfoIp.getInfoIp import getInfoIp
from assets.addIp.addIp import addIp


def logs(request):
    with open("./settings/settings.json", "r") as f:
        ff = json.load(f)
        if ff["logs"] is True:
            if not request.cookies.get("user"):
                addIp(request.remote_addr)
                print(
                    Fore.RED + "[!] " + Fore.RESET + "User connected!")
                print(getInfoIp(request.remote_addr))
