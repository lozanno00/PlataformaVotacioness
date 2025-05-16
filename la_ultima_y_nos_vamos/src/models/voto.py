# Modelo de dominio: Voto (Vote)
class Voto:
    def __init__(self, username, opcion, poll_id):
        self.username = username
        self.opcion = opcion  # Puede ser str o list[str]
        self.poll_id = poll_id
