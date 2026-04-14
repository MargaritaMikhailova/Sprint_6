from selenium.webdriver.common.by import By

# Кнопки

class Buttons:

    BUTTON_QUESTION = (By.CLASS_NAME, "accordion__heading")
    BUTTON_ORDER_UP = (By.XPATH, "(//button[contains(@class, 'Button_Button__ra12g') and text()='Заказать'])[1]")
    BUTTON_ORDER_DOWN = (By.XPATH, "(//button[contains(@class, 'Button_Button__ra12g') and text()='Заказать'])[2]")
    BUTTON_SUBWAY = (By.XPATH, "//button[@value='5']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")
    RETURN_BUTTON = (By.XPATH, "//button[text()='Назад']")
    YES_BUTTON = (By.XPATH, "//*[contains(text(), 'Да')]")
    NO_BUTTON = (By.XPATH, "//*[contains(text(), 'Нет')]")
    BUTTON_IN_ORDER = (By.XPATH, "//div[contains(@class, 'Order_Buttons')]//button[text()='Заказать']")
    BUTTON_STATUS = (By.XPATH, "//*[contains(text(), 'Посмотреть статус')]")
    BUTTON_LOGOTYPE = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")
    BUTTON_YANDEX = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")

#Элементы проверок
class Element_check:

    MAIN_PAGE = (By.CLASS_NAME, "App_App__15LM-")
    BLOCK_QUESTION = (By.CLASS_NAME, "accordion")
    PRE_REQ_ORDER = (By.XPATH, "//div[contains(@class, 'Order_ModalHeader__3FDaJ') and contains(text(), 'Хотите оформить заказ?')]")
    SUCCESS_ORDER = (By.XPATH, "//div[contains(@class, 'Order_ModalHeader__3FDaJ') and contains(text(), 'Заказ оформлен')]")
    SECOND_PAGE_FORM = (By.CLASS_NAME, "Order_Content__bmtHS")

    @staticmethod
    def check_question(question):
        return (By.XPATH, f"//div[@class='accordion__button' and contains(., '{question}')]")

    @staticmethod
    def check_answer(answer):
        return (By.XPATH, f"//div[@class='accordion__panel']//p[contains(., '{answer}')]")

    @staticmethod
    def get_number(text: str):
        match = re.search(r'\d{6}', text)
        return match.group() if match else None

# Поля ввода

class Fill_order:

    NAME = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    SUBWAY = (By.XPATH, "//input[@placeholder='* Станция метро']")
    NUMBER = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    DATE =  (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    LONG_PERIOD = (By.XPATH, "//div[contains(@class, 'Dropdown-control')]")
    COLOR = (By.XPATH, "//div[text()='* Цвет самоката']")
    COMMENT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    TYPE_RENT = (By.XPATH, "//div[contains(@class, 'Dropdown-option') and text()='двое суток']")
    TYPE_COLOR = (By.XPATH, "//label[text()='чёрный жемчуг']")


