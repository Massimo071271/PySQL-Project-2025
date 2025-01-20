import sys
from dotenv import load_dotenv
import os
from db_manager import DBManager
from search import Search
from display import Display

# Load environment variables
load_dotenv()

class MainApp:
    def __init__(self):
        self.manager = DBManager()
        self.search = Search(self.manager)
        self.display = Display()

    def main_menu(self):
        while True:
            self.display.show_menu()
            choice = input("Enter the command number: ").strip()

            if choice == "1":
                title = input("Enter the movie title: ").strip()
                results = self.search.by_title(title)
                self.display.show_results(results)

            elif choice == "2":
                release_year = input("Enter the release year: ").strip()
                results = self.search.by_release_year(release_year)
                self.display.show_results(results)

            elif choice == "3":
                categories = self.search.get_categories()
                self.display.show_categories(categories)
                category_number = input("Enter the category number: ").strip()

                try:
                    category_index = int(category_number) - 1
                    if 0 <= category_index < len(categories):
                        category_name = categories[category_index]['category']
                        results = self.search.by_category(category_name)
                        self.display.show_results(results)

                    else:
                        print("Invalid category number.")

                except ValueError:
                    print("Please enter a valid number.")

            elif choice == "4":
                actor_name = input("Enter the actor's first or last name: ").strip()
                results = self.search.by_actor_lastname(actor_name)
                self.display.show_results(results)

            elif choice == "5":
                keyword = input("Enter the keyword for search: ").strip()
                results = self.search.by_keyword(keyword)
                self.display.show_results(results)

            elif choice == "6":
                operator = input("Enter the operator (> < =): ").strip()
                duration = input("Enter the duration in minutes: ").strip()
                results = self.search.by_duration(operator, duration)
                self.display.show_results(results)

            elif choice == "7":
                prices = self.search.get_ticket_prices()
                self.display.show_prices(prices)
                price = input("Enter the ticket price from the list: ").strip()

                try:
                    results = self.search.by_ticket_price(float(price))
                    self.display.show_results(results)

                except ValueError:

                    print("Please enter a valid numeric price.")

            elif choice == "8":
                ratings = self.search.get_ratings()
                self.display.show_ratings(ratings)
                rating = input("Enter the rating from the list: ").strip()
                results = self.search.by_rating(rating)
                self.display.show_results(results)


            elif choice == "9":
                popular_queries = self.search.get_popular_queries()
                self.display.show_popular_queries(popular_queries)


            elif choice == "10":
                print("Exiting the program.")
                self.manager.close()
                sys.exit()

            else:
                print("Invalid input. Please select a valid option.")

if __name__ == "__main__":
    app = MainApp()
    app.main_menu()
