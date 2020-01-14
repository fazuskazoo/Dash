from flask import Flask, render_template, Blueprint


bp = Blueprint('dashboard', __name__, url_prefix='/dashboard')


@bp.route('/tables')
def tables():
    return render_template("/dashboard/tables.html")


@bp.route('/treegrid')
def treegrid():
    return render_template("/dashboard/treegrid.html")