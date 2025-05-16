# Servicio de negocio: UserService
class UserService:
    def __init__(self, usuario_repo):
        self.usuario_repo = usuario_repo

    def registrar(self, usuario):
        if self.usuario_repo.obtener_usuario(usuario.username):
            return False
        self.usuario_repo.guardar_usuario(usuario)
        return True

    def login(self, username, password_hash):
        usuario = self.usuario_repo.obtener_usuario(username)
        if usuario and usuario.password_hash == password_hash:
            return True
        return False
