import json
import pytest

from hello_world import app


def test_lambda_handler():

    ret = app.lambda_handler("", "")
    assert ret == "hello world"

def test_hello():
    actual = "hello test"
    assert actual == "hello test"

