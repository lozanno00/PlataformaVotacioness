import sys
import os

# Ruta absoluta al src y app.py
project_root = os.path.dirname(__file__)
src_dir = os.path.join(project_root, "la_ultima_y_nos_vamos", "src")
app_path = os.path.join(src_dir, "app.py")

if not os.path.exists(app_path):
    print(f"No se encontró app.py en {app_path}")
    sys.exit(1)

# Asegura que la raíz del proyecto esté en sys.path para imports tipo 'src.ui.gradio_app'
if project_root not in sys.path:
    sys.path.insert(0, project_root)

# Ejecuta app.py como script principal, definiendo __file__ en el contexto
sys.argv = [app_path] + sys.argv[1:]
with open(app_path, "rb") as f:
    code = compile(f.read(), app_path, 'exec')
    exec(code, {'__name__': '__main__', '__file__': app_path})
