import pytest
from playwright.sync_api import Page, expect


def test_login_success(page: Page, login_page):
    login_page.login("tomsmith", "SuperSecretPassword!")
    expect(page).to_have_url("https://the-internet.herokuapp.com/secure")
    expect(login_page.messages).to_contain_text("You logged into a secure area!")


@pytest.mark.parametrize("username, password, message", [
    ("tomsmith", "wrong", "Your password is invalid!"),
    ("tomsmit", "SuperSecretPassword!", "Your username is invalid!"),
])
def test_login_failed(page: Page, login_page, username, password, message):
    login_page.login(username, password)
    expect(page).to_have_url("https://the-internet.herokuapp.com/login")
    expect(login_page.messages).to_contain_text(message)







