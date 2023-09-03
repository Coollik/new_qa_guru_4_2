import pytest
@pytest.fixture
def add_browser():
    print('Открываю браузер')
    yield 'Chrome'
    print('Закрываю браузер')