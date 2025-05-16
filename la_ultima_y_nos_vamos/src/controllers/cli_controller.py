class CLIController:
    def __init__(self, poll_service, user_service, nft_service):
        self.poll_service = poll_service
        self.user_service = user_service
        self.nft_service = nft_service

    def run(self):
        print("CLI de votaciones. Escribe 'ayuda' para ver comandos.")
        while True:
            cmd = input("> ").strip()
            if cmd == "salir":
                break
            elif cmd == "ayuda":
                print("Comandos: crear_encuesta, listar_encuestas, cerrar_encuesta <id>, ver_resultados <id>, mis_tokens, transferir_token <token_id> <nuevo_owner>, crear_usuario, login")
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
            elif cmd.startswith("crear_usuario"):
                username = input("Username: ").strip()
                password = input("Password: ").strip()
                # Aquí deberías hashear el password antes de pasarlo al servicio
                import hashlib, os
                salt = os.urandom(16)
                password_hash = salt + hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
                if self.user_service.registrar(username, password_hash):
                    print("Usuario registrado correctamente.")
                else:
                    print("El usuario ya existe.")
            elif cmd.startswith("login"):
                username = input("Username: ").strip()
                password = input("Password: ").strip()
                import hashlib
                usuario = self.user_service.usuario_repo.obtener_usuario(username)
                if not usuario:
                    print("Usuario no encontrado.")
                    continue
                salt = usuario.password_hash[:16]
                password_hash = salt + hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
                token = self.user_service.login(username, password_hash)
                if token:
                    print(f"Login exitoso. Token de sesión: {token}")
                else:
                    print("Credenciales incorrectas.")
            else:
                print("Comando no reconocido.")
