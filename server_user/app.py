from ariadne import graphql_sync
from ariadne.constants import PLAYGROUND_HTML
from flask import Flask, jsonify, request

from server_user.schema.schema import SchemaCreator

from .settings import Config

schemaCreator = SchemaCreator()
schema = schemaCreator.getSchema()

app = Flask(__name__, instance_relative_config=True)
app.config.from_object(Config)


@app.route("/", methods=["GET"])
def graphql_playgroud():
    return PLAYGROUND_HTML, 200


@app.route("/", methods=["POST"])
def graphql_server():
    data = request.get_json()
    success, result = graphql_sync(schema, data, context_value=request, debug=app.debug)

    status_code = 200 if success else 400
    print(jsonify(result))
    return jsonify(result), status_code


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8300)
