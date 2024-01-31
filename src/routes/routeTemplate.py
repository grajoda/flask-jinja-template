from flask import * 

# import functionalities in /controllers directory
import controller.dataController as dataController

route_blueprint = Blueprint('routeName', __name__)

@route_blueprint.route("/nameRoute", methods=['GET'])
def ControllerFunction():
    # route code logic
    dataController.manipulateData()

    return render_template('pages/introPage.html')