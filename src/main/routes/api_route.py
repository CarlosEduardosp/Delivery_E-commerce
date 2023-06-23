from flask import Blueprint, render_template

api_routes_bp = Blueprint("api_routes", __name__)


@api_routes_bp.route("/", methods=["GET"])
def teste():
    """rota teste"""

    return render_template("teste.html")
