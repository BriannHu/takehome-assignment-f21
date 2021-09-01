from typing import Tuple

from flask import Flask, jsonify, request, Response
import mockdb.mockdb_interface as db

app = Flask(__name__)


def create_response(
    data: dict = None, status: int = 200, message: str = ""
) -> Tuple[Response, int]:
    """Wraps response in a consistent format throughout the API.
    
    Format inspired by https://medium.com/@shazow/how-i-design-json-api-responses-71900f00f2db
    Modifications included:
    - make success a boolean since there's only 2 values
    - make message a single string since we will only use one message per response
    IMPORTANT: data must be a dictionary where:
    - the key is the name of the type of data
    - the value is the data itself

    :param data <str> optional data
    :param status <int> optional status code, defaults to 200
    :param message <str> optional message
    :returns tuple of Flask Response and int, which is what flask expects for a response
    """
    if type(data) is not dict and data is not None:
        raise TypeError("Data should be a dictionary 😞")

    response = {
        "code": status,
        "success": 200 <= status < 300,
        "message": message,
        "result": data,
    }
    return jsonify(response), status


"""
~~~~~~~~~~~~ API ~~~~~~~~~~~~
"""


@app.route("/")
def hello_world():
    return create_response({"content": "hello world!"})


@app.route("/mirror/<name>")
def mirror(name):
    data = {"name": name}
    return create_response(data)

# PART 6
@app.route("/shows", methods=['GET'])
def get_all_shows():
    if request.args.get('minEpisodes'):
        data = db.getByMinEpisodes('shows', int(request.args.get('minEpisodes')))
        if data == []: # no shows have the min number of episodes
            return create_response(status=404, message="No shows fit the specified minEpisode parameter")
        return create_response({'shows': data})
    return create_response({"shows": db.get('shows')})

@app.route("/shows/<id>", methods=['DELETE'])
def delete_show(id):
    if db.getById('shows', int(id)) is None:
        return create_response(status=404, message="No show with this id exists")
    db.deleteById('shows', int(id))
    return create_response(message="Show deleted")


# TODO: Implement the rest of the API here!

# PART 2
@app.route("/shows/<id>", methods=['GET'])
def get_show(id):
    if db.getById('shows', int(id)) is None:
        return create_response(status=404, message="No show with this id exists")
    return create_response({"show": db.getById('shows', int(id))})


# PART 3
@app.route("/shows", methods=['POST'])
def post_show():
    request_data = request.get_json()
    for item in ['name', 'episodes_seen']:
        if item not in request_data:
            return create_response(status=422, message="<" + item + "> parameter is not provided")
    name = request_data['name']
    episodes_seen = request_data['episodes_seen']
    payload = {'name': name, 'episodes_seen': episodes_seen}
    data = db.create('shows', payload)
    return create_response(data, status=201)


# PART 4 (assumes only valid body parameters are provided)
@app.route("/shows/<id>", methods=['PUT'])
def put_show(id):
    if db.getById('shows', int(id)) is None:
        return create_response(status=404, message="No show with this id exists")
    request_data = request.get_json()
    return create_response({"show": db.updateById('shows', int(id), request_data)}, status=201)


"""
~~~~~~~~~~~~ END API ~~~~~~~~~~~~
"""
if __name__ == "__main__":
    app.run(port=8080, debug=True)
