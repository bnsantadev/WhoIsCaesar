turkishAlphabet = ["A", "B", "C", "Ç", "D", "E", "F", "G", "Ğ", "H", "I", "İ", "J", "K", "L", "M", "N", "O", "Ö", "P", "R", "S", "Ş", "T", "U", "Ü", "V", "Y", "Z"]
englishAlphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

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
            else:
                result += harf
        else:
            print("Geçersiz seçenek!!!")

        
    return result

Banner()
while True:
    option = input("1-Şifreleme\n2-Çözümleme\n>>")

    if option == "1":
        text = input(">>Şifrelemek istediğiniz text'i yazınız : ")
        shift = input(">>Kaç harf kaydırılacak : ")
        language = input(">>Dil seçiniz (en, tr) : ")
        encrypted = caesar(text, shift, mode="encrypt", language=language)
        print(f"Şifrelenmiş text : {encrypted}")

    elif option == "2":
        text = input("Çözümlemek istediğiniz text'i yazınız: ")
        shift = input("Kaç harf kaydırılacak : ")
        language = input(">>Dil seçiniz (en, tr) : ")
        decrypted = caesar(text, shift, mode="decrypt", language=language)
        print(f"Çözümlenmiş text : {decrypted}")

    else:
        print("Geçersiz seçenek!!!")