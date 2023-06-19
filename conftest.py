import pytest
from playwright.async_api import async_playwright
from elements.login import LoginPage

@pytest.fixture(scope="function")
async def page_with_login():
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=True,)
        context = await browser.new_context()
        page = await context.new_page()

        await page.goto("https://www.saucedemo.com/")
        login_page = LoginPage(page)
        await login_page.perform_complete_login("standard_user", "secret_sauce")

        yield page

        await context.close()
        await browser.close()
