from flask import Blueprint

from routes.root import root_blueprint

main_bp = Blueprint('main', __name__)

# Importe e registre outros Blueprints aqui
main_bp.register_blueprint(root_blueprint)