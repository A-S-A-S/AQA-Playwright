class ConfirmationPage:
    def __init__(self, page):
        self.page = page

    async def is_confirmation_displayed(self):
        confirmation_selector = ".complete-header"
        confirmation_element = await self.page.query_selector(confirmation_selector)
        return confirmation_element is not None

    async def get_item_total(self):
        item_total_label = await self.page.query_selector(".summary_subtotal_label")
        item_total = await item_total_label.text_content()
        return item_total

    async def get_tax(self):
        tax_label = await self.page.query_selector(".summary_tax_label")
        tax = await tax_label.text_content()
        return tax

    async def get_total_cost(self):
        total_cost_label = await self.page.query_selector(".summary_total_label")
        total_cost = await total_cost_label.text_content()
        return total_cost

    async def complete_purchase(self):
        await self.page.click("[data-test=\"finish\"]")
