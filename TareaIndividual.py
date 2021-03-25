#1)

def superficieRectangulo(base,altura):
    superficie = base * altura
    print(f"La superficie total es de : {superficie}")
    return superficie

#2)
def triangulo_rectangulo(base,altura):
    superficie = (base * altura) / 2
    print(f"La superficie total del triangulo rectangulo es: {superficie}")
    return superficie

#3)
def numeroPrimo(numero,b=2):
    if (b >= numero):
        print("Es un numero primo")
        return True
    elif numero % b !=0:
        return numeroPrimo (numero , b +1)
    else:
        print(f"No es primo {b} es divisor")
    return False

#4) 
def cantidad_de_repeticiones(letra,oracion):
    cantidad = oracion.count(letra)
    print(f"La cantidad de repeticiones de la letra {letra} es {cantidad}")


#5)
def capicua(palabra):
    rev = palabra[::-1]
    if(palabra == rev):
        print(f"La palabra {palabra} es capicua")
    else: 
        print("No lo es")

#6)
def leetSpeak(palabra):
    for i in palabra:
	    if i == ("a"):
		    palabra = palabra.replace("a","4")
	    elif i == "b":
		    palabra = palabra.replace("b","8")
	    elif i == "e":
		    spalabra = palabra.replace("e","3")
	    elif i == "l":
		    palabra = palabra.replace("l","1")
	    elif i == "o":
		    palabra = palabra.replace("o","0")
	    elif i == "s": 
		    palabra= palabra.replace("s","5")
	    elif i == "t":
		    palabra = palabra.replace("t","7")
    else: 
        pass
    print(palabra)











