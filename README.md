# Password Manager

## Overview

This is a simple command-line-based **Password Manager** that allows users to securely manage their passwords. The passwords are encrypted using the `cryptography` library with a key, ensuring that sensitive information is kept safe. Users can create, load, and manage their passwords with ease.

## Features

- **Create a New Key**: Generates a new encryption key and saves it to a file.
- **Load an Existing Key**: Loads an encryption key from a file.
- **Create a New Password File**: Creates a file to store encrypted passwords.
- **Load an Existing Password File**: Loads and decrypts passwords from an existing file.
- **Add a New Password**: Adds a password for a specific site to the password file.
- **Get a Password**: Retrieves a password for a specific site.
- **Quit**: Exit the application.

## Installation

1. **Clone the repository**:
   
   ```bash
   git clone https://github.com/casey829/Password-manager

2. **Navigate to the project directory**:

bash

cd password-manager


3. **Install required dependencies**:

Make sure you have cryptography library installed:

bash

pip install cryptography

**Usage**
To run the password manager, use:

bash

python password_manager.py

**Application Menu**

Copy code
(1) Create a new key.
(2) Load an existing key.
(3) Create new password file.
(4) Load existing password file.
(5) Add a new password.
(6) Get a password.
(q) Quit

***How to Use***
1. Create or Load a Key: Before adding or retrieving passwords, you need to create or load an encryption key.

 . Choose option 1 to create a new key file and save it to a location of your choice.
 . Choose option 2 to load an existing key file.

2. Create or Load a Password File:

  .Choose option 3 to create a new password file. You can provide initial values if needed.
  .Choose option 4 to load an existing password file.
3. Manage Passwords:

Choose option 5 to add a new password. You'll be prompted to enter the site name and the password.

Choose option 6 to retrieve a password for a specific site.
4. Exit:
  .Choose option q to quit the application.

**Example**
Here's an example workflow:

1. Create a new key:

Copy code
Enter your choice: 1
Enter path for new key file: ./my_key.key

2. Create a new password file:

Enter your choice: 3
Enter path for new password file: ./my_passwords.txt

3. Add a new password:

Enter your choice: 5
Enter the site: Facebook
Enter the password: mySecretPassword123

4. Retrieve a password:

Enter your choice: 6
What site do you want the password for? Facebook
Password for Facebook: mySecretPassword123
Quit:

5. less

Enter your choice: q
Goodbye!

**File Structure**
. password_manager.py - Main Python file containing the password manager code.
. requirements.txt - Dependencies for the project.
. README.md - This file.
. my_key.key - Example key file for encryption/decryption.
. my_passwords.txt - Example password file.

**Dependencies**
cryptography: A library for encryption and cryptographic operations.
Install it via:

pip install cryptography

**Security Note**

The encryption key is crucial for decrypting your passwords. Keep it safe and secure.
Do not share your key file or password file publicly.
If you lose your key file, you won't be able to decrypt the saved passwords.

**License**
This project is licensed under the MIT License. See the LICENSE file for more details.

**Contributing**
Feel free to submit a pull request or file an issue if you have any suggestions or find any bugs!


