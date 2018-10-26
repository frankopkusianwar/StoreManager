from flask import Flask
from app.views import productsView

app = Flask(__name__, instance_relative_config=True)
app.register_blueprint(productsView.bp)