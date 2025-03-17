from colorama import Fore
import os

from assets.printLogo.printLogo import printLogo
from menu.settingsMenu.settingsMenu import settingsMenu
from menu.site.site import site


def main():
    while (True):
        printLogo()
        print(Fore.YELLOW + "[1]" + Fore.RESET + " PhishPanel")
        print(Fore.YELLOW + "[0]" + Fore.RESET + " Settings")
        print(Fore.YELLOW + "[99]" + Fore.RESET + " Exit")
        menu = int(input(Fore.YELLOW + '>> '))

        match menu:
            case 1:
                site()
            case 0:
                settingsMenu()
            case 99:
                os.system("clear || cls")
                print('\nBye!!!')
                exit(0)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        os.system("clear || cls")
        print('\nBye!!!')
