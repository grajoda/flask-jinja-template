from flask import * 

root_blueprint = Blueprint('root', __name__)

@root_blueprint.route("/", methods=['GET'])
def root():
    return render_template('pages/introPage.html')