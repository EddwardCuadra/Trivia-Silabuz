import random
import time
#Codigos de color
NEGRO = '\033[30m'
ROJO = '\033[31m'
VERDE = '\033[32m'
AMARILLO = '\033[33m'
AZUL = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
BLANCO = '\033[37m'
NEGRITA = '\033[1m'
NFIN = '\033[0m'
RESET = '\033[39m'
# Fin Codigos de Color
print(NEGRITA + CYAN + "Bienvenido a mi trivia\n".upper() + NFIN)
nombre = input("Por favor dinos tu nombre:").capitalize()
print(CYAN + "\nHola", nombre,
      "espero disfrutes de jugar esta trivia.\n" + RESET)
print(
    CYAN +
    "En este apartado podrás ver algunas preguntas a las cuales tu tendras que responder cual crees que es la respuesta correcta.\n\nPor cada respuesta Correcta se te sumaran puntos y en las respuestas incorrectas se te restaran puntos. La cantidad de puntos ganados o perdidos sera aleatoria para cada pregunta:\nPor cada respuesta correcta recibiras de 5 a 15 puntos\nPor cada respuesta incorrecta perderas de 1 a 10 puntos.\n\nSi eres un poco creativo puede que te encuentres alguna sorpresa durante las preguntas.\n"
    + RESET)
#Variables y listas
puntuacion = 0
palabra = ["ayuda", "mosca", "gane"]


#Funciones
#Funcion para preguntas
def pregunta(
    enunciado, op1, op2, op3, op4
):  #el enunciado es la pregunta a realizar y op son las opciones de la pregunta
    time.sleep(1)
    enunciado = enunciado.upper()
    op1 = op1.capitalize()
    op2 = op2.capitalize()
    op3 = op3.capitalize()
    op4 = op4.capitalize()
    print("\n" + enunciado)
    print(MAGENTA + "\na)", op1, "\nb)", op2, "\nc)", op3, "\nd)", op4 + RESET)


#Funcion para respuesta secreta
def comodin():
    aleatorio = random.choice(palabra)
    return aleatorio


