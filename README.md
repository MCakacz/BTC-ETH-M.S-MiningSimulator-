# Crypto-Wallet imitation Script

## Overview

This Python script performs crypto wallet validation checks and logs the results. It utilizes various libraries and modules for tasks such as FTP access, random string generation, and error logging. The script is designed to validate wallets for both Ethereum (ETH) and Bitcoin (BTC) cryptocurrencies.

## Dependencies

Make sure you have the following Python libraries and modules installed:

- `tkinter`: Used for creating a simple graphical user interface (GUI).
- `ftplib`: Provides FTP functionality for accessing a remote server.
- `io`: Used for handling binary data.
- `base64`: Required for decoding encoded data.
- `os`: Handles file and directory operations.
- `logging`: Logs important information and errors.
- `socket`: Provides access to low-level network functions.
- `datetime`: Used for timestamping log files.
- `random`: Generates random numbers and strings.
- `colorama`: Adds color to console output.
- `atexit`: Registers functions to be called when the script exits.

## Usage

1. Run the script by executing the Python file.

2. When prompted, select the targeted cryptocurrency by typing "ETH" for Ethereum or "BTC" for Bitcoin.

3. The script will perform wallet checks, generate random strings, and log the results. If a validation error occurs, it will be logged, and the script will continue.

4. To access the crypto app, enter a password when prompted. The password is stored securely on an FTP server.

## Configuration

Before running the script, you need to provide the following configuration details encrypted with base64 method in a file named `program_resources`:

- FTP server host
- FTP username
- FTP password

Ensure that the `access_codes.txt` file with login codes is available on the FTP server.

Below is the sample content of the access_codes.txt file, with each line corresponding to a different code. Each code, which constitutes the entire content of a SINGLE line in the file, will be considered valid.
```
FILE PATH: /access_codes.txt <--- this line cannot be included in the file unless you want it to be a access code 😂
password1
password2
password3
```

## Logging

- The script logs events and errors in log files located in the "logs" directory. Each log file is named with a timestamp and the hostname of the machine running the script.

- Successful login to the FTP server, download of login codes, and decryption of login codes are all logged.

## Exit Handling

- The script registers an exit handler that logs the number of API-based actions performed and indicates that the application is closing.

## License

This script is licensed under the [MIT](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwjh5ej0j7qBAxVQExAIHRIwDLQQFnoECBcQAQ&url=https%3A%2F%2Fpl.wikipedia.org%2Fwiki%2FLicencja_MIT&usg=AOvVaw23YLLI-Iwi0nDZ40uyvkLX&opi=89978449) License. See the [LICENSE](https://github.com/MCakacz/Januszyk/blob/main/LICENSE) file for more details.

**Note:** This [README](https://github.com/MCakacz/Januszyk/blob/main/README.md) provides a high-level overview of the script and its usage. Please refer to the script's comments and documentation for more detailed information about its functionality and implementation.

For any questions or issues, feel free to contact me.
---

**Clarification:** From [file](https://github.com/MCakacz/Januszyk/blob/main/main.py) src you can conclude that this file does not actually do any [crypto-related](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwiKiOm1lLqBAxXrIhAIHZ4_BfAQFnoECB0QAQ&url=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FCryptocurrency&usg=AOvVaw23s5u17TzWkCzDKm_bEVgx&opi=89978449)https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwiKiOm1lLqBAxXrIhAIHZ4_BfAQFnoECB0QAQ&url=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FCryptocurrency&usg=AOvVaw23s5u17TzWkCzDKm_bEVgx&opi=89978449 stuff, it was created only for presentational purposes.
