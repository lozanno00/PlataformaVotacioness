import sys
from src.ui.gradio_app import crear_gradio_ui

def main():
    # Inicialización de configuración (puerto, rutas, parámetros IA, estrategias)
    # config = cargar_configuracion()  # Simulado

    # Aquí se inicializarían los servicios y controladores reales
    # poll_service = PollService(...)
    # user_service = UserService(...)
    # nft_service = NFTService(...)
    # chatbot_service = ChatbotService(...)

    if "--ui" in sys.argv:
        print("Iniciando interfaz visual con Gradio...")
        demo = crear_gradio_ui()  # Puedes pasar servicios reales si los tienes
        demo.launch()
    else:
        print("Iniciando CLI...")
        # cli = CLIController(poll_service, user_service, nft_service)
        # cli.run()
        print("CLI no implementada en este demo.")

if __name__ == "__main__":
    main()