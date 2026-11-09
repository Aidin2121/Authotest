class LoginPage:
    URL = "https://the-internet.herokuapp.com/login"

    def __init__(self, page):
        self.page = page
        self.username_field = page.locator("#username")
        self.password_field = page.locator("#password")
        self.login_button = page.locator('button[type="submit"]')
        self.messages = page.locator("#flash-messages")

    def open(self):
        self.page.goto(self.URL)

    def login(self, username, password):
        self.username_field.fill(username)
        self.password_field.fill(password)
        self.login_button.click()