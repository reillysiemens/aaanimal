from adjective_adjective_animal import generate


def test_generate():
    sep = "-"
    assert len(generate(2, sep=sep).split(sep)) == 3
