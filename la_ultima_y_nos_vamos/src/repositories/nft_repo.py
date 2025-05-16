# Repositorio para tokens NFT (simulado en memoria)
class NFTRepository:
    def __init__(self):
        self.tokens = {}  # token_id -> TokenNFT

    def guardar_token(self, token):
        self.tokens[token.token_id] = token

    def obtener_token(self, token_id):
        return self.tokens.get(token_id)

    def listar_tokens_por_owner(self, owner):
        return [t for t in self.tokens.values() if t.owner == owner]
