import pytest

@pytest.fixture
def add_browser():
    print('Открываю браузер')
    yield 'Chrome'
    print('Закрываю браузер')

@pytest.fixture
def get_admin(add_browser):
    return 5

def test_simple(get_admin, add_browser):
    assert get_admin == 5
    assert 1 == 1 # Единица не должна быть равна двойке

def test_another():
    assert 1 == 1
