# 🔐 A Simple Password Manager

A simple desktop application for generating and saving passwords. This tool provides a basic interface to create strong, unique passwords and manage login credentials locally.

## Features

  * **Strong Password Generation:** Creates a secure, randomized password using a mix of letters, symbols, and numbers.
  * **Automatic Clipboard Copy:** The generated password is automatically copied to the clipboard for easy pasting.
  * **Local Credential Storage:** Saves the website, email/username, and password together in a local `saved_passwords.txt` file.
  * **Simple User Interface:** The interface is clean, intuitive, and built with Python's Tkinter library.
  * **Input Validation:** Checks to ensure all fields are filled before saving an entry.

-----

## How to Run

Follow these steps to get the application running.

### 1\. Setup

First, download all the project files (or clone the repository) to a folder on your computer.

### 2\. Install Dependencies

This program requires the `pyperclip` library to copy text to the clipboard. Open your terminal, navigate to the project directory, and run the following command to install the necessary packages:

```sh
pip install -r requirements.txt
```

### 3\. Run the Application

Ensure the `logo.png` image file is in the same folder as the script. Execute the following command in your terminal:

```sh
python main.py
```

The application window should now appear.

-----

## ⚠️ Security Warning

This application is an educational project and **is not a secure password vault**.

Passwords are saved in a plain, unencrypted text file (`saved_passwords.txt`). Anyone with access to this file can read its contents. It is strongly recommended **not to use this application for real, sensitive credentials.**

-----

## Acknowledgments

This project was built based on the password manager module from the ["100 Days of Code: The Complete Python Pro Bootcamp"](https://www.udemy.com/course/100-days-of-code/) on Udemy.
