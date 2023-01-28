def cadenaLarga():
    t=input("frase:").split()

    for i in t:
	    b = max(t, key=len)
    return b

print(cadenaLarga())
print()