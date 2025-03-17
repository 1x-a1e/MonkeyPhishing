from colorama import Fore
import json
import importlib

from assets.printLogo.printLogo import printLogo


def site():
    while True:
        printLogo()

        with open("./menu/site/all.json", "r") as f:
            ff = json.load(f)
            sett = {}

            i = 0
            for set in ff:
                print(Fore.YELLOW + "[" + str(i) + "]" + Fore.RESET + " " + str(set))
                i += 1
                sett[str(set)] = str(ff[set])

            print(Fore.YELLOW + "[99] Back")

            try:
                choice = int(input(Fore.YELLOW + ">> "))
                if choice == 99:
                    break

                key = list(sett.keys())
                selected_key = key[int(choice)]

                mod = importlib.import_module(
                    f"menu.site.siteTemplate.{sett[selected_key]}.{sett[selected_key]}"
                )
                mod.server()
            except IndexError:
                print(Fore.RED + "Invalid option" + Fore.RESET)
                input("Press Enter to continue...")
                continue
