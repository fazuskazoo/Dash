from flask import Flask

app = Flask(__name__)

from dashboard.views import dashboard

app.register_blueprint(dashboard.bp)