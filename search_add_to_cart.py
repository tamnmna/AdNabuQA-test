from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Automation:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 50)

    def open_website(self):
        self.driver.get("https://adnabu-store-assignment1.myshopify.com/")

    def search_product(self, product_name):
        search_box = self.wait.until(
            EC.presence_of_element_located((By.NAME, "q"))
        )

        search_box.clear()
        search_box.send_keys(product_name)
        search_box.send_keys(Keys.ENTER)

    def open_product(self):
        product = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".card-information__text"))
        )
        product.click()

    def add_to_cart(self):
        add_to_cart_button = self.wait.until(
            EC.element_to_be_clickable(
                (By.NAME, "add")
            )
        )
        add_to_cart_button.click()

    def verify_cart(self):
        cart_item = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".cart-item"))
        )

        if cart_item.is_displayed():
            print("Product added to cart successfully")

    def close_browser(self):
        input("Press Enter to close browser...")
        self.driver.quit()


if __name__ == "__main__":

    test = Automation()

    test.open_website()
    test.search_product("shirt")
    test.open_product()
    test.add_to_cart()
    test.verify_cart()
    test.close_browser()