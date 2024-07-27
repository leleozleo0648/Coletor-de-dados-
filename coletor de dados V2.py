def get_valid_age(): # def criada para validar se o campo idade contém apenas números
    while True:
        age = input("Insira sua idade: ")
        if age.isdigit():
            return int(age)
        else:
            print("O Campo idade deve ser preenchido apenas com números.")

name = input("Insira seu nome: ").strip()
city = input("Insira sua cidade: ").strip()
age = get_valid_age()

print(f"\nOlá {name}, você tem {age} anos e mora em {city}.")