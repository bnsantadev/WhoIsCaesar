turkishAlphabet = ["A", "B", "C", "Ç", "D", "E", "F", "G", "Ğ", "H", "I", "İ", "J", "K", "L", "M", "N", "O", "Ö", "P", "R", "S", "Ş", "T", "U", "Ü", "V", "Y", "Z"]
englishAlphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

def Banner():
    ascii_art = """
██╗    ██╗██╗  ██╗ ██████╗ ██╗███████╗ ██████╗ █████╗ ███████╗███████╗ █████╗ ██████╗ 
██║    ██║██║  ██║██╔═══██╗██║██╔════╝██╔════╝██╔══██╗██╔════╝██╔════╝██╔══██╗██╔══██╗
██║ █╗ ██║███████║██║   ██║██║███████╗██║     ███████║█████╗  ███████╗███████║██████╔╝
██║███╗██║██╔══██║██║   ██║██║╚════██║██║     ██╔══██║██╔══╝  ╚════██║██╔══██║██╔══██╗
╚███╔███╔╝██║  ██║╚██████╔╝██║███████║╚██████╗██║  ██║███████╗███████║██║  ██║██║  ██║
 ╚══╝╚══╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝
 by santa
    """
    print(ascii_art)

def bruteforce(encryptedText, lang):
    if lang == "tr":
        alphabet = turkishAlphabet
    elif lang == "en":
        alphabet = englishAlphabet
    else:
        print("Geçersiz dil seçimi!")
        return

    for i in range(1, len(alphabet)):
        arrayText = list(encryptedText)
        result = ""
        for harf in arrayText:
            if harf.upper() in alphabet:
                index = alphabet.index(harf.upper())
                newIndex = (index - i) % len(alphabet)
                if harf.isupper():
                    result += alphabet[newIndex].upper()
                else:
                    result += alphabet[newIndex].lower()
            elif harf in numbers:
                numberIndex = numbers.index(harf)
                newNumberIndex = (numberIndex - i) % len(numbers)
                result += numbers[newNumberIndex]
            else:
                result += harf
        print(f"[{i}] >> {result}")
            

def caesar(text, shift, mode, language):
    result = ""
    shiftInt = int(shift)
    arrayText = list(text)

    for harf in arrayText:
        if language == "tr":
            if harf.upper() in turkishAlphabet:
                if harf == harf.upper():
                    index = turkishAlphabet.index(harf.upper())
                    if mode == "encrypt":
                        newIndex = (index + shiftInt) % len(turkishAlphabet)
                        result += turkishAlphabet[newIndex].upper()
                    elif mode == "decrypt":
                        newIndex = (index - shiftInt) % len(turkishAlphabet)
                        result += turkishAlphabet[newIndex].upper()
                elif harf == harf.lower():
                    index = turkishAlphabet.index(harf.upper())
                    if mode == "encrypt":
                        newIndex = (index + shiftInt) % len(turkishAlphabet)
                        result += turkishAlphabet[newIndex].lower()
                    elif mode == "decrypt":
                        newIndex = (index - shiftInt) % len(turkishAlphabet)
                        result += turkishAlphabet[newIndex].lower()
            elif harf in numbers:
                tempNumberIndex = numbers.index(harf)
                if mode == "encrypt":
                    newNumberIndex = (tempNumberIndex + shiftInt) % len(numbers)
                    result += numbers[newNumberIndex]
                elif mode == "decrypt":
                    newNumberIndex = (tempNumberIndex - shiftInt) % len(numbers)
                    result += numbers[newNumberIndex]
            else:
                result += harf
                
        elif language == "en":
            if harf.upper() in englishAlphabet:
                if harf == harf.upper():
                    index = englishAlphabet.index(harf.upper())
                    if mode == "encrypt":
                        newIndex = (index + shiftInt) % len(englishAlphabet)
                        result += englishAlphabet[newIndex].upper()
                    elif mode == "decrypt":
                        newIndex = (index - shiftInt) % len(englishAlphabet)
                        result += englishAlphabet[newIndex].upper()
                elif harf == harf.lower():
                    index = englishAlphabet.index(harf.upper())
                    if mode == "encrypt":
                        newIndex = (index + shiftInt) % len(englishAlphabet)
                        result += englishAlphabet[newIndex].lower()
                    elif mode == "decrypt":
                        newIndex = (index - shiftInt) % len(englishAlphabet)
                        result += englishAlphabet[newIndex].lower()
            
            elif harf in numbers:
                tempNumberIndex = numbers.index(harf)
                if mode == "encrypt":
                    newNumberIndex = (tempNumberIndex + shiftInt) % len(numbers)
                    result += numbers[newNumberIndex]
                elif mode == "decrypt":
                    newNumberIndex = (tempNumberIndex - shiftInt) % len(numbers)
                    result += numbers[newNumberIndex]
            
            else:
                result += harf
        else:
            print("Geçersiz seçenek!!!")

        
    return result

Banner()
while True:
    option = input("1-Şifreleme\n2-Çözümleme\n99-Çıkış\n>>")

    if option == "1":
        text = input(">>Şifrelemek istediğiniz text'i yazınız : ")
        language = input(">>Dil seçiniz (en, tr) : ")
        shift = input(">>Kaç harf kaydırılacak : ")
        encrypted = caesar(text, shift, mode="encrypt", language=language)
        print(f"[+] Şifrelenmiş text : {encrypted}")

    elif option == "2":
        text = input(">>Çözümlemek istediğiniz text'i yazınız : ")
        language = input(">>Dil seçiniz (en, tr) : ")
        mode = input("BruteForce mu yoksa normal modda mı çözümlemek istersiniz (bf, normal): ")
        if mode == "bf":
            bruteforce(text, language)
        elif mode == "normal":
            shift = input(">>Kaç harf kaydırılacak : ")
            decrypted = caesar(text, shift, mode="decrypt", language=language)
            print(f"[ + ] Çözümlenmiş text : {decrypted}")
        else:
            print(">>Geçersiz Seçenek!!")

    elif option == "99":
        exit()
    
    else:
        print("[ ! ] Geçersiz seçenek!!!")