from humanizer import humanize


def test_humanize_runs():
    text = "I am going to the store"
    output = humanize(text)

    assert isinstance(output, str)
    assert len(output) > 0