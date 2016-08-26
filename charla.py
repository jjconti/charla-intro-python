import decimal
import fractions

slide1 = "Agradecimiento"
slide2 = "Presentación"
slide3 = "Encuentas"
slide4 = "Introducción general"
slide5 = "Tipos de datos"
slide6 = "Estructuras de control"
slide7 = "Funciones"
slide8 = "Decoradores"
slide9 = "Fin"

lenguajes = []

def encuesta(total):
    programadores = input("¿Cuántos son programadores? ")
    conocen_python = input("¿Cuántos usaron alguna vez Python? ")
    usan_python = input("¿Cuántos usan Python con regularidad? ")
    
    while len(lenguajes) < 5:
        otro = input("¿Qué otros lenguajes usan? ")
        lenguajes.append(otro)

    def porcentaje(n):
        return int(n) / total * 100
    
    print("\n\n")
    print("El {}% son programadores".format(porcentaje(programadores)))
    print("El {}% conoce Python".format(porcentaje(conocen_python)))
    print("El {}% usa Python".format(porcentaje(usan_python)))

dec = decimal.Decimal('0.1')
frac = fractions.Fraction(2, 3)

slides = {slide1: [], slide2: "libros", slide3: encuesta, slide4: [],
          slide5: [1j, dec, frac, list(), tuple(), set()],
          slide6: ["for", "while", "mas listas"], slide7: "args y kwargs",
          slide8: "decoradoes", slide9: "Muchas gracias!"}
