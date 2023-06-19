"""Review the assortiment and add it all to the cart"""
import pytest
from elements.products import ProductDetailPage
from elements.cart import CartPage

@pytest.mark.asyncio
async def test_e2e_product_details(page_with_login):
    async for page in page_with_login:
        product_detail_page = ProductDetailPage(page)
        cart_page = CartPage(page)

        product_list = [
            "Sauce Labs Backpack",
            "Sauce Labs Bike Light",
            "Sauce Labs Bolt T-Shirt",
            "Sauce Labs Fleece Jacket",
            "Sauce Labs Onesie",
            "Test.allTheThings() T-Shirt (Red)"
        ]

        product_cards = await page.query_selector_all(".inventory_item")
        cart_item_names = []

        for i in range(len(product_cards)):
            item_title_element = (await page.query_selector_all(".inventory_item_name"))[i]
            await item_title_element.click()

            # Check the item's title
            item_title = await product_detail_page.get_item_title()
            assert item_title == product_list[i]

            # Add the item to the cart
            await product_detail_page.add_to_cart()

            # Navigate back to the inventory page
            await product_detail_page.navigate_back_to_products()

            # Add item name to cart_item_names list
            cart_item_names.append(item_title)

        await cart_page.open_cart()

        # Check if all the products are in the cart
        assert set(cart_item_names) == set(product_list)

        # Check the total count of items in the cart
        cart_item_count = await cart_page.get_cart_item_count()
        assert cart_item_count == len(product_cards)
