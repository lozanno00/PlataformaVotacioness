# Modelo de dominio: TokenNFT
class TokenNFT:
    def __init__(self, token_id, owner, poll_id, option, issued_at):
        self.token_id = token_id
        self.owner = owner
        self.poll_id = poll_id
        self.option = option
        self.issued_at = issued_at
