import flask
import os
import hashlib

from utils.config import Config

blueprint = flask.Blueprint('api', __name__)

@blueprint.route("/api/upload", methods=['POST'])
def upload_file():
    if flask.request.headers.get("Authorization") != hashlib.md5(Config.get_auth_token().encode()).hexdigest():
        if flask.request.headers.get('Authorization') != Config.get_auth_token(): 
            return flask.jsonify({'error': 'unauthorized'}), 403

    if "file" not in flask.request.files:
        return flask.jsonify({'error': 'no file'}), 400

    file = flask.request.files['file']
    if file.filename == '':
        return flask.jsonify({'error': 'no file selected'}), 400

    if os.path.exists(os.path.join(Config.get_upload_dir(), file.filename)):
        return flask.jsonify({'error': 'file already exists'}), 409

    if file:
        filename = file.filename
        file.save(os.path.join(Config.get_upload_dir(), filename))
        return flask.jsonify({'success': True}), 200

    return flask.jsonify({'error': 'unknown error'}), 500

@blueprint.route("/api/change_auth_token", methods=['POST'])
def change_auth_token():
    if flask.request.headers.get("Authorization") != hashlib.md5(Config.get_auth_token().encode()).hexdigest():
        if flask.request.headers.get('Authorization') != Config.get_auth_token(): 
            return flask.jsonify({'error': 'unauthorized'}), 403

    new_auth_token = flask.request.headers.get('new_auth_token')
    if new_auth_token == '':
        return flask.jsonify({'error': 'no new auth token'}), 400

    Config.change_auth_token(new_auth_token)
    flask.session["authorization"] = new_auth_token
    return flask.jsonify({'success': True}), 200