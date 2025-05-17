alphabet = ["A", "B", "C", "Ç", "D", "E", "F", "G", "Ğ", "H", "I", "İ", "J", "K", "L", "M", "N", "O", "Ö", "P", "R", "S", "Ş", "T", "U", "Ü", "V", "Y", "Z"]


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


def caesar(text, shift, mode):
    result = ""
    text = text.upper()
    shiftInt = int(shift)
    arrayText = list(text)

    for harf in arrayText:
        if harf in alphabet:
            index = alphabet.index(harf)
            if mode == "encrypt":
                newIndex = (index + shiftInt) % len(alphabet)
                result += alphabet[newIndex]
            elif mode == "decrypt":
                newIndex = (index - shiftInt) % len(alphabet)
                result += alphabet[newIndex]
        else:
            result += harf
        
    return result

Banner()
while True:
    option = input("1-Şifreleme\n2-Çözümleme\n>>")

    if option == "1":
        text = input("Şifrelemek istediğiniz text'i yazınız : ")
        shift = input("Kaç harf kaydırılacak : ")
        encrypted = caesar(text, shift, mode="encrypt")
        print(f"Şifrelenmiş text : {encrypted}")

    elif option == "2":
        text = input("Çözümlemek istediğiniz text'i yazınız: ")
        shift = input("Kaç harf kaydırılacak : ")
        decrypted = caesar(text, shift, mode="decrypt")
        print(f"Çözümlenmiş text : {decrypted}")

    else:
        print("Geçersiz seçenek!!!")