from flask import Blueprint

from app.application.price.usecases import GetPriceByStateUseCase


price_blueprint = Blueprint("price", __name__, url_prefix="/price")


@price_blueprint.route("/<string:state>", methods=["GET"])
def get_price_average(state):
    use_case = GetPriceByStateUseCase(state)
    return {
        "average_price": use_case.get_average_state_price(state),
        "state": state,
    }, 200
