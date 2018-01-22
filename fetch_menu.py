from lxml import html

def main():
  with open("testdata/menu.html") as menu_file:
    root_node = html.parse(menu_file)
  product_nodes = root_node.xpath("//div[@class='product-content']")
  print(repr(product_nodes))

if __name__ == "__main__":
  main()