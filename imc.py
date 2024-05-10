weight = float(input("Digite seu peso: "))

height = float(input("Digite sua altura: "))


imc = weight/(height * height)

if 1.67 > height <= 1.70 and 70 > weight >= 54:
    print(f"Sua massa corporal é {imc}")
    print ("Sua massa corporal é conciderada normal para o sua altura")

    


