﻿## Тесты на проверку параметра name при создании набора продуктов (зарегистрированным пользователем) в Яндекс Прилавок с помощью API Яндекс Прилавок.
____
### **Основной файловый состав проекта:**
1) data.py - данные для регистрации пользователя и создания продуктового набора;
2) configuration.py - ссылка на тестовый стенд, и API *ручки* для регистрации пользователя и создания продуктового набора;
3) sender_stand_request.py - функции регистрации пользователя и создания продуктового набора;
4) create_kit_name_kit_test.py - функции: подготовка токена, подготовка тела  для последующих тестов, описание позитивной и негативной функции и 11 тестов на проверку параметра "name" при создании продуктового набора.
### **Вспомогательный файловый состав проекта:**
1) .gitignore - для исключения публикации в Git автоматически генерируемых файлов;
2) README.md - инструкция и описание к проекту.
____
### **Инструкция к применению:**
1) Для осуществления тестирования необходим рабочий тестовый стенд "Яндекс Прилавок";
2) Для запуска функций и тестов необходимо установить пакеты: requests, pytest;
3) Выполнение авто-тестов запускается командой "pytest create_kit_name_kit_test.py".# Portfolio_auth-test