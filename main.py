def clearTerminal():
    from os import system     # Utilisé pour appeler os.system('cls')
    system('cls')

def showOptions():
    print("1/ Encrypter avec code César")
    print("2/ Décrypter code César")
    print("3/ Encrypter à partir d'un fichier")
    print("4/ Décrypter à partir d'un fichier")
    print("5/ Décryption \"Brute Force\" en essayant tous les décalages")
    print("6/ Sortir")
    

def getUserInputOption():
    validEntries = ['1', '2', '3', '4', '5', '6']
    while True:
        userInput = input("Choisissez votre option [1-6]: ")
        if userInput in validEntries:
            return userInput
        print("Entrée invalide, veuillez réessayer")

def getUserText():
    return input("Texte à encrypter/décrypter: ")

def getUserNumber():
    while True:
        userNumber = input("Veuillez entrer le décalage: ")
        try:
            return int(userNumber)
        except ValueError:
            print("Entrée invalide, veuillez réessayer.")

def cesarEncryption(text, number):
    result = ''
    for char in text:
        if char.isalpha():
            shift = ord('A') if char.isupper() else ord('a')
            newChar = chr((ord(char) - shift + number) % 26 + shift)
        else:
            newChar = char
        result += newChar
    return result

def cesarDecryption(text, number):
    result = ''
    for char in text:
        if char.isalpha():
            shift = ord('A') if char.isupper() else ord('a')
            newChar = chr((ord(char) - shift - number) % 26 + shift)
        else:
            newChar = char
        result += newChar
    return result
  
def encryptFromFile():
    with open('to_encrypt.txt', 'r') as inputFile:
        fileText = inputFile.read()
    userNumber = getUserNumber()
    result = cesarEncryption(fileText, userNumber)
    with open('encrypt_result.txt', 'w') as outputFile:
        outputFile.write(result)
    print("Encryption terminée.")

def decryptFromFile():
    with open('to_decrypt.txt', 'r') as inputFile:
        fileText = inputFile.read()
    userNumber = getUserNumber()
    result = cesarDecryption(fileText, userNumber)
    with open('decrypt_result.txt', 'w') as outputFile:
        outputFile.write(result)
    print("Decryption terminée.")

def main():
    while True:
        showOptions()
        userInputOption = getUserInputOption()
        clearTerminal()

        if userInputOption == '1':
            print("1/ Encrypter avec code César")
            userText = getUserText()
            userNumber = getUserNumber()
            print(f"\nRésultat: {cesarEncryption(userText, userNumber)} \n")
        elif userInputOption == '2':
            print("2/ Décrypter code César")
            userText = getUserText()
            userNumber = getUserNumber()
            print(f"\nRésultat: {cesarDecryption(userText, userNumber)} \n")
        elif userInputOption == '3':
            print("3/ Encrypter à partir d'un fichier")
            encryptFromFile()
        elif userInputOption == '4':
            print("4/ Décrypter à partir d'un fichier")
            decryptFromFile()
        elif userInputOption == '5':
            print("5/ Décryption \"Brute Force\" en essayant tous les décalages")
            userText = getUserText()
            for i in range(1, 26):
                print(f"\n{i} : {cesarDecryption(userText, i)}\n")

        else:
            print("6/ Sortir")
            print("Au revoir.")
            break

if __name__ == "__main__":
    main()
