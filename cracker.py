import os
import zipfile
from time import time
from itertools import product
import string
from tqdm import tqdm

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def generate_passwords(length):
    characters = string.ascii_letters + string.digits
    return (''.join(combination) for combination in product(characters, repeat=length))

def main(file_path, max_length=8):
    try:
        zip_ = zipfile.ZipFile(file_path)
    except zipfile.BadZipfile:
        print(" [!] Please check the file's Path. It doesn't seem to be a ZIP file.")
        return

    password = None
    i = 0
    c_t = time()

    for length in range(1, max_length + 1):
        for candidate in tqdm(generate_passwords(length), desc=f"Trying passwords (length {length})"):
            i += 1
            password = candidate
            try:
                zip_.extractall(pwd=password.encode())
                t_t = time() - c_t
                print("\n [*] Password Found :)\n" + f" [*] Password: {password}\n")
                print(f" [***] Took {t_t} seconds to Crack the Password. That is, {i / t_t} attempts per second.")
                return
            except Exception:
                pass
    print(" [X] Sorry, Password Not Found :(")

cls()
banner = '\n ###################################\n'
banner += ' # ZIP Password BruteForcer        #\n'
banner += ' ###################################\n'
banner += ' # Coded By Sifat and chatgpt                   #\n'
banner += ' #              #\n'
banner += ' ##\n'
banner += ' #                #\n'
banner += ' ###################################\n'
banner += ' [1] Zip Password Cracker\n'
banner += ' [0] Exit\n'
print(banner)

a = int(input(" [?] Enter Number : "))
if a == 0:
    cls()
    print(" [!] Good Bye :)")
elif a == 1:
    file_name = input(" [+] ZIP File Name (e.g., Serenity.zip): ")
    file_path = os.path.join(os.path.expanduser("~"), "Downloads", file_name)
    print(" [+] ZIP File Path: ", file_path)  
    main(file_path)
else:
    print(" [X] Invalid choice.")
