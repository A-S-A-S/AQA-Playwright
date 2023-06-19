from playwright.async_api import Page

class ProductDetailPage:
    def __init__(self, page: Page):
        self.page = page

    async def get_item_title(self):
        item_title = await self.page.inner_text(".inventory_details_name")
        return item_title

    async def add_to_cart(self):
        await self.page.click(".btn_primary")

    async def navigate_back_to_products(self):
        await self.page.click("[data-test=\"back-to-products\"]")

    async def is_product_page(self):
        item_title = await self.page.query_selector(".inventory_details_name")
        return item_title is not None
