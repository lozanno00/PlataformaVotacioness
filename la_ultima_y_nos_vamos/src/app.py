import sys
import os

# Asegura que la raíz del proyecto esté en sys.path para los imports relativos
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

# --- INICIO: Conexión a MongoDB y Neo4j ---
from pymongo import MongoClient
from neo4j import GraphDatabase

# Firebase Admin SDK
import firebase_admin
from firebase_admin import credentials, firestore

def conectar_mongodb(uri="mongodb://localhost:27017/", db_name="votaciones"):
    try:
        mongo_client = MongoClient(uri)
        mongo_db = mongo_client[db_name]
        print("Conexión a MongoDB exitosa.")
        return mongo_client, mongo_db
    except Exception as e:
        print(f"Error conectando a MongoDB: {e}")
        sys.exit(1)

def conectar_neo4j(uri="bolt://localhost:7687", user="neo4j", password="neo4j"):
    try:
        neo4j_driver = GraphDatabase.driver(uri, auth=(user, password))
        # Probar conexión
        with neo4j_driver.session() as session:
            session.run("RETURN 1")
        print("Conexión a Neo4j exitosa.")
        return neo4j_driver
    except Exception as e:
        print(f"Error conectando a Neo4j: {e}")
        sys.exit(1)

def conectar_firebase(cred_path="firebase_key.json"):
    try:
        if not firebase_admin._apps:
            cred = credentials.Certificate(cred_path)
            firebase_admin.initialize_app(cred)
        db = firestore.client()
        print("Conexión a Firebase exitosa.")
        return db
    except Exception as e:
        print(f"Error conectando a Firebase: {e}")
        sys.exit(1)
# --- FIN: Conexión a MongoDB y Neo4j ---

try:
    from src.ui.gradio_app import crear_gradio_ui
except ImportError as e:
    print("Error importando 'crear_gradio_ui' desde 'src.ui.gradio_app':", e)
    print("Asegúrate de que la estructura de carpetas sea correcta y de ejecutar el script desde la raíz del proyecto.")
    sys.exit(1)

def main():
    # Inicialización de configuración (puerto, rutas, parámetros IA, estrategias)
    # config = cargar_configuracion()  # Simulado

    # Conexión a MongoDB y Neo4j
    mongo_client, mongo_db = conectar_mongodb()
    neo4j_driver = conectar_neo4j()
    firebase_db = conectar_firebase()  # <-- Añadido Firebase

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