# HoneyBank
HoneyBank Password Manager
HoneyBank is a simple yet secure password manager written in Python, utilizing SQLite for the database. The primary goal of HoneyBank is to provide users with a secure and convenient way to manage their passwords.

Features
Encryption: HoneyBank encrypts your stored passwords to ensure the security of your sensitive information.
Master Password: A single master password is required to access your stored passwords, making it the only password you need to remember.
Magic Login Button: Simplify the login process by using the "Magic Login" button. Clicking on the username and password fields will autofill your credentials, making login hassle-free.

# Getting Started
First wee need to install the application, we will use Pyinstaller.
```
pip install pyinstaller
```
Download the program files.
```
git clone https://github.com/Dovshmi/HoneyBank.git
```
Change to the program folder.
```
cd Honeybank
```
Using Pyinstaller install all the programs files with one command:
```
pyinstaller --onefile --windowed --icon=Honey.ico HoneyBank.py inputdatabase.py
```
# Congratulations you installed HoneyBank !!!
