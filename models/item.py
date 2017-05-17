# internal representation
from db import db

class ItemModel(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80)) #the username has to be 80 characters or less
    price = db.Column(db.Float(precison=2)) #2 points past decimal point

    #ForeignKey because the values correspond to a store that has its own id
    #a store cant be deleted if there are items in it
    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))
    #there is only one store that an item is related to
    store = db.relationship('StoreModel')

    def __init__(self, name, price, store_id):
        self.name = name
        self.price = price
        self.store_id = store_id

    def json(self):
        return {'name': self.name, 'price': self.price}

    @classmethod
    def find_by_name(cls,name):
        return cls.query.filter_by(name=name).first() # SELECT * FROM items WHERE name=name LIMIT 1

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
