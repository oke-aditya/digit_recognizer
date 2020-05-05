from waitress import serve
import web_app

serve(web_app.app, port=8000, threads=6)
