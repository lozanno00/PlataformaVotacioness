# Patrón Strategy para desempate y presentación de resultados

import random

class DesempateStrategy:
    def resolver(self, opciones_empate):
        pass

class DesempateAlfabetico(DesempateStrategy):
    def resolver(self, opciones_empate):
        return sorted(opciones_empate)[0]

class DesempateAleatorio(DesempateStrategy):
    def resolver(self, opciones_empate):
        return random.choice(opciones_empate)

class DesempateProrroga(DesempateStrategy):
    def resolver(self, opciones_empate):
        return "prorroga"

class PresentacionResultadosStrategy:
    def presentar(self, resultados):
        pass

class PresentacionTexto(PresentacionResultadosStrategy):
    def presentar(self, resultados):
        return str(resultados)

class PresentacionASCII(PresentacionResultadosStrategy):
    def presentar(self, resultados):
        # Simulación simple
        return "\n".join(f"{op}: {'#'*int(p)}" for op, p in resultados["conteo"].items())

class PresentacionJSON(PresentacionResultadosStrategy):
    def presentar(self, resultados):
        import json
        return json.dumps(resultados, indent=2)
