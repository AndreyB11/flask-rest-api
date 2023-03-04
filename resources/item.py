from flask.views import MethodView
from flask_smorest import Blueprint, abort
from schemas import ItemSchema, ItemUpdateSchema
from sqlalchemy.exc import SQLAlchemyError
from services import ItemService
from flask_jwt_extended import jwt_required

blp = Blueprint("items", __name__, description="Operations on items")


@blp.route("/items/<int:item_id>")
class Item(MethodView):
    # @jwt_required()
    @blp.response(200, ItemSchema)
    def get(self, item_id):
        try:
            return ItemService.get_item_by_id(item_id), 200
        except SQLAlchemyError:
            abort(500, message="Something went wrong")

    # @jwt_required()
    def delete(self, item_id):
        try:
            ItemService.delete_item_by_id(item_id)

            return {"message": "Item has been deleted"}, 200
        except SQLAlchemyError:
            abort(500, message="Something went wrong")

    # @jwt_required()
    @blp.arguments(ItemUpdateSchema)
    @blp.response(200, ItemSchema)
    def put(self, item_data, item_id):
        try:
            return ItemService.update_item_by_id(item_id, item_data), 200
        except SQLAlchemyError:
            abort(500, message="Something went wrong")


@blp.route("/items")
class ItemList(MethodView):
    # @jwt_required()
    @blp.response(200, ItemSchema(many=True))
    def get(self):
        try:
            return ItemService.get_all_items(), 200
        except SQLAlchemyError:
            abort(500, message="Something went wrong")

    # @jwt_required()
    @blp.arguments(ItemSchema)
    @blp.response(201, ItemSchema)
    def post(self, item_data):
        try:
            return ItemService.create_item(item_data), 201
        except SQLAlchemyError:
            abort(500, message="Something went wrong")
