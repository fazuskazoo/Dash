from flask import Flask, render_template

app = Flask(__name__)

from dashboard.views import dashboard
app.register_blueprint(dashboard.bp)

@app.route('/')
def index():
    return render_template("/dashboard/index.html")

@app.route('/all')
def all():
    return render_template("/dashboard/index_all.html")
