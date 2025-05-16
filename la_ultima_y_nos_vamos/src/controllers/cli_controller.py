class CLIController:
    def __init__(self, poll_service, user_service, nft_service):
        self.poll_service = poll_service
        self.user_service = user_service
        self.nft_service = nft_service
        self.current_user = None  # Para autenticación
        self.session_token = None  # Guardar token de sesión

    def run(self):
        print("CLI de votaciones. Escribe 'ayuda' para ver comandos.")
        while True:
            cmd = input("> ").strip()
            if cmd == "salir":
                break
            elif cmd == "ayuda":
                print("Comandos: registro, login, crear_encuesta, listar_encuestas, cerrar_encuesta <id>, ver_resultados <id>, mis_tokens, transferir_token <token_id> <nuevo_owner>")
            elif cmd == "registro":
                username = input("Usuario: ").strip()
                password = input("Contraseña: ").strip()
                try:
                    self.user_service.register(username, password)
                    print("Usuario registrado exitosamente.")
                except ValueError as e:
                    print(f"Error: {e}")
            elif cmd == "login":
                username = input("Usuario: ").strip()
                password = input("Contraseña: ").strip()
                token = self.user_service.login(username, password)
                if token:
                    self.current_user = username
                    self.session_token = token
                    print(f"Bienvenido, {username}! Token de sesión: {token}")
                else:
                    print("Usuario o contraseña incorrectos.")
            elif cmd.startswith("crear_encuesta"):
                # Aquí deberías pedir datos y llamar a poll_service.crear_encuesta(...)
                print("Funcionalidad crear_encuesta no implementada (demo).")
            elif cmd == "listar_encuestas":
                encuestas = self.poll_service.encuesta_repo.listar_encuestas()
                for e in encuestas:
                    print(f"{e.id}: {e.pregunta} [{e.estado}]")
            elif cmd.startswith("cerrar_encuesta"):
                parts = cmd.split()
                if len(parts) == 2:
                    self.poll_service.cerrar_encuesta(parts[1])
                    print("Encuesta cerrada.")
            elif cmd.startswith("ver_resultados"):
                parts = cmd.split()
                if len(parts) == 2:
                    res = self.poll_service.get_partial_results(parts[1])
                    print(res)
            elif cmd == "mis_tokens":
                # Aquí deberías pedir el usuario actual y mostrar tokens
                print("Funcionalidad mis_tokens no implementada (demo).")
            elif cmd.startswith("transferir_token"):
                print("Funcionalidad transferir_token no implementada (demo).")
            else:
                print("Comando no reconocido.")
