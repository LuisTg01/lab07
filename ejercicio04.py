def frecuencia():
    dicionary={}
    frase="El programa que esta dentro de un programa es otro programa"
    contador=0
    for i in frase.split():
        if i == i:
            dicionary.update({i:len(i)})
    return dicionary

print(frecuencia())
