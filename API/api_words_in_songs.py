from flask import Flask
from flask_restful import Api

from resources.Words_In_Songs import SearchWords

app = Flask(__name__)
api = Api(app)


api.add_resource(SearchWords, '/<artista>/<palavra>')

if __name__ == '__main__':
    app.run(debug=True)
