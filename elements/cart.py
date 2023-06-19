from playwright.async_api import Page

class CartPage:
    def __init__(self, page: Page):
        self.page = page

    async def open_cart(self):
        # Open the cart by clicking on the cart container
        await self.page.click("#shopping_cart_container")

    async def get_cart_items(self):
        # Get all cart items on the page
        cart_items = await self.page.query_selector_all(".cart_item")
        return cart_items

    async def get_cart_item_names(self):
        # Get the names of all items in the cart
        cart_items = await self.get_cart_items()
        item_names = []
        for item in cart_items:
            item_name_locator = item.locator(".inventory_item_name")
            item_name = await item_name_locator.text_content()
            item_names.append(item_name)
        return item_names

    async def remove_item_from_cart(self, item_name):
        # Remove a specific item from the cart by name
        cart_items = await self.get_cart_items()
        for item in cart_items:
            item_name_locator = item.locator(".inventory_item_name")
            current_item_name = await item_name_locator.text_content()
            if current_item_name == item_name:
                remove_button_locator = item.locator(".cart_button")
                await remove_button_locator.click()
                break

    async def is_item_in_cart(self, item_name):
        # Check if a specific item is present in the cart by name
        cart_items = await self.get_cart_items()
        for item in cart_items:
            item_name_element = await item.query_selector(".inventory_item_name")
            current_item_name = await item_name_element.text_content()
            if current_item_name == item_name:
                return True
        return False

    async def get_cart_item_count(self):
        # Get the count of items in the cart
        cart_items = await self.get_cart_items()
        return len(cart_items)

    async def proceed_to_checkout(self):
        # Proceed to checkout by clicking the checkout button
        await self.page.click(".checkout_button")
