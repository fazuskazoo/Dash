from flask import Flask, render_template, Blueprint


bp = Blueprint('dashboard', __name__, url_prefix='/')

@bp.route('/')
def index():
    return render_template("/dashboard/index2.html")

@bp.route('/hello')
def hello():
    return render_template("/dashboard/tables.html")