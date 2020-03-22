from flask import Blueprint, current_app, jsonify
from flask_restful import Api
from marshmallow import ValidationError

from cultureondemand.extensions import apispec
from cultureondemand.api.resources import UserResource, UserList
from cultureondemand.api.resources.user import UserSchema
from cultureondemand.api.resources import OfferResource, OfferList
from cultureondemand.api.resources.offer import OfferSchema


blueprint = Blueprint("api", __name__, url_prefix="/api/v1")
api = Api(blueprint)


api.add_resource(UserResource, "/users/<int:user_id>")
api.add_resource(UserList, "/users")

api.add_resource(OfferResource, "/offer/<int:offer_id>")
api.add_resource(OfferList, "/offers")

@blueprint.before_app_first_request
def register_views():
    apispec.spec.components.schema("UserSchema", schema=UserSchema)
    apispec.spec.components.schema("OfferSchema", schema=OfferSchema)
    apispec.spec.path(view=UserResource, app=current_app)
    apispec.spec.path(view=UserList, app=current_app)
    apispec.spec.path(view=OfferResource, app=current_app)
    apispec.spec.path(view=OfferList, app=current_app)


@blueprint.errorhandler(ValidationError)
def handle_marshmallow_error(e):
    """Return json error for marshmallow validation errors.

    This will avoid having to try/catch ValidationErrors in all endpoints, returning
    correct JSON response with associated HTTP 400 Status (https://tools.ietf.org/html/rfc7231#section-6.5.1)
    """
    return jsonify(e.messages), 400
