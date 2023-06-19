from playwright.async_api import Page

class MenuComponent:
    def __init__(self, page: Page):
        self.page = page

    async def open_menu(self):
        menu_button = await self.page.wait_for_selector(".bm-burger-button")
        await menu_button.click()

    async def click_logout(self):
        logout_link = await self.page.wait_for_selector("#logout_sidebar_link")
        await logout_link.click()

    async def is_menu_open(self):
        menu_panel = await self.page.query_selector(".bm-menu")
        return menu_panel is not None

    async def is_logout_visible(self):
        logout_link = await self.page.query_selector("#logout_sidebar_link")
        return logout_link is not None
