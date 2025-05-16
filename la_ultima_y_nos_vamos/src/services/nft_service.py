# Servicio de negocio: NFTService
class NFTService:
    def __init__(self, nft_repo):
        self.nft_repo = nft_repo

    def mint_token(self, token):
        self.nft_repo.guardar_token(token)

    def transferir_token(self, token_id, nuevo_owner):
        token = self.nft_repo.obtener_token(token_id)
        if token:
            token.owner = nuevo_owner
            self.nft_repo.guardar_token(token)
            return True
        return False

    def tokens_por_usuario(self, owner):
        return self.nft_repo.listar_tokens_por_owner(owner)
