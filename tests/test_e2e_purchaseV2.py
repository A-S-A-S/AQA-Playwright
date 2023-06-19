"""Happy Path of purchasing the 1st item — Sauce Labs Backpack"""
import pytest
from elements.products import ProductDetailPage
from elements.cart import CartPage
from elements.checkout import CheckoutPage
from elements.confirmation import ConfirmationPage

@pytest.mark.asyncio
async def test_e2e_product_details(page_with_login):
    async for page in page_with_login:
        product_detail_page = ProductDetailPage(page)
        cart_page = CartPage(page)
        checkout_page = CheckoutPage(page)
        confirmation_page = ConfirmationPage(page)

        # Add an item to the cart
        await product_detail_page.add_to_cart()

        # Go to the cart page
        await cart_page.open_cart()

        # Verify the added item is in the cart
        assert await cart_page.is_item_in_cart("Sauce Labs Backpack")

        # Get the number of items in the cart
        items_count = await cart_page.get_cart_item_count()
        assert items_count == 1

        # Proceed to checkout
        await cart_page.proceed_to_checkout()

        # Fill out the checkout form
        await checkout_page.fill_checkout_form()

        # Proceed to the order summary
        await checkout_page.proceed_to_summary()

        # Verify the checkout summary and total
        assert await confirmation_page.get_item_total() == "Item total: $29.99"
        assert await confirmation_page.get_tax() == "Tax: $2.40"
        assert await confirmation_page.get_total_cost() == "Total: $32.39"

        # Complete the purchase
        await confirmation_page.complete_purchase()

        # Verify the order confirmation
        assert await confirmation_page.is_confirmation_displayed()

