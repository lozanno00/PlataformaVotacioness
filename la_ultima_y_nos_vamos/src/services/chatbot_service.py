# Servicio de negocio: ChatbotService
class ChatbotService:
    def __init__(self, poll_service):
        self.poll_service = poll_service
        # Aquí se podría inicializar el pipeline de transformers

    def responder(self, pregunta, username=None):
        # Lógica básica: si la pregunta es sobre encuestas, responde con datos de PollService
        # Si no, delega a un modelo IA (simulado aquí)
        if "quién va ganando" in pregunta.lower():
            # Simulación: retorna string fijo
            return "Consulta de resultados en curso..."
        return "Respuesta IA simulada."
