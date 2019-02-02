from flask import Flask  # pragma: no cover


def create_app():  # pragma: no cover
    """
    Create app flask
    :return: new app
    """
    new_app = Flask(__name__)
    new_app.debug = True
    new_app.config['JSON_SORT_KEYS'] = False

    with new_app.app_context():
        pass

    return new_app


app = create_app()  # pragma: no cover
