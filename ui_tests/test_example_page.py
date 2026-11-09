from playwright.sync_api import Page, expect

def test_example_domain(page: Page):
    page.goto("https://example.com")
    expect(page).to_have_title("Example Domain")
    expect(page.locator("a")).to_have_text("Learn more")
    expect(page.locator("a")).to_have_attribute("href", "https://iana.org/help/example-domains")

