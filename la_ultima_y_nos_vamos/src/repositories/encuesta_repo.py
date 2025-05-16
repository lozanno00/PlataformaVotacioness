# Repositorio para encuestas y votos (simulado en memoria)
class EncuestaRepository:
    def __init__(self):
        self.encuestas = {}  # id -> Encuesta

    def guardar_encuesta(self, encuesta):
        self.encuestas[encuesta.id] = encuesta

    def obtener_encuesta(self, encuesta_id):
        return self.encuestas.get(encuesta_id)

    def listar_encuestas(self):
        return list(self.encuestas.values())
