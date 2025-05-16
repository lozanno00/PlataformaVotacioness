from transformers import pipeline, Conversation

# Servicio de negocio: ChatbotService
class ChatbotService:
    def __init__(self, poll_service=None):
        self.chatbot = pipeline("conversational", model="facebook/blenderbot-400M-distill")
        self.historial = {}  # opcional: historial por usuario
        self.poll_service = poll_service

    def responder(self, mensaje, username=None):
        # Palabras clave para lógica de encuestas
        keywords = [
            "quién va ganando", "quien va ganando", "cuánto falta", "cuanto falta",
            "resultado", "ganador", "votos", "encuesta"
        ]
        msg_lower = mensaje.lower()
        if any(k in msg_lower for k in keywords) and self.poll_service:
            # Ejemplo simple: mostrar resultados parciales de la última encuesta activa
            encuestas = self.poll_service.encuesta_repo.listar_encuestas()
            activas = [e for e in encuestas if e["estado"] == "activa"]
            if activas:
                poll = activas[-1]
                resultados = self.poll_service.get_partial_results(poll["id"])
                res_str = ", ".join([f"{opt}: {val['conteo']} votos ({val['porcentaje']:.1f}%)" for opt, val in resultados.items()])
                return f"Resultados actuales de '{poll['pregunta']}': {res_str}"
            else:
                return "No hay encuestas activas en este momento."
        # Conversación IA normal
        if username:
            if username not in self.historial:
                self.historial[username] = Conversation(mensaje)
            else:
                self.historial[username].add_user_input(mensaje)
            response = self.chatbot(self.historial[username])
            return str(response)
        else:
            conv = Conversation(mensaje)
            response = self.chatbot(conv)
            return str(response)
