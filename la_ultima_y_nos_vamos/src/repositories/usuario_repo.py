# Repositorio para usuarios (simulado en memoria)
class UsuarioRepository:
    def __init__(self):
        self.usuarios = {}  # username -> Usuario

    def guardar_usuario(self, usuario):
        self.usuarios[usuario.username] = usuario

    def obtener_usuario(self, username):
        return self.usuarios.get(username)
