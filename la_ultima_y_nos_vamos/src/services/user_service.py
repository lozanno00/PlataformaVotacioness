import hashlib
import uuid

# Servicio de negocio: UserService
class UserService:
    def __init__(self, usuario_repo):
        self.usuario_repo = usuario_repo
        self.active_sessions = {}

    def registrar(self, usuario):
        if self.usuario_repo.obtener_usuario(usuario.username):
            return False
        self.usuario_repo.guardar_usuario(usuario)
        return True

    def login(self, username, password):
        usuario = self.usuario_repo.obtener_usuario(username)
        if not usuario:
            return None
        hash_ = hashlib.pbkdf2_hmac(
            'sha256',
            password.encode(),
            usuario.salt,
            100000
        )
        if hash_ == usuario.password_hash:
            token = str(uuid.uuid4())
            self.active_sessions[token] = username
            return token
        return None
