def celsius_para_fahrenheit(c):
    return c * 9 / 5 + 32

def fahrenheit_para_celsius(f):
    return (f - 32) * 5 / 9

def celsius_para_kelvin(c):
    return c + 273.15

def main():
    print("Conversor de Temperaturas")
    print("1. Celsius para Fahrenheit")
    print("2. Fahrenheit para Celsius")
    print("3. Celsius para Kelvin")
    try:
        opcao = int(input("Escolha uma opção: "))
        if opcao == 1:
            c = float(input("Digite a temperatura em Celsius: "))
            print(f"Temperatura em Fahrenheit: {celsius_para_fahrenheit(c):.2f}")
        elif opcao == 2:
            f = float(input("Digite a temperatura em Fahrenheit: "))
            print(f"Temperatura em Celsius: {fahrenheit_para_celsius(f):.2f}")
        elif opcao == 3:
            c = float(input("Digite a temperatura em Celsius: "))
            print(f"Temperatura em Kelvin: {celsius_para_kelvin(c):.2f}")
        else:
            print("Opção inválida.")
    except ValueError:
        print("Por favor, insira um número válido.")

if __name__ == "__main__":
    main()
