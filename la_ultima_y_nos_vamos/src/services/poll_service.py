# Servicio de negocio: PollService
class PollService:
    def __init__(self, encuesta_repo):
        self.encuesta_repo = encuesta_repo

    def crear_encuesta(self, encuesta):
        self.encuesta_repo.guardar_encuesta(encuesta)

    def votar(self, poll_id, username, opcion):
        encuesta = self.encuesta_repo.obtener_encuesta(poll_id)
        if encuesta and encuesta.estado == "activa" and username not in encuesta.votos:
            encuesta.votos[username] = opcion
            return True
        return False

    def cerrar_encuesta(self, poll_id):
        encuesta = self.encuesta_repo.obtener_encuesta(poll_id)
        if encuesta:
            encuesta.estado = "cerrada"
            encuesta.timestamp_cierre = "now"  # Simulación
            return True
        return False

    def get_partial_results(self, poll_id):
        encuesta = self.encuesta_repo.obtener_encuesta(poll_id)
        if not encuesta:
            return None
        conteo = {op: 0 for op in encuesta.opciones}
        for v in encuesta.votos.values():
            if isinstance(v, list):
                for op in v:
                    conteo[op] += 1
            else:
                conteo[v] += 1
        total = sum(conteo.values())
        porcentajes = {op: (conteo[op] / total * 100) if total > 0 else 0 for op in conteo}
        return {"conteo": conteo, "porcentajes": porcentajes}
