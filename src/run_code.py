from roman_converter import decimal_to_roman

resu = ''

while( resu != "salir"):
    inp = input("digite un numero y si quiere salir digite salir:\n")
    if inp == 'salir': 
        break
    try:
        resultado = decimal_to_roman(int(inp))
        print(f"resultado: {resultado}")
    except ValueError:
        print("Entrada inválida, se esperaba un número.")