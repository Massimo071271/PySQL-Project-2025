Project Report: "Movie Search Application"
General Project Logic
Project Goal — Create an application to search for movie information in the sakila database. The program provides functionalities to:

Search movies based on various criteria, such as title, release year, category, actor, keyword, duration, ticket price, and rating.
Log popular queries and present them to the user.
Operate as a console-based application with a colorful interface.
The program is modular for better maintainability and development.

Project Modules

1. db_manager.py
Purpose: Manages database connections and executes SQL queries.
Class: DBManager
Methods:
__init__: Initializes the database connection using environment variables (.env).
execute_query: Executes SQL queries. Returns results for SELECT queries and commits changes for INSERT/UPDATE/DELETE.
close: Closes the database connection and cursor.

2. search.py
Purpose: Handles movie search logic and database interactions.
Class: Search
Methods:
log_query: Logs user queries into the query_logs table.
by_title: Searches movies by title.
by_release_year: Searches movies by release year.
get_categories: Retrieves a list of available categories.
by_category: Searches movies by category.
by_actor_lastname: Searches movies by an actor's first or last name.
by_keyword: Searches movies using a keyword.
by_duration: Searches movies by duration with comparison operators (>, <, =).
by_ticket_price: Searches movies by ticket price.
get_ticket_prices: Retrieves a list of unique ticket prices.
by_rating: Searches movies by rating.
get_ratings: Retrieves a list of available ratings.
get_popular_queries: Returns the most popular queries logged.

3. display.py
Purpose: Manages the display of menus and search results to the user.
Class: Display
Methods:
show_menu: Displays the main menu.
show_results: Displays search results in a formatted view.
show_categories: Displays available categories.
show_prices: Displays available ticket prices.
show_ratings: Displays available ratings.
show_popular_queries: Displays a list of the most popular queries.

4. main.py
Purpose: Controls the main application flow.
Class: MainApp
Methods:
main_menu: Handles user input and calls relevant functions.
search_by_title: Processes search requests for movies by title.
search_by_release_year: Processes search requests for movies by release year.
search_by_category: Processes search requests for movies by category.
search_by_actor: Processes search requests for movies by actor's name.
search_by_keyword: Processes search requests for movies by keyword.
search_by_duration: Processes search requests for movies by duration.
search_by_price: Processes search requests for movies by ticket price.
search_by_rating: Processes search requests for movies by rating.
show_popular_queries: Displays the most popular queries logged.
exit_program: Exits the application and displays a farewell message.
Methods and Arguments Used
Search Methods (Search):

Each method logs queries using log_query.
SQL queries use parameters to prevent SQL injection.
Methods return results as list[dict].
Menu and Display (Display):

Uses the colorama library for colored text output.
Methods like show_results handle results formatting for the user.
Database Management (DBManager):

Handles all SQL operations through execute_query.
Raises exceptions instead of printing errors, allowing better error handling.
Summary of Project Workflow
The user launches the application (main.py).
The main menu is displayed via Display.show_menu.
The user selects a menu option, and the application:
Executes a database query via Search (using DBManager).
Logs the query for analytics.
Displays results to the user via Display.
The user can repeat actions or exit the application.
Upon exit, the application calls exit_program, closing the database connection and displaying a farewell message.


Отчет по проекту "Movie Search Application"

Общая логика работы проекта

Цель проекта — создать приложение для поиска информации о фильмах в базе данных sakila.

Программа позволяет:

Искать фильмы по различным критериям, таким как название, год выпуска, категория, актер, ключевое слово, длительность,
цена на билет, рейтинг.
Логировать популярные запросы и предоставлять их пользователю.
Работать как консольное приложение с удобным цветным интерфейсом.
Программа разбита на несколько модулей для обеспечения модульности, удобства разработки и поддержки.

Модули проекта
1. db_manager.py
Назначение: Управление соединением с базой данных и выполнение SQL-запросов.
Класс: DBManager
Методы:
__init__: Инициализирует соединение с базой данных, ис.env).
execute_query: Выполняет SQL-запросы. Возвращает результат для SELECT запросов и фиксирует изменения для INSERT/UPDATE/DELETE.
close: Закрывает соединение с базой данных и курсор.

2. search.py
Назначение: Логика поиска фильмов и работы с данными из базы.
Класс: Search
Методы:
log_query: Логирует запросы в таблицу query_logs.
by_title: Поиск фильмов по названию
by_release_year: Поиск фильмов по году выпуска.
get_categories: Возвращает список доступных категорий.
by_category: Поиск фильмов по категории.
by_actor_lastname: Поиск фильмов по имени или фамилии актера.
by_keyword: Поиск фильмов по ключевому слову.
by_duration: Поиск фильмов по длительности с использованием операторов (>, <, =).
by_ticket_price: Поиск фильмов по цене билета.
get_ticket_prices: Возвращает список уникальных цен билетов.
by_rating: Поиск фильмов по рейтингу.
get_ratings: Возвращает список доступных рейтингов фильмов
get_popular_queries: Возвращает список самых популярных запросов.

3. display.py
Назначение: Отображение меню и результатов пользователю.
Класс: Display
Методы:
show_menu: Отображает главное меню.
show_results: Выводит результаты поиска.
show_categories: Выводит список доступных категорий.
show_prices: Выводит список доступных цен на билеты
show_ratings: Выводит список доступных рейтингов.
show_popular_queries: Выводит список популярных запросов.

4. main.py
Назначение: Управление основным процессом приложения.
Класс: MainApp
Методы:
main_menu: Управляет выбором пользователя и вызывает соответствующие функции.
search_by_title: Обрабатывает запрос поиска по названию фильма.
search_by_release_year: Обрабатывает запрос поиска по году выпуска.
search_by_category: Обрабатывает запрос поиска по категории.
search_by_actor: Обрабатывает запрос поиска по имени или фамилии актера.
search_by_keyword: Обрабатывает запрос поиска по ключевому слову.
search_by_duration: Обрабатывает запрос поиска по длительности фильма.
search_by_price: Обрабатывает запрос поиска по цене билета.
search_by_rating: Обрабатывает запрос поиска по рейтингу.
show_popular_queries: Отображает самые популярные запросы.
exit_program: Завершает работу программы с выводом прощального сообщения.

Используемые методы и аргументы

Методы поиска (Search):

У всех методов есть логирование запросов (log_query).
SQL-запросы используют параметры для предотвращения SQL-инъекций.
Результаты возвращаются в формате list[dict].

Меню и отображение (Display):

Используется библиотека colorama для цветного отображения текста.
Методы, такие как show_results, обрабатывают результаты в удобном формате.

Управление базой данных (DBManager):

Обработка всех запросов через execute_query.
Исключения генерируются в случае ошибок соединения или выполнения
Краткая логика работы проекта
Пользователь запускает программу (main.py).
Отображается главное меню через Display.show_menu.
Пользователь выбирает нужный пункт, после чего программа:
Выполняет SQL-запрос через Search (используя DBManager).
Логирует запрос.
Отображает результаты через Display.
Пользователь может продолжить работу или выйти из программы.
При выходе программа вызывает exit_program, закрывая соединение с базой данных и выводя прощальное сообщение.
