import pytest

@pytest.fixture()
def set_up():
    print('\nStart Test')
    yield
    print('\nFinish Test')