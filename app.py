import os
import redis
from rq import Queue
from flask import Flask, jsonify
from flask_smorest import Api
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from dotenv import load_dotenv

from db import db
from blocklist import BLOCKLIST
import models

from resources import ItemBlueprint, StoreBlueprint, AuthBlueprint


def configure_jwt(jwt: JWTManager):
    @jwt.token_in_blocklist_loader
    def check_token_in_blocklist(jwt_header, jwt_payload):
        return jwt_payload["jti"] in BLOCKLIST

    @jwt.revoked_token_loader
    def revoked_token_cb(jwt_header, jwt_payload):
        return (
            jsonify({"message": "Signature verification failed",
                    "error": "invalid_token"}),
            401
        )

    @jwt.expired_token_loader
    def expired_token_cb(jwt_header, jwt_payload):
        return (
            jsonify({"message": "The token has expired",
                    "error": "token_expired"}),
            401
        )

    @jwt.invalid_token_loader
    def invalid_token_cb(err):
        return (
            jsonify({"message": "Signature verification failed",
                    "error": "invalid_token"}),
            401
        )

    @jwt.unauthorized_loader
    def missing_token_cb(err):
        return (
            jsonify({"message": "Request does not contain an access token",
                    "error": "authorization_required"}),
            401
        )


def create_app(db_url=None, jwt_secret=None):
    app = Flask(__name__)
    load_dotenv()

    connection = redis.from_url(os.getenv("REDIS_URL"))

    app.queue = Queue("emails", connection=connection)

    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "Stores REST API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url or os.getenv(
        "DATABASE_URL", "sqlite:///data.db")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["JWT_SECRET_KEY"] = jwt_secret or os.getenv(
        "JWT_SECRET", "a1s2d3")

    db.init_app(app)
    Migrate(app, db)

    api = Api(app)

    jwt = JWTManager(app)
    configure_jwt(jwt)

    with app.app_context():
        db.create_all()

    api.register_blueprint(ItemBlueprint)
    api.register_blueprint(StoreBlueprint)
    api.register_blueprint(AuthBlueprint)

    return app
