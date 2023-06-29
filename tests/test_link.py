from playwright.sync_api import Page, expect


def test_link(page: Page) -> None:
    page.goto("http://localhost:3000/")

    page.locator('input[type="text"]').click()

    page.locator('input[type="text"]').fill("Luis")

    page.get_by_role("button", name="Submit").click()