#Funcion para limitar input
def comprobar(respuesta):
    while respuesta not in ("a", "b", "c", "d", "A", "B", "C", "D", "ayuda",
                            "mosca", "gane"):
        respuesta = input(
            "Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
    return respuesta.lower()


#Funcion para evaluar respuesta correcta
def evaluar(respuesta, mal1, mal2, mal3, comodin,
            correcto):  #mal1,mal2,mal3 indican las respuestas incorrectas
    if respuesta == mal1:
        puntos = random.randint(1, 10)
        print("\nPerdiste", puntos, "puntos")
        puntos = puntuacion - puntos
        print(ROJO + "\nIncorrecto!", nombre,
              " Debes estudiar más sobre los animales\n" + RESET,
              "\nTu puntuacion es de", puntos, "puntos\n")
        return puntos
    elif respuesta == mal2:
        puntos = random.randint(1, 10)
        print("\nPerdiste", puntos, "puntos")
        puntos = puntuacion - puntos
        print(ROJO + "\nIncorrecto!", nombre,
              "Sigue intentando te falta pocas alternativas\n" + RESET,
              "\nTu puntuacion es de", puntos, "puntos\n")
        return puntos
    elif respuesta == mal3:
        puntos = random.randint(1, 10)
        print("\nPerdiste", puntos, "puntos")
        puntos = puntuacion - puntos
        print(ROJO + "\nIncorrecto!", nombre,
              "Te pasaste de alternativa\n" + RESET, "\nTu puntuacion es de",
              puntos, "puntos\n")
        return puntos
    elif respuesta == comodin:
        print(
            AMARILLO +
            "\nEsta es una respuesta secreta, automaticamente te dare un puntuacion aleatorio entre 20 y 100, cruza los dedos"
            + RESET)
        puntos = random.randint(20, 101)
        print("\nGanaste", puntos, "puntos")
        puntos = puntuacion + puntos
        print(AZUL + "\nTu puntuacion es de", puntos, "puntos\n" + RESET)
        return puntos
    elif respuesta == correcto:  #Esta sera la respuesta correcta
        puntos = random.randint(5, 15)
        print("\nGnaste", puntos, "puntos")
        puntos = puntuacion + puntos
        print(VERDE + "\nMuy bien", nombre, "!\n" + RESET, "\n",
              AZUL + "\nTu puntuacion es de", puntos, "puntos\n" + RESET)
        return puntos
    else:
        print(
            AMARILLO +
            "\nParece que has encontrado una de las palabras comodin... sin embargo no funciona en esta pregunta, quizas funcione en otra."
            + RESET)
        puntos = puntuacion
        print(AZUL + "\nTu puntuacion es de", puntos,
              "puntos\nNO HAS GANADO PUNTOS EXTRA\n" + RESET)
        return puntos


#Fin de funciones

iniciartrivia = True
Intento = 0
while iniciartrivia == True:
    Intento += 1
    print("\nIntento numero:", Intento)
    puntuacion = random.randint(0, 11)
    print(AZUL + "\nTienes", puntuacion, "puntos\n" + RESET)
    print(CYAN + "Mucha suerte y que empieze la trivia:\n" + RESET)
    for cuenta in range(0, 6, +1):
        print(cuenta)
        time.sleep(0.2)
    #PREGUNTA1
    pregunta(
        "1 Como se le llaman a los animales que caminan sobre sus 4 patas",
        "bipedo", "octupedo", "Cuadrupedo", "Ninguna de las anteriores")
    respC = input("\nTu respuesta:")
    puntuacion = evaluar(comprobar(respC), 'a', 'b', 'd', comodin(), 'c')

    #PREGUNTA2
    pregunta("2 Como se le llaman a los animales que caminan sobre dos patas",
             "Voladores", "Tripode", "Cuadrupedo", "Bipedo")
    respC = input("\nTu respuesta:")
    puntuacion = evaluar(comprobar(respC), 'a', 'b', 'c', comodin(), 'd')

    #PREGUNTA3
    pregunta("3 Cuantas extremidades tiene el ser humano", "3", "4", "5", "1")
    respC = input("\nTu respuesta:")
    puntuacion = evaluar(comprobar(respC), 'a', 'c', 'd', comodin(), 'b')

    #PREGUNTA 4
    pregunta("4 Quien fue el primer humano descubierto", "Homo habilis",
             "Australopithecus", "Homo sapien", "Homo sapien sapien")
    respC = input("\nTu Respuesta:").lower()

    while respC not in ("a", "b", "c", "d", "A", "B", "C", "D"):
        respC = input(
            "Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: "
        ).lower()
    if respC == "a":
        print(VERDE + "\nMuy bien" + RESET)
        puntuacion = puntuacion * 2
    elif respC == "b":
        print("\nCerca pero no tan cerca, A ESTUDIAR")
        puntuacion = puntuacion / 2
    elif respC == "c":
        print("\nBien pensado pero aun no es la respuesta correcta")
        puntuacion = puntuacion - 2
    else:
        print("\nMUy bien pensado pero quizas demasiado bien pensado")
        puntuacion = puntuacion + 2
    print("\nGracias", nombre, "Tu puntuacion en esta Trivia es de",
          puntuacion, "puntos")
    print("\nDeseas continuar la trivia nuevamente?")
    repetirtrivia = input(
        "Responder con un si, si deseas repetir la trivia, o cualquier tecla si deseas terminarla:"
    ).lower()
    if repetirtrivia == "si":
        print("\nGENIAL! Intentemoslo otra vez", nombre)
        iniciartrivia = True
    else:
        print("\nEspero te haya gustado mi Trivia", nombre, "Vuelve pronto")
        iniciartrivia = False
