from pages.product_page import ProductPage


# run: pytest -s test_product_page.py
# link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"  # test1
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"  # test2


def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                        # открываем страницу
    page.go_to_basket_page()           # выполняем метод страницы - переходим на страницу корзины
    # Проверить сообщение о добавлении товара в корзину, сравнить название и цену.
    page.solve_quiz_and_get_code()
    # page.should_be_product_status()
    # should_be_product_name()
    # should_be_product_cost()
