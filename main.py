import random
import pyperclip
import hashlib
import dotenv
import time
import os

dotenv.load_dotenv()
key = os.getenv("key", "FPasswordGenerator")

if key == "FPasswordGenerator":
    print("\nIt seems that you don't have a .env file with your key in it, it will default to 'FPasswordGenerator'.")
    print('In case you want a custom key, just create a file called .env in the same directory as the program and inside put:\nkey="your custom key"')

lowercase_letters = "qwertyuiopasdfghjklzxcvbnm"
uppercase_letters = "QWERTYUIOPASDFGHJKLZXCVBNM"
characters = "!#$%&*+-/~"
numbers = "1234567890"
pool = lowercase_letters + uppercase_letters + characters + numbers # creates a pool of all lowercase and uppercase letters, some characters and numbers

print("\nStarting the password generator, press (ctrl + c) anytime to cancel or just close the console.")

def randomize(length):
    result = [ # adds 4 character of each list, so theres always one uppercase letter, one lowercase letter, one character and one number.
        random.choice(lowercase_letters),
        random.choice(uppercase_letters),
        random.choice(characters),
        random.choice(numbers)
    ]
    for _ in range(length-4): # -4 because theres 4 added characters already
        result.append(random.choice(pool))
    random.shuffle(result) # shuffles the password, so the 4 added characters arent all in the start
    return "".join(result) 

try:
    subkey = input("- Insert subkey, or just hit enter to skip.\nsubkey=").lower()
    second_subkey = input("- Insert second subkey, or just hit enter to skip.\nsecond_subkey=").lower()
    
    combined_key = hashlib.sha512(f"{key}:{subkey}:{second_subkey}".encode()).hexdigest() # extra layer of security

    random.seed(combined_key)

    while True: # Loop until a valid length is inserted
        try:
            length = int(input("- Insert the length of the password\nlength="))
            if length < 4: # because of the already added characters I had to put this
                print("## Warning: length is less than 4, insert a bigger number.")
                continue
            if length < 30: # Just a warning for more security
                print("## Warning: length is less than 30, less length is less secure.")
                print("## Do you want to retype the length? ('y' to retype, anything else to continue):")
                user_input = input().lower()
                if user_input == "y":
                    continue
            break
        except ValueError:
            print("## Invalid: enter a valid integer for the length.") # in case someone inputs anything else than a integer

    pswrd = randomize(length)  # pswrd = password
    
    print(f"\n{pswrd}\n")
    pyperclip.copy(pswrd)
    print("### Password copied to the clipboard.")
    print("### This program will close in 3 seconds.")
    time.sleep(3)
except Exception as e:
    pyperclip.copy(e)
    print(f"## Unexpected error: {e}")
    print("\n## Error copied to clipboard.\n## Closing in 10 seconds.")
    time.sleep(10)
