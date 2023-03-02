from db import db
from models import StoreModel, ItemModel


class StoreService():
    @staticmethod
    def get_all_stores():
        return StoreModel.query.all()

    @staticmethod
    def create_store(store_data):
        store = StoreModel(**store_data)
        db.session.add(store)
        db.session.commit()

        return store

    @staticmethod
    def get_store_by_id(store_id):
        return StoreModel.query.get_or_404(store_id)

    @staticmethod
    def delete_store_by_id(store_id):
        store = StoreModel.query.get_or_404(store_id)
        items = ItemModel.query.filter_by(store_id=store_id).all()

        for item in items:
            db.session.delete(item)

        db.session.delete(store)
        db.session.commit()

        return store
