# importing all the libraries

from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
from flask_graphql import GraphQLView
from database import db_session, init_db
from schema import schema

app = Flask(__name__)



#creating a TABLE in the database
mysql = MySQL(app)



app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True # for having the GraphiQL interface
    )
)

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

if __name__ == '__main__':
    init_db()
    app.run(debug=True)