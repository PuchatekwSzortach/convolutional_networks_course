"""
Module to run the server
"""

import flask


APP = flask.Flask("convolutional_networks")


@APP.route("/")
def render_index():

    return flask.render_template("index.html")


if __name__ == "__main__":

    # To prevent loading model twice, set use_reloader to False
    APP.run(host="0.0.0.0", use_reloader=True, extra_files=["./templates/index.html", "./templates/macros.html"])
