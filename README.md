# F-Password-Generator

A user-friendly console program written in Python for generating secure passwords using "keys" as the seed for the password randomizer.
The goal is to create secure passwords from easy-to-remember words, phrases, or any other text that you can type.

## Keys

- **Main Key**: Saved in a `.env` file, this key can be considered the "global" key for any of your passwords.
- **Sub Key**: Whenever you generate a password, you will be prompted to enter a sub key, which will serve as the "seed" for your password.
- **Secondary Sub Key**: Another optional key you can enter, or you can skip this step.

### Examples

You can use the keys in this way:
- Main Key: your name or just a global password for all your passwords
- Sub Key: the name of the service you want the password to be used for
- Secondary Sub Key: an easy password you can remember

In this case, you could easily regenerate the same password if you provide the same keys, making it easy to recover the password, but hard to brute force.

## Installation
You obviously need python for this to work, the version I used was `3.12.3`

After downloading the repository, just do `pip install -r requirements.txt` and you could just run the program on a console after that
