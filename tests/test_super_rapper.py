from src.super_rapper.super_rapper import SuperRapper

def test_hello_world():
    rapper = SuperRapper()
    message = rapper.hello_world()
    expected = "hello, world!"
    assert expected == message
