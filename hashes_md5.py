from urllib.request import urlopen, hashlib
md5hash = input("Please input the MD5 hash to crack: \n")
LIST_OF_COMMON_PASSWORDS = str(urlopen("https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-10000.txt").read(), 'utf-8')
for guess in LIST_OF_COMMON_PASSWORDS.split('\n'):
    hashedGuess = hashlib.md5(bytes(guess, 'utf-8')).hexdigest()
    if hashedGuess == md5hash:
        print("The password is: ", str(guess))
        quit()
    elif hashedGuess != md5hash:
        print("Trying password: ", str(guess)," does not match, trying next...")
print("Password not in database, we'll get them next time!")