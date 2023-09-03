import pytest

import random


@pytest.fixture
def get_admin(add_browser):
    return random.randint(5, 10)

def test_simple(get_admin, add_browser):
    assert get_admin == 5
    assert 1 == 1 # Единица не должна быть равна двойке

def test_another(get_admin):
    assert get_admin == 5
    assert 1 == 1
