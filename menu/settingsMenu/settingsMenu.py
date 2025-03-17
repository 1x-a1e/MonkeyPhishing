import json
from colorama import Fore

from assets.printLogo.printLogo import printLogo


def settingsMenu():
    while True:
        printLogo()

        i = 0
        sett = {}

        with open("./settings/settings.json", "r+") as f:
            ff = json.load(f)

            for set in ff:
                if type(ff[set]) is bool:
                    color = Fore.RED if bool(ff[set]) is False else Fore.GREEN
                else:
                    color = Fore.YELLOW

                print(
                    Fore.YELLOW + "[" + str(i) + "] " + Fore.RESET + str(set) +
                    " = " + color + str(ff[set])
                    )

                sett[str(set)] = bool(ff[set]) if type(ff[set]) is bool else str(ff[set])
                i += 1
            print(Fore.YELLOW + "[99] Back")

            try:
                change = int(input(">> "))

                if change == 99:
                    break

                key = list(sett.keys())

                selected_key = key[int(change)]
                if type(ff[selected_key]) is bool:
                    ff[selected_key] = True if not ff[selected_key] else False
                else:
                    value = input("Ente options >> ")
                    ff[selected_key] = value

                f.seek(0)
                json.dump(ff, f, indent=4)
                f.truncate()
            except IndexError:
                print(Fore.RED + "Invalid option" + Fore.RESET)
                input("Press Enter to continue...")
                continue
