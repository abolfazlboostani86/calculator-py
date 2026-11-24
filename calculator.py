def jam(a, b):
    return a + b

def tafrigh(a, b):
    return a - b

def zarb(a, b):
    return a * b

def taghsim(a, b):
    if b == 0:
        return "Taghsim bar sefr mamnoo ast!"
    return a / b

def tavan(a, b):
    return a ** b

def baghimande(a, b):
    if b == 0:
        return "Taghsim bar sefr mamnoo ast!"
    return a % b

while True:
    print("\nMashin Hesab Mohandesi")
    print("1. Jam")
    print("2. Tafrigh")
    print("3. Zarb")
    print("4. Taghsim")
    print("5. Tavan")
    print("6. Baghimande")
    print("0. Khorooj")

    op = input("Entekhab konid: ")

    if op == "0":
        print("Khoda negahdar!")
        break

    if op not in ["1", "2", "3", "4", "5", "6"]:
        print("Entekhab eshtebah ast!")
        continue

    a = float(input("Adad aval: "))
    b = float(input("Adad dovom: "))

    match op:
        case "1":
            result = jam(a, b)
        case "2":
            result = tafrigh(a, b)
        case "3":
            result = zarb(a, b)
        case "4":
            result = taghsim(a, b)
        case "5":
            result = tavan(a, b)
        case "6":
            result = baghimande(a, b)

    print("Natije mohasebe:")
    print(result)

    again = input("Mohasebe jadid? (y/n): ")

    if again == "n":
        print("Barname baste shod!")
        break
    elif again == "y":
        continue