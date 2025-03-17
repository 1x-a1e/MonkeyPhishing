# MonkeyPhishing

![MonkeyLogo.png](/img/MonkeyLogo.png)

## What is it?

> MonkeyPhishing aims to bring back a phishing tool optimized for new technologies.

## What technologies does it use?

- [Python](https://www.python.org/)
- [Flask](https://pypi.org/project/Flask/)

## Installation

```sh
git clone <url>
pip install -r requirements.txt
sudo python MonkeyPhishing.py
```

## Usage

After installing, run:

```sh
python MonkeyPhishing.py
```

You will be presented with a menu with two options:
> PhishPanel => To create a phishing site
> Settings => Tool settings

### Settings setup
```sh
ip => Setup ip
port => Setup port
logs => See all user information and when they log in (this is saved)
otp => Option that also allows you to create a fake page to get the OTP code
```

### OTP code?
When this option is activated, the program redirects the victim to a malicious url where it will ask him to enter an otp code, each site has its own way and therefore this operation may or may not be available or may change.
When a user enters the credentials, the program will wait for your input to proceed with the redirection of the victim to the url (obviously this must be done simultaneously by the malicious person to obtain the otp code through an access with the credentials) after this it proceeds with an ENTER only when the program asks you and when you have requested the otp code affixed to the victim.
The user will enter the code and will be directed to an infinite loading just to simulate its correct functioning.

## Demonstration

### Devil
[View the video](img/PC.mp4)
### Victim
[View the video](img/MOBILE.mp4)
## Version 0.1

> The project is in early access, and currently, only a few pages are available for the tool.
> We welcome useful pull requests that improve the project. Any contribution is appreciated, and I'll try to update it as often as possible!

## Contributing

If you want to contribute, feel free to fork the repository and submit a pull request with improvements.

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

For any questions or suggestions, feel free to open an issue or contact me directly!

