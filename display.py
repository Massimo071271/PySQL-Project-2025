class Display:
    def show_menu(self) -> None:
        """
        Displays the main menu for the program.

        Returns:
            None
        """
        print("\nHello! I am your assistant in the world of cinema! \nSelect the section to search for the information you need:")
        print("\n1. Search by movie title")
        print("2. Search by release year")
        print("3. Search by movie category")
        print("4. Search by actor's last name")
        print("5. Search by keyword in description")
        print("6. Search by movie duration")
        print("7. Search by ticket price")
        print("8. Search by rating")
        print("9. Display popular queries")
        print("10. Exit the program")

    def show_results(self, results) -> None:
        """
        Displays the search results in a columnar format, with each field on a new line.

        Args:
            results (list): The list of search results to display.
        """
        if not results:
            print("\nNo results found.")
            return

        print("\nSearch Results:")
        for idx, row in enumerate(results, start=1):
            title = row.get('title', 'N/A')
            description = row.get('description', 'N/A')
            release_year = row.get('release_year', 'N/A')
            category = row.get('category', 'N/A')
            actors = row.get('actors', 'N/A')
            price = row.get('price', 'N/A')
            length = row.get('length', 'N/A')
            rating = row.get('rating', 'N/A')

            print(f"\nFilm {idx}:")
            print(f"Title: {title}")
            print(f"Description: {description}")
            print(f"Release Year: {release_year}")
            print(f"Category: {category}")
            print(f"Actors: {actors}")
            print(f"Price: {price}")
            print(f"Length: {length} min")
            print(f"Rating: {rating}")

    def show_categories(self, categories) -> None:
        print("\nAvailable categories:")
        for idx, category in enumerate(categories, start=1):
            print(f"{idx}: {category['category']}")

    def show_prices(self, prices) -> None:
        """
        Displays the available ticket prices.

        Args:
            prices (list): The list of prices to display.
        """
        print("\nAvailable ticket prices:")
        for price in prices:
            print(f"{price['price']}")

    def show_ratings(self, ratings) -> None:
        print("\nAvailable ratings:")
        for rating in ratings:
            print(rating['rating'])

    def show_popular_queries(self, queries) -> None:
        """
        Displays the most popular queries.

        Args:
            queries (list): The list of popular queries to display.
        """
        print("\nPopular queries:")
        for query in queries:
            print(f"{query['query_text']} - {query['count']} searches")


