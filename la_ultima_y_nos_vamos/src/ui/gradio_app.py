import gradio as gr

def mostrar_encuestas(encuestas):
    if not encuestas:
        return "No hay encuestas activas."
    return "\n".join([f"{e.id}: {e.pregunta} [{e.estado}]" for e in encuestas])

def votar_formulario(poll_id, opcion):
    # Aquí deberías conectar con PollService.vote
    return f"Voto registrado para encuesta {poll_id} opción {opcion} (demo)."

def mostrar_tokens(tokens):
    if not tokens:
        return "No tienes tokens NFT."
    return "\n".join([f"{t.token_id}: {t.option} ({t.poll_id})" for t in tokens])

def transferir_token(token_id, nuevo_owner):
    # Aquí deberías conectar con NFTService.transferir_token
    return f"Token {token_id} transferido a {nuevo_owner} (demo)."

def crear_gradio_ui(poll_service=None, chatbot_service=None, nft_service=None, usuario_actual=None):

    def gradio_chatbot_responder(mensaje, historial=[]):
        if chatbot_service:
            respuesta = chatbot_service.responder(mensaje, username=usuario_actual)
        else:
            respuesta = f"Respuesta IA simulada a: {mensaje}"
        historial.append((mensaje, respuesta))
        return "", historial

    with gr.Blocks() as demo:
        gr.Markdown("# Plataforma de Votaciones Interactivas")

        with gr.Tab("Encuestas"):
            encuestas = [] if poll_service is None else poll_service.encuesta_repo.listar_encuestas()
            gr.Markdown("## Encuestas activas")
            gr.Textbox(value=mostrar_encuestas(encuestas), label="Listado de encuestas", interactive=False)
            gr.Textbox(label="ID de encuesta para votar")
            gr.Textbox(label="Opción")
            gr.Button("Votar").click(votar_formulario, inputs=["ID de encuesta para votar", "Opción"], outputs="text")

        with gr.Tab("Chatbot"):
            gr.ChatInterface(fn=gradio_chatbot_responder)

        with gr.Tab("Tokens NFT"):
            tokens = [] if nft_service is None or usuario_actual is None else nft_service.tokens_por_usuario(usuario_actual)
            gr.Markdown("## Mis tokens NFT")
            gr.Textbox(value=mostrar_tokens(tokens), label="Tokens", interactive=False)
            gr.Textbox(label="Token ID para transferir")
            gr.Textbox(label="Nuevo propietario")
            gr.Button("Transferir").click(transferir_token, inputs=["Token ID para transferir", "Nuevo propietario"], outputs="text")

    return demo
