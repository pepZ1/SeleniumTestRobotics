# SeleniumTestRobotics
Selenium Automaton project

Тестран для сайта https://mobistore.by/ 

chromedriver.exe находится в папке utilities укажите полный путь до него в файле 
test_by_product.py
g = Service('ваш путь\\utilities\\chromedriver.exe')

запуск теста из test_by_product.py/n
авторизация на сайте в login_page.py
выбор категории продукта в main_page.py и проверка по url
выставление фильтров и вырбор продукта с переходом в карзину в filters_notebook_page.py
оформление товара, способ оплаты и доставки, проверка по слову в cart_page.py
скриншот с последней страницы сохраняется в папку screen из finish_page.py
