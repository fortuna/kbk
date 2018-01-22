from lxml import html


def main():
    # TODO: Get from the website
    with open("testdata/menu.html") as menu_page:
        root_node = html.parse(menu_page).getroot()

    products = []
    for product_node in root_node.findall(".//div[@class='product-content']"):
        product = {}
        anchor = product_node.find(".//a[@class='h3']")
        product["title"] = anchor.get("title")
        product["url"] = anchor.get("href")
        products.append(product)

    for product in products:
        # TODO: Get from the website
        with open("testdata/product_2_sizes.html") as product_page:
            root_node = html.parse(product_page).getroot()
        product["description"] = root_node.find("//h2").getnext().text_content()
        product["price"] = root_node.get_element_by_id("price").text_content()
        product["price_medium"] = root_node.get_element_by_id(
            "medium").get("data-price")
        product["price_large"] = root_node.get_element_by_id(
            "large").get("data-price")

        for nutrition_row in root_node.findall(".//table/tbody/tr"):
            label = nutrition_row.findtext("td").lower()
            product[label] = nutrition_row.findall("td")[1].text_content()

    for product in products:
        print(product)


if __name__ == "__main__":
    main()
