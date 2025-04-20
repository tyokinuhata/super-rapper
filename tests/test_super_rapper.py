from src.super_rapper.super_rapper import SuperRapper

def test_default_tempo():
    rapper = SuperRapper()
    assert rapper.get_tempo() == 120

def test_set_tempo():
    rapper = SuperRapper()
    rapper.tempo(bpm=140)
    assert rapper.get_tempo() == 140

def test_method_chaining():
    rapper = SuperRapper()
    chained_rapper = rapper.tempo(bpm=160).tempo(bpm=180)
    assert chained_rapper.get_tempo() == 180
    assert chained_rapper is rapper
