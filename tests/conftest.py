import pytest
from pages.vk_auth import VKLogin

@pytest.fixture()
def vk_login():
    vk = VKLogin()
    yield vk
    vk.exit()