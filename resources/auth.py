from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from services import AuthService
from schemas import UserRegisterSchema, UserLoginSchema
from exceptions import InvalidUsage
from flask_jwt_extended import jwt_required, get_jwt


blp = Blueprint("auth", __name__, description="Operations on auth")


@blp.route("/auth/register")
class AuthRegister(MethodView):
    @blp.arguments(UserRegisterSchema)
    @blp.response(201, UserRegisterSchema)
    def post(self, user_data):
        try:
            return AuthService.register_user(user_data), 201
        except IntegrityError:
            abort(400, message="User already exists")
        except SQLAlchemyError:
            abort(500, message="Something went wrong")


@blp.route("/auth/login")
class AuthLogin(MethodView):
    @blp.arguments(UserLoginSchema)
    @blp.response(200, UserLoginSchema)
    def post(self, user_data):
        try:
            return AuthService.login_user_by_email(user_data), 200
        except InvalidUsage as err:
            abort(err.status_code, message=err.message)
        except SQLAlchemyError:
            abort(500, message="Something went wrong")


@blp.route("/auth/logout")
class AuthLogin(MethodView):
    @jwt_required()
    def put(self):
        try:
            AuthService.logout(get_jwt()["jti"])

            return {"message": "Logout successful"}, 200
        except InvalidUsage as err:
            abort(err.status_code, message=err.message)
        except SQLAlchemyError:
            abort(500, message="Something went wrong")
