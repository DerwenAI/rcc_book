#!/usr/bin/env python
# encoding: utf-8

from flask import Flask, render_template
import sys

APP = Flask(__name__, static_folder="_build/html/_static", template_folder="_build/html")


@APP.route("/")
def page_home():
    return render_template("index.html")


if __name__ == "__main__":
    PORT = int(sys.argv[1])
    APP.run(host="0.0.0.0", port=PORT, debug=True)
