#!/usr/bin/env python3

# Stdlib imports
import os
import json

# Internal imports

# 3rd party imports
from bottle import run, route, template


@route("/")
def index():
    return


if __name__ == "__main__":
    run(host="0.0.0.0", port=8080, reloader=True, debug=True)

