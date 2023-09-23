import herm

def test_find_api_key():
    herm.api_key = "HELLO1"
    assert herm.api_key == "HELLO1"