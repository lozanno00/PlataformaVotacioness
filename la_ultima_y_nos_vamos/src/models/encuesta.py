# Modelo de dominio: Encuesta (Poll)
class Encuesta:
    def __init__(self, id, pregunta, opciones, duracion_segundos, tipo):
        self.id = id
        self.pregunta = pregunta
        self.opciones = opciones  # Lista de strings
        self.votos = {}  # username -> opcion (o lista de opciones)
        self.estado = "activa"
        self.timestamp_inicio = None
        self.duracion_segundos = duracion_segundos
        self.tipo = tipo  # "simple" o "multiple"
        self.timestamp_cierre = None
