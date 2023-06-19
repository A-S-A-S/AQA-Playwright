from playwright.async_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page

    async def enter_username(self, username: str):
        await self.page.fill("[data-test=\"username\"]", username)

    async def enter_password(self, password: str):
        await self.page.fill("[data-test=\"password\"]", password)

    async def click_login(self):
        await self.page.click("[data-test=\"login-button\"]")

    async def get_error_message_text(self):
        error_message_locator = self.page.locator("[data-test=\"error\"]")
        return await error_message_locator.text_content()

    async def perform_complete_login(self, username: str, password: str):
        await self.enter_username(username)
        await self.enter_password(password)
        await self.click_login()
