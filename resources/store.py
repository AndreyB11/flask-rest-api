from flask.views import MethodView
from flask_smorest import Blueprint, abort
from schemas import StoreSchema
from services import StoreService
from sqlalchemy.exc import SQLAlchemyError, IntegrityError


blp = Blueprint("stores", __name__, description="Operations on stores")


@blp.route("/stores/<int:store_id>")
class Store(MethodView):
    @blp.response(200, StoreSchema)
    def get(self, store_id):
        try:
            return StoreService.get_store_by_id(store_id), 200
        except SQLAlchemyError:
            abort(500, message="Something went wrong")

    def delete(self, store_id):
        try:
            StoreService.delete_store_by_id(store_id)

            return {"message": "Store has been delete"}, 200
        except SQLAlchemyError:
            abort(500, message="Something went wrong")


@blp.route("/stores")
class StoreList(MethodView):
    @blp.response(200, StoreSchema(many=True))
    def get(self):
        try:
            return StoreService.get_all_stores(), 200
        except SQLAlchemyError:
            abort(500, message="Something went wrong")

    @blp.arguments(StoreSchema)
    @blp.response(201, StoreSchema)
    def post(self, store_data):
        try:
            return StoreService.create_store(store_data), 201
        except IntegrityError:
            abort(400, message="A store with that name already exists")
        except SQLAlchemyError:
            abort(500, message="Something went wrong")
