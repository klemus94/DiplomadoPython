class VerificarPreguntas:

    def __init__(self, lista_preguntas):
        self.lista_preguntas = lista_preguntas
        self.numero_preguntas = 0


    def mostrar_pregunta(self):

        lista_respuestas = []
        for pregunta in self.lista_preguntas[1::2]:
            print(f'P{self.numero_preguntas}: {pregunta.texto}')