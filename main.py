import sys
from dotenv import load_dotenv
import os
from db_manager import DBManager
from search import Search
from display import Display
from typing import Optional
from colorama import Fore

# Load environment variables
load_dotenv()

class MainApp:
    def __init__(self):
        """
        Initializes the MainApp class.
        Sets up database manager, search logic, and display functionality.
        """
        self.manager: DBManager = DBManager()
        self.search: Search = Search(self.manager)
        self.display: Display = Display()

    def main_menu(self) -> None:
        """
        Displays the main menu and handles user input for various commands.
        """
        while True:
            self.display.show_menu()
            choice: str = input(f"{Fore.GREEN}\nEnter the command number: ").strip()

            try:
                if choice == "1":
                    self.search_by_title()
                elif choice == "2":
                    self.search_by_release_year()
                elif choice == "3":
                    self.search_by_category()
                elif choice == "4":
                    self.search_by_actor()
                elif choice == "5":
                    self.search_by_keyword()
                elif choice == "6":
                    self.search_by_duration()
                elif choice == "7":
                    self.search_by_price()
                elif choice == "8":
                    self.search_by_rating()
                elif choice == "9":
                    self.show_popular_queries()
                elif choice == "10":
                    self.exit_program()
                else:
                    print(f"{Fore.RED}Invalid input. Please select a valid option.")
            except Exception as e:
                print(f"{Fore.RED}An error occurred: {e}")

    def search_by_title(self) -> None:
        """Handles searching for movies by title."""
        title: str = input(f"{Fore.GREEN}Enter the movie title: ").strip()
        results = self.search.by_title(title)
        self.display.show_results(results)

    def search_by_release_year(self) -> None:
        """Handles searching for movies by release year."""
        release_year: str = input(f"{Fore.GREEN}Enter the release year: ").strip()
        results = self.search.by_release_year(release_year)
        self.display.show_results(results)

    def search_by_category(self) -> None:
        """Handles searching for movies by category."""
        categories = self.search.get_categories()
        self.display.show_categories(categories)
        category_number: str = input(f"{Fore.GREEN}Enter the category number: ").strip()

        try:
            category_index: int = int(category_number) - 1
            if 0 <= category_index < len(categories):
                category_name = categories[category_index]['category']
                results = self.search.by_category(category_name)
                self.display.show_results(results)
            else:
                print(f"{Fore.RED}Invalid category number.")
        except ValueError:
            print(f"{Fore.RED}Please enter a valid number.")

    def search_by_actor(self) -> None:
        """Handles searching for movies by actor's name."""
        actor_name: str = input(f"{Fore.GREEN}Enter the actor's first or last name: ").strip()
        results = self.search.by_actor_lastname(actor_name)
        self.display.show_results(results)

    def search_by_keyword(self) -> None:
        """Handles searching for movies by a keyword."""
        keyword: str = input(f"{Fore.GREEN}Enter the keyword for search: ").strip()
        results = self.search.by_keyword(keyword)
        self.display.show_results(results)

    def search_by_duration(self) -> None:
        """Handles searching for movies by duration."""
        operator: str = input(f"{Fore.GREEN}Enter the operator (> < =): ").strip()
        duration: str = input(f"{Fore.GREEN}Enter the duration in minutes: ").strip()
        try:
            results = self.search.by_duration(operator, int(duration))
            self.display.show_results(results)
        except ValueError as e:
            print(f"{Fore.RED}Error: {e}")

    def search_by_price(self) -> None:
        """Handles searching for movies by ticket price."""
        prices = self.search.get_ticket_prices()
        self.display.show_prices(prices)
        price: str = input(f"{Fore.GREEN}Enter the ticket price from the list: ").strip()
        try:
            results = self.search.by_ticket_price(float(price))
            self.display.show_results(results)
        except ValueError:
            print(f"{Fore.RED}Please enter a valid numeric price.")

    def search_by_rating(self) -> None:
        """Handles searching for movies by rating."""
        ratings = self.search.get_ratings()
        self.display.show_ratings(ratings)
        rating: str = input(f"{Fore.GREEN}Enter the rating from the list: ").strip()
        results = self.search.by_rating(rating)
        self.display.show_results(results)

    def show_popular_queries(self) -> None:
        """Displays the most popular queries from the query logs."""
        popular_queries = self.search.get_popular_queries()
        self.display.show_popular_queries(popular_queries)

    def exit_program(self) -> None:
        """Handles exiting the program."""
        print(f"{Fore.GREEN} 🎥  Program actions are complete. See you again soon. Until next time! 🎥 ")
        self.manager.close()
        sys.exit()

if __name__ == "__main__":
    app = MainApp()
    app.main_menu()