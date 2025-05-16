# Modelo de dominio: Usuario (User)
class Usuario:
    def __init__(self, username, password_hash):
        self.username = username
        self.password_hash = password_hash
        self.tokens = []  # Lista de TokenNFT o ids de tokens
