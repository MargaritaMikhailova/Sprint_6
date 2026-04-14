# Sprint_6 - Тестирование сервиса аренды самокатов

Автотесты для сайта [qa-scooter.praktikum-services.ru](https://qa-scooter.praktikum-services.ru/)

## Описание проекта

Проект содержит автоматизированные тесты для проверки функциональности сервиса аренды самокатов:
- Создание заказа через разные кнопки
- Проверка ответов на вопросы в разделе "Вопросы о важном"
- Проверка работы логотипов и навигации

## Технологии

- **Python** 3.9+
- **Selenium** 4.41.0
- **Pytest** 9.0.2
- **Allure** 2.15.3
- **Page Object Pattern**

#### Запуск всех тестов
pytest tests/ -v

#### Запуск конкретного теста
pytest tests/test_order.py -v
pytest tests/test_questions.py -v
pytest tests/test_logo.py -v

#### Открытие отчёта
allure open allure-report
