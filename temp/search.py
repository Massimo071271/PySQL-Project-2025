class Search:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    def log_query(self, query_text):
        """
        Logs the executed query in the query_logs table. If the query already exists, increments its count.
        """
        # Check if the query already exists
        check_query = "SELECT id FROM query_logs WHERE query_text = %s"
        params = (query_text,)
        existing = self.db_manager.execute_query(check_query, params)

        if existing:
            # If the query exists, increment the counter
            update_query = "UPDATE query_logs SET count = count + 1 WHERE id = %s"
            update_params = (existing[0]['id'],)
            self.db_manager.execute_query(update_query, update_params)
        else:
            # If the query is new, insert it
            insert_query = "INSERT INTO query_logs (query_text, count) VALUES (%s, 1)"
            self.db_manager.execute_query(insert_query, params)

    def by_title(self, title):
        """
        Search for movies by title using the film_list view.

        Args:
            title (str): The title or part of the title of the movie.

        Returns:
            list: A list of movies matching the title.
        """
        query = """
            SELECT *
            FROM film_list
            WHERE title LIKE %s
        """
        params = (f"%{title}%",)
        self.log_query(f"by_title: {title}")
        return self.db_manager.execute_query(query, params)

    def by_release_year(self, year):
        """
        Search for movies by release year using the film_list view.

        Args:
            year (str): The release year of the movie.

        Returns:
            list: A list of movies matching the release year.
        """
        query = """
            SELECT *
            FROM film_list
            WHERE release_year = %s
        """
        params = (year,)
        self.log_query(f"by_release_year: {year}")
        return self.db_manager.execute_query(query, params)

    def get_categories(self):
        """
        Returns a list of all available categories from the film_list view.

        Returns:
            list: A list of categories.
        """
        query = """
            SELECT DISTINCT category
            FROM film_list
            ORDER BY category
        """
        self.log_query("get_categories")
        return self.db_manager.execute_query(query)

    def by_category(self, category_name):
        """
        Search for movies by category using the film_list view.

        Args:
            category_name (str): The category name.

        Returns:
            list: A list of movies matching the category.
        """
        query = """
            SELECT *
            FROM film_list
            WHERE category = %s
        """
        params = (category_name,)
        self.log_query(f"by_category: {category_name}")
        return self.db_manager.execute_query(query, params)

    def by_actor_lastname(self, actor_name):
        """
        Search for movies by actor's name using the film_list view.

        Args:
            actor_name (str): The actor's first or last name.

        Returns:
            list: A list of movies featuring the actor.
        """
        query = """
            SELECT *
            FROM film_list
            WHERE actors LIKE %s
        """
        params = (f"%{actor_name}%",)
        self.log_query(f"by_actor_lastname: {actor_name}")
        return self.db_manager.execute_query(query, params)

    def by_keyword(self, keyword):
        """
        Search for movies by a keyword in the film_list view.

        Args:
            keyword (str): The keyword to search for.

        Returns:
            list: A list of movies matching the keyword.
        """
        query = """
            SELECT *
            FROM film_list
            WHERE title LIKE %s OR description LIKE %s OR category LIKE %s OR actors LIKE %s
        """
        params = (f"%{keyword}%", f"%{keyword}%", f"%{keyword}%", f"%{keyword}%")
        self.log_query(f"by_keyword: {keyword}")
        return self.db_manager.execute_query(query, params)

    def by_duration(self, operator, duration):
        """
        Search for movies by duration using the film_list view.

        Args:
            operator (str): The comparison operator ('>', '<', '=').
            duration (int): The duration in minutes.

        Returns:
            list: A list of movies matching the criteria.
        """
        if operator not in ('>', '<', '='):
            raise ValueError("Invalid operator. Only >, <, = are allowed.")

        query = f"""
            SELECT *
            FROM film_list
            WHERE length {operator} %s
        """
        params = (duration,)
        self.log_query(f"by_duration: {operator} {duration}")
        return self.db_manager.execute_query(query, params)

    def by_ticket_price(self, price):
        """
        Search for movies by ticket price using the film_list view.

        Args:
            price (float): The ticket price.

        Returns:
            list: A list of movies matching the price.
        """
        query = """
            SELECT *
            FROM film_list
            WHERE price = %s
        """
        params = (price,)
        self.log_query(f"by_ticket_price: {price}")
        return self.db_manager.execute_query(query, params)

    def get_ticket_prices(self):
        """
        Returns a list of distinct ticket prices from the film_list view.

        Returns:
            list: A list of available ticket prices.
        """
        query = """
            SELECT DISTINCT price
            FROM film_list
            ORDER BY price
        """
        self.log_query("get_ticket_prices")
        return self.db_manager.execute_query(query)

    def by_rating(self, rating):
        """
        Search for movies by rating using the film_list view.

        Args:
            rating (str): The movie rating.

        Returns:
            list: A list of movies matching the rating.
        """
        query = """
            SELECT *
            FROM film_list
            WHERE rating = %s
        """
        params = (rating,)
        self.log_query(f"by_rating: {rating}")
        return self.db_manager.execute_query(query, params)

    def get_ratings(self):
        """
        Returns a list of all available ratings from the film_list view.

        Returns:
            list: A list of available ratings.
        """
        query = """
            SELECT DISTINCT rating
            FROM film_list
            ORDER BY rating
        """
        self.log_query("get_ratings")
        return self.db_manager.execute_query(query)

    def get_popular_queries(self):
        """
        Returns the top 10 most popular queries, sorted by count in descending order.

        Returns:
            list: A list of popular queries with their counts.
        """
        query = """
            SELECT query_text, count
            FROM query_logs
            ORDER BY count DESC
            LIMIT 10
        """
        return self.db_manager.execute_query(query)

