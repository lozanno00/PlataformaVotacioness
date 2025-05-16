import uuid
from datetime import datetime

# Clase TokenNFT
class TokenNFT:
    def __init__(self, owner, poll_id, option, issued_at=None, token_id=None):
        self.token_id = token_id or str(uuid.uuid4())
        self.owner = owner
        self.poll_id = poll_id
        self.option = option
        self.issued_at = issued_at or datetime.utcnow().isoformat()

    def to_dict(self):
        return {
            "token_id": self.token_id,
            "owner": self.owner,
            "poll_id": self.poll_id,
            "option": self.option,
            "issued_at": self.issued_at
        }

# Servicio de negocio: NFTService
class NFTService:
    def __init__(self, nft_repo):
        self.nft_repo = nft_repo

    def mint_token(self, owner, poll_id, option):
        token = TokenNFT(owner, poll_id, option)
        self.nft_repo.guardar_token(token)
        return token

    def transferir_token(self, token_id, nuevo_owner, usuario_actual):
        token = self.nft_repo.obtener_token(token_id)
        if not token:
            raise ValueError("Token no encontrado.")
        if token.owner != usuario_actual:
            raise ValueError("No eres el propietario de este token.")
        token.owner = nuevo_owner
        self.nft_repo.actualizar_token(token)

    def tokens_por_usuario(self, username):
        return self.nft_repo.tokens_por_usuario(username)
