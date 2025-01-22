from colorama import Fore, Style, init

init(autoreset=True)

class Display:
    def __init__(self):
        self.menu_items = [
            "Search movie by title",
            "Search by release year",
            "Search by movie category",
            "Search by actor's last name",
            "Search by keyword in description",
            "Search by movie duration",
            "Search by ticket price",
            "Search by rating",
            "Display popular queries",
            "Exit the program"
        ]

    def show_menu(self) -> None:
        """
        Displays the main menu for the program with improved code organization.

        Returns:
            None
        """
        print(f"{Fore.CYAN}=" * 50)
        print(f"{Fore.GREEN}🎥 Welcome to Your Cinema Assistant! 🎥".center(50))
        print(f"{Fore.CYAN}=" * 50)
        print(f"{Fore.GREEN}\n📋 Choose an option from the menu below:\n")
        for index, item in enumerate(self.menu_items, start=1):
            print(f"{index}. {item}")
        print("\n" + f"{Fore.CYAN}=" * 50)

    def show_results(self, results: list[dict]) -> None:
        """
        Displays the search results in a columnar format, with each field on a new line.

        Args:
            results (list): The list of search results to display.
        """
        if not results:
            print(f"{Fore.RED}\nNo results found.")
            return

        print(f"{Fore.CYAN}\nSearch Results:")
        for idx, row in enumerate(results, start=1):
            print(f"{Fore.CYAN}\nFilm {idx}:")
            for key, value in row.items():
                value = f"{value} min" if key == 'length' else value  # Add 'min' for length field
                print(f"{key.capitalize()}: {value or 'N/A'}")

    def show_categories(self, categories) -> None:
        print(f"{Fore.CYAN}\nAvailable categories:")
        for idx, category in enumerate(categories, start=1):
            print(f"{idx}: {category['category']}")

    def show_prices(self, prices) -> None:
        """
        Displays the available ticket prices.

        Args:
            prices (list): The list of prices to display.
        """
        print(f"{Fore.CYAN}\nAvailable ticket prices:")
        for price in prices:
            print(f"{price['price']}")

    def show_ratings(self, ratings) -> None:
        print(f"{Fore.CYAN}\nAvailable ratings:")
        for rating in ratings:
            print(rating['rating'])

    def show_popular_queries(self, queries) -> None:
        """
        Displays the most popular queries.

        Args:
            queries (list): The list of popular queries to display.
        """
        print(f"{Fore.CYAN}\nPopular queries:")
        for query in queries:
            print(f"{Fore.CYAN}{query['query_text']} - {query['count']} searches")


