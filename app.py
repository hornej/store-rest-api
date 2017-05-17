from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
#when importing from a file, python actually runs the file first
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db' #i can change this to mySQL
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = 'josh'
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()

jwt = JWT(app, authenticate, identity) #/auth

api.add_resource(Store, '/store/<string:name>')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(StoreList, '/stores')

api.add_resource(UserRegister, '/register')

#this makes sure it isnt run when being imported
#only the file that is being run is called __main__
if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True) #this debug will help with debugging

#test-first API design is the way to go!
#using the right status codes is important
#JWT stands for JSON web token.
# the most common REST API is a CRUD (Create, Request, Update, Delete)
