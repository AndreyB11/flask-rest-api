from marshmallow import Schema, fields


class PlainItemSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    price = fields.Float(required=True)
    brand = fields.Str()
    image = fields.Str()
    created_at = fields.Str(dump_only=True)


class PlainStoreSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    created_at = fields.Str(dump_only=True)


class ItemUpdateSchema(Schema):
    name = fields.Str()
    price = fields.Float()
    brand = fields.Str()
    image = fields.Str()


class ItemSchema(PlainItemSchema):
    store_id = fields.Int(required=False, load_only=True)
    store = fields.Nested(PlainStoreSchema(), dump_only=True)


class StoreSchema(PlainStoreSchema):
    items = fields.List(fields.Nested(PlainItemSchema()), dump_only=True)


class PlainAuthSchema(Schema):
    id = fields.Int(dump_only=True)
    email = fields.Str(required=True)
    password = fields.Str(required=True, load_only=True)


class UserLoginSchema(PlainAuthSchema):
    access_token = fields.Str(dump_only=True)


class UserRegisterSchema(PlainAuthSchema):
    username = fields.Str(required=True)
