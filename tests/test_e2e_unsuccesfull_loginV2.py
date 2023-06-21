import pytest
from playwright.async_api import async_playwright
from elements.login import LoginPage

@pytest.mark.asyncio
@pytest.mark.parametrize(
    "username, password, err",
    [
        ("locked_out_user", "secret_sauce", "Epic sadface: Sorry, this user has been locked out."),  # Locked out user
        ("nonexistent_user", "secret_sauce", "Epic sadface: Username and password do not match any user in this service"),  # Nonexistent user
        ("standard_user", "wrong_password", "Epic sadface: Username and password do not match any user in this service"),  # Wrong password
        (None, "secret_sauce", "Epic sadface: Username is required"),  # Missing username
        ("standard_user", None, "Epic sadface: Password is required"),  # Missing password
    ],
)
async def test_e2e_unsuccessful_login(username, password, err):
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=False, slow_mo=1000)
        context = await browser.new_context()
        page = await context.new_page()

        await page.goto("https://www.saucedemo.com/")

        login_page = LoginPage(page)

        # Perform unsuccessful login
        if username:
            await login_page.enter_username(username)
        if password:
            await login_page.enter_password(password)
        await login_page.click_login()

        # Verify error message
        error_message_text = await login_page.get_error_message_text()

        assert error_message_text == err

        # Close the context, but not the browser
        await context.close()
