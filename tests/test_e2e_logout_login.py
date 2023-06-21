"""Ensure that the logout and login process does not reset the state of the cart"""
import pytest
from elements.menu import MenuComponent
from elements.products import ProductDetailPage
from elements.cart import CartPage
from elements.login import LoginPage


@pytest.mark.asyncio
async def test_e2e_logout_login(page_with_login):
    async for page in page_with_login:
        menu_component = MenuComponent(page)
        login_page = LoginPage(page)
        product_detail_page = ProductDetailPage(page)
        cart_page = CartPage(page)

        # Add an item to the cart
        await product_detail_page.add_to_cart()

        # Perform logout
        await menu_component.open_menu()
        await menu_component.click_logout()

        # Login again
        await login_page.perform_complete_login("standard_user", "secret_sauce")

        # Verify that state was not reset
        await cart_page.open_cart()
        assert await cart_page.is_item_in_cart("Sauce Labs Backpack")
