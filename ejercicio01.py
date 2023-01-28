def palindromo():
    
    nombre = input("Ingrese su nombre: ")
    nombre = nombre.replace(' ', '')
    if nombre == nombre[::-1]:
        print("Su nombre es palindromo")

    else:
        print("Su nombre no es palindromo")
 

palindromo()