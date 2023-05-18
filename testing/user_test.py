import pytest
import json
from user import User

def test_show_details():
    user = User("Rafael", 27, "Male")
    assert user.show_details() == json.dumps({"name": "Rafael", "age": 27, "gender": "Male"})