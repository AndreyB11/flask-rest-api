from db import db
from models import UserModel
from passlib.hash import pbkdf2_sha256
from flask_jwt_extended import create_access_token
from exceptions import InvalidUsage
from blocklist import BLOCKLIST


class AuthService():
    @staticmethod
    def register_user(user_data):
        user_data["password"] = pbkdf2_sha256.hash(user_data["password"])

        new_user = UserModel(**user_data)
        db.session.add(new_user)
        db.session.commit()

        return new_user

    @staticmethod
    def login_user_by_email(user_data):
        user = UserModel.query.filter(
            UserModel.email == user_data["email"]).first()

        if user and pbkdf2_sha256.verify(user_data["password"], user.password):
            access_token = create_access_token(identity=user.id)

            return {**user.__dict__, "access_token": access_token}

        raise InvalidUsage("Email or password are not valid", 401)

    @staticmethod
    def logout(jti):
        BLOCKLIST.add(jti)
