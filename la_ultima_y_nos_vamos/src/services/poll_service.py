import uuid
import time

class PollService:
    def __init__(self, encuesta_repo, voto_repo, nft_service, desempate_strategy=None):
        self.encuesta_repo = encuesta_repo
        self.voto_repo = voto_repo
        self.nft_service = nft_service
        self.desempate_strategy = desempate_strategy

    def create_poll(self, pregunta, opciones, duracion_segundos, tipo):
        poll_id = str(uuid.uuid4())
        encuesta = {
            "id": poll_id,
            "pregunta": pregunta,
            "opciones": opciones,
            "duracion": duracion_segundos,
            "tipo": tipo,
            "timestamp_inicio": int(time.time()),
            "estado": "activa"
        }
        self.encuesta_repo.guardar_encuesta(encuesta)
        return poll_id

    def _check_and_close_expired(self):
        now = int(time.time())
        for encuesta in self.encuesta_repo.listar_encuestas():
            if encuesta["estado"] == "activa" and now > encuesta["timestamp_inicio"] + encuesta["duracion"]:
                self.close_poll(encuesta["id"])

    def vote(self, poll_id, username, opcion):
        self._check_and_close_expired()
        encuesta = self.encuesta_repo.obtener_encuesta(poll_id)
        if not encuesta or encuesta["estado"] != "activa":
            raise ValueError("Encuesta no existe o no está activa.")
        if self.voto_repo.usuario_ya_voto(poll_id, username):
            raise ValueError("El usuario ya votó en esta encuesta.")
        # Para tipo multiple, opcion puede ser lista
        self.voto_repo.registrar_voto(poll_id, username, opcion)
        self.nft_service.mint_token(username, poll_id, opcion)

    def close_poll(self, poll_id):
        encuesta = self.encuesta_repo.obtener_encuesta(poll_id)
        if encuesta and encuesta["estado"] == "activa":
            encuesta["estado"] = "cerrada"
            self.encuesta_repo.actualizar_encuesta(encuesta)
            # Notificar observadores si existen
            # Almacenar resultado final
            # ... (puedes agregar lógica aquí)

    def get_partial_results(self, poll_id):
        self._check_and_close_expired()
        votos = self.voto_repo.obtener_votos(poll_id)
        encuesta = self.encuesta_repo.obtener_encuesta(poll_id)
        if not encuesta:
            return {}
        conteo = {}
        total = 0
        for v in votos:
            opts = v["opcion"] if isinstance(v["opcion"], list) else [v["opcion"]]
            for opt in opts:
                conteo[opt] = conteo.get(opt, 0) + 1
                total += 1
        resultados = {}
        for opt in encuesta["opciones"]:
            count = conteo.get(opt, 0)
            resultados[opt] = {
                "conteo": count,
                "porcentaje": (count / total * 100) if total else 0
            }
        return resultados

    def get_final_results(self, poll_id):
        encuesta = self.encuesta_repo.obtener_encuesta(poll_id)
        if not encuesta or encuesta["estado"] != "cerrada":
            raise ValueError("La encuesta no está cerrada.")
        resultados = self.get_partial_results(poll_id)
        # Desempate si es necesario
        max_votos = max((v["conteo"] for v in resultados.values()), default=0)
        ganadores = [opt for opt, v in resultados.items() if v["conteo"] == max_votos]
        if len(ganadores) > 1 and self.desempate_strategy:
            ganador = self.desempate_strategy.resolve(encuesta)
            resultados["ganador"] = ganador
        else:
            resultados["ganador"] = ganadores[0] if ganadores else None
        return resultados
