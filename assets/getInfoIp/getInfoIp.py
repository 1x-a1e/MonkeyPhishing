from requests import get
from colorama import Fore


def getInfoIp(ip: str) -> str:
    r = get(f"https://freeipapi.com/api/json/{ip}").json()

    return Fore.YELLOW + "ipAddress >> " + Fore.RESET + r["ipAddress"] + Fore.YELLOW + "\nCountry >> " + Fore.RESET + r["countryName"] + " (" + r["countryCode"] + ") - " + r["cityName"] + " " + r["regionName"] + " " + r["zipCode"] + " (" + r["continentCode"] + ")" + Fore.YELLOW + "\nProxy >> " + (Fore.RED if bool(r["isProxy"]) is False else Fore.GREEN) + str(r["isProxy"]) + Fore.YELLOW + "\nMaps link >> " + Fore.RESET + "https://www.google.com/maps?q=" + str(r["latitude"]) + "," + str(r["longitude"])
