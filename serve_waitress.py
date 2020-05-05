from waitress import serve
import app

serve(app.app, port=8000, threads=6)
