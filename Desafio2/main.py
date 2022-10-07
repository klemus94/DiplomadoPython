from pregunta import Pregunta
from datos import datos

banco_preguntas = []

for dato in datos:
    pregunta = Pregunta(dato['texto'],dato['respuesta'])
    banco_preguntas.append(pregunta)