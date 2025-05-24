import sys
import os

# Asegura que la raíz del proyecto esté en sys.path para los imports relativos
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

try:
    from src.ui.gradio_app import crear_gradio_ui
except ImportError as e:
    print("Error importando 'crear_gradio_ui' desde 'src.ui.gradio_app':", e)
    print("Asegúrate de que la estructura de carpetas sea correcta y de ejecutar el script desde la raíz del proyecto.")
    sys.exit(1)

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