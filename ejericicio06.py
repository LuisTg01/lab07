def reemplazo():
    frase="A todos nos gusta la cancion y al que no le gusta esta muerto"
    frase_a_cambiar="gusta"
    frase_nueva=frase.replace(frase_a_cambiar,"chevere")
    return frase_nueva

print(reemplazo())