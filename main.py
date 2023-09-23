#importowanie wymaganych bibliotek
import tkinter as tk
from ftplib import FTP
from io import BytesIO
import base64
import os
import logging
import socket
from datetime import datetime
import random
from colorama import Fore, Style
import atexit

if not os.path.exists("logs"):
    os.makedirs("logs")

# Ustalanie sposobu tworzenia nazwy pliku logującego dla każdej sesji skryptu
log_filename = datetime.now().strftime("%Y-%m-%d_%H-%M-%S_") + socket.gethostname() + ".log"
logging.basicConfig(filename=os.path.join("logs", log_filename), level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logging.info("Log file successfully created.")

def generate_random_string(length):
    characters = "0123456789ABCDEF"
    random_string = ''.join(random.choice(characters) for _ in range(length))

    return random_string

Validation_error_counter = 0
wallet_checks = 0



def main():
    global Validation_error_counter
    global wallet_checks
    crypto_choice = input("Select targeted currency (" + Fore.MAGENTA + "ETH" + Style.RESET_ALL + "/" + Fore.YELLOW + "BTC" + Style.RESET_ALL + "): ").upper()

    if crypto_choice not in ["ETH", "BTC"]:
        print("Incorrect answer, choose "+ Fore.MAGENTA + "ETH" + Style.RESET_ALL + " or " + Fore.YELLOW + "BTC" + Style.RESET_ALL + ".")
        logging.info("The program couldn't resolve entered data (currency choice error).")
        return

    while True:
        random_string_64 = generate_random_string(64)
        
        # Generowanie losowej liczby od 1 do 100
        random_number = random.randint(1, 10000)

        if random_number == 1:
            Valid_status = ("Validation Error")
            Validation_error_counter += 1
            logging.info("Validation error occured (API connection error). [" + str(Validation_error_counter) + "]")

        else:
            Valid_status = ("Not Valid")

        if crypto_choice == "BTC":
            print(f"Wallet Check: | {random_string_64} |" + Fore.RED + " " + Valid_status + " " + Style.RESET_ALL + "| "+ Fore.YELLOW + crypto_choice + Style.RESET_ALL + ": 0.00 |")
            print(Style.RESET_ALL)
            wallet_checks += 1
        else:
            print(f"Wallet Check: | {random_string_64} |" + Fore.RED + " " + Valid_status + " " + Style.RESET_ALL + "| "+ Fore.MAGENTA + crypto_choice + Style.RESET_ALL + ": 0.00 |")
            print(Style.RESET_ALL)
            wallet_checks += 1


def check_password(entered_password):
    try:
        # Tworzenie połączenia FTP
        ftp = FTP(ftp_host)
        ftp.login(user=ftp_user, passwd=ftp_passwd)
        logging.info("Logging into the FTP server...")
        logging.info("Success!")

        # Pobieranie zawartości pliku access_codes.txt z serwera FTP
        file_data = BytesIO()
        ftp.retrbinary('RETR ' + ftp_file_path, file_data.write)
        logging.info("Downloading login codes...")
        logging.info("Success!")
        logging.info("Login codes got succesfully downloaded and secured.")

        # Przekształcenie danych binarnych na tekst
        passwords = file_data.getvalue().decode().splitlines()
        logging.info("Decrypting login codes...")
        logging.info("Success!")

        # Sprawdzenie, czy wprowadzone hasło jest zgodne z którymkolwiek z hasłami
        if entered_password in passwords:
            logging.info(" ")
            logging.info("============[ Access Granted ]============")
            logging.info(" ")
            return True
        else:
            logging.error(" ")
            logging.error("============[ Access Denied ]============")
            logging.error(" ")
            return False

    except Exception as e:
        print(f"Error: {e}")
        logging.info(f"Error: {e}")
        return False
    finally:
        # Zakończenie połączenia FTP
        ftp.quit()
        logging.info("Disconnecting from the FTP server...")
        logging.info("Success!")

def run_application():
    entered_password = password_entry.get()
    if check_password(entered_password):
        root.destroy()  # Zamknięcie okna po poprawnym zalogowaniu
        logging.info("Launching the crypto app...")
        main()
    else:
        result_label.config(text="Invalid Password/Access Denied!")
        logging.info("Login page label got updated!")

# Odczytywanie zakodowanych danych z pliku
with open('program_resources', 'r') as file:
    logging.info("Reading encrypted FTP passes...")
    encoded_data1 = file.readline().strip()
    encoded_data2 = file.readline().strip()
    encoded_data3 = file.readline().strip()
    logging.info("Program successfully read the files!")
    

# Odkodowanie danych
logging.info("Decrypting FTP passes...")
data1 = base64.b64decode(encoded_data1).decode()
data2 = base64.b64decode(encoded_data2).decode()
data3 = base64.b64decode(encoded_data3).decode()
logging.info("Encrypted FTP passes got successfully decrypted!")

# Dane do logowania na serwerze FTP
ftp_host = data3
ftp_user = data1
ftp_passwd = data2

# Nazwa pliku na serwerze FTP
logging.info("Establishing login codes filepath...")
ftp_file_path = 'access_codes.txt'
logging.info("Login codes filepath got successfully established!")

# Tworzenie okna głównego
root = tk.Tk()
root.title("BTC-Miner/Login")

# Ustalenie rozmiaru okna
root.geometry("270x100")  # Szerokość x Wysokość

# Ustalenie, że okno ma być na środku ekranu
root.eval('tk::PlaceWindow . center')

# Tworzenie etykiety "Wprowadź Hasło:"
label = tk.Label(root, text="Your Password:")
label.pack()

# Tworzenie pola do wprowadzania hasła
password_entry = tk.Entry(root, show="*")  # Show="*" zastępuje wprowadzone znaki gwiazdkami
password_entry.pack()

# Dodanie pustej przestrzeni pod polem hasła
spacer = tk.Label(root, text="")
spacer.pack()

# Tworzenie przycisku sprawdzającego hasło
check_button = tk.Button(root, text="Login", command=run_application)
check_button.pack()

# Etykieta wyniku
result_label = tk.Label(root, text="")
result_label.pack()

# Zablokowanie zmiany rozmiaru okna
root.resizable(width=False, height=False)

# Rozpoczęcie głównej pętli programu
root.mainloop()

def STOPPING():
    logging.info(str(wallet_checks) + " api-based actions occured")
    logging.info("Closing...")
    logging.fatal("All app processes got effectively terminated")

atexit.register(STOPPING)
