from db import db
from models import ItemModel, StoreModel


class ItemService():
    @staticmethod
    def get_all_items():
        return ItemModel.query.all()

    @staticmethod
    def create_item(item_data):
        StoreModel.query.get_or_404(item_data["store_id"])

        item = ItemModel(**item_data)
        db.session.add(item)
        db.session.commit()

        return item

    @staticmethod
    def get_item_by_id(item_id):
        return ItemModel.query.get_or_404(item_id)

    @staticmethod
    def update_item_by_id(item_id, item_data):
        item = ItemModel.query.get_or_404(item_id)

        if "price" in item_data:
            item.price = item_data["price"]

        if "name" in item_data:
            item.name = item_data["name"]

        db.session.add(item)
        db.session.commit()

        return item

    @staticmethod
    def delete_item_by_id(item_id):
        item = ItemModel.query.get_or_404(item_id)
        db.session.delete(item)
        db.session.commit()
