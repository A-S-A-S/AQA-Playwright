from playwright.async_api import Page

class CheckoutPage:
    def __init__(self, page: Page):
        self.page = page

    async def fill_checkout_form(self, first_name="John", last_name="Doe", postal_code="12345"):
        await self.page.fill("[data-test=\"firstName\"]", first_name)
        await self.page.fill("[data-test=\"lastName\"]", last_name)
        await self.page.fill("[data-test=\"postalCode\"]", postal_code)

    async def proceed_to_summary(self):
        await self.page.click("[data-test=\"continue\"]")

    async def back_to_card(self):
        await self.page.click("[data-test=\"cancel\"]")
