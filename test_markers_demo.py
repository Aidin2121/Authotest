import pytest


def test_normal():
    assert 1 == 1


@pytest.mark.skip(reason="не актуален")
def test_skipped():
    assert 5 == 5



def test_known_bug():
    assert 2 + 2 == 4