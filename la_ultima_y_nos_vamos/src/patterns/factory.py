# Patrón Factory Method para Encuesta y TokenNFT

class EncuestaSimple:
    pass

class EncuestaMultiple:
    pass

class EncuestaPonderada:
    pass

class EncuestaFactory:
    @staticmethod
    def crear_encuesta(tipo, *args, **kwargs):
        if tipo == "simple":
            return EncuestaSimple(*args, **kwargs)
        elif tipo == "multiple":
            return EncuestaMultiple(*args, **kwargs)
        elif tipo == "ponderada":
            return EncuestaPonderada(*args, **kwargs)
        else:
            raise ValueError("Tipo de encuesta no soportado")

class TokenNFTStandard:
    pass

class TokenNFTLimitedEdition:
    pass

class TokenNFTFactory:
    @staticmethod
    def crear_token(tipo, *args, **kwargs):
        if tipo == "standard":
            return TokenNFTStandard(*args, **kwargs)
        elif tipo == "limited":
            return TokenNFTLimitedEdition(*args, **kwargs)
        else:
            raise ValueError("Tipo de token no soportado")
