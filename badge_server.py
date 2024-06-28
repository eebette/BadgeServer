import json
from typing import Dict
import flask
import pybadges

app = flask.Flask(__name__)


@app.route("/bank_scrapers")
def serve_badge() -> flask.Response:
    """
    Serve a badge image based on the request query string.
    :return: A flask response object with the requested badge
    """
    with open("/tests/bank_scrapers/tests.json") as json_file:
        tests: Dict = json.load(json_file)

    b: Dict = tests[flask.request.args.get("name")]

    badge: str = pybadges.badge(
        left_text=b["test_date"],
        right_text="Verified" if b["status"] == "passed" else "Failed",
        right_color="green" if b["status"] == "passed" else "red",
    )

    response: flask.Response = flask.make_response(badge)
    response.content_type = "image/svg+xml"
    return response


if __name__ == "__main__":
    app.run()
