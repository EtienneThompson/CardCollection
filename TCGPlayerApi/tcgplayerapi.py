"""Class that can get market prices from the tcgplayer website."""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException

class TCGPlayerAPI():
    """This is designed so that it is instantiated once at the beginning of
        a single file, and that single instance is used across all parts of
        that file. This is because the startup for the broswer takes some time,
        and so instantiating multiples can take a long time/require too much
        memory."""


    def __init__(self):
        # This url doesn't work for everything on the TCGPlayer site.
        self.base_url = "https://www.tcgplayer.com/search/all/product?q="
        self.set_url = "https://shop.tcgplayer.com/magic/"
        # options = Options()
        # options.headless = True
        # self.driver = webdriver.Firefox(options=options)
        self.driver = webdriver.Firefox()


    def get_price(self, card_name, card_set=None):
        """
        Want to be able to search for multiple things.
        1. Generic searches of a singular card name. Only return market prices
            cards with the given card names (some generic searches return more
            cards than the one searched for).
        2. Specific searches, where a card name and set are given. This should
            only return the market price for that specific card.
        3. Handle searching multiple urls.
        """

        card_name = card_name.split(" ")
        card_query = "%20".join(card_name).lower()

        if card_set:
            prices = self.get_set_price(card_query, card_set)
        else:
            prices = self.get_generic_price(card_query)

        if prices[0] == -1:
            # The price fetch failed.
            print("Failed to fetch price.")

        return prices


    def get_generic_price(self, card_query):
        """Gets a list of cards from a generic all products endpoint."""
        endpoint = f"{self.base_url}{card_query}"
        # print(endpoint)
        prices = list()

        self.driver.get(endpoint)
        # Wait until a market price can be found, or no results were found.
        WebDriverWait(self.driver, 2).until(
            ec.visibility_of_element_located((
                By.XPATH,
                (
                    "//span[@class='search-result__market-price-value'] | "
                    "//div[@class='blank-slate']"
                )
            ))
        )

        # Check if no results were found.
        try:
            self.driver.find_element_by_xpath(
                "//div[@class='blank-slate']")
            return [-1]
        except NoSuchElementException:
            pass

        div = self.driver.find_element_by_xpath(
            ".//div[@id='app']")
        search_results = div.find_element_by_xpath(
            ".//span[@class='search-results']")
        results = search_results.find_elements_by_xpath(
            ".//div[@class='search-result']")

        for result in results:
            # Isolate the part of the webpage with the search results.
            body = result.find_element_by_xpath(
                ".//a[@class='search-result__body']")

            try:
                # Check if returned cards have the same name.
                name = body.find_element_by_xpath(
                    ".//div[@class='search-result__title']").text
                if " ".join(card_query.split("%20")) not in name.lower():
                    continue

                # Check if the cards are from the same game.
                game = body.find_element_by_xpath(
                    ".//div[@class='search-result__category-name']").text
                if game != "Magic: The Gathering":
                    # Card was from a different game, but had the same name.
                    continue

                # Finally get the market price if those previous two conditions
                # are true.
                market_price = body.find_element_by_xpath(
                    ".//span[@class='search-result__market-price-value']").text
                prices.append(market_price)

            except NoSuchElementException:
                # The card name, card game, or market price were unavailable,
                # so skip it.
                continue

        if not prices:
            prices.append(-1)

        return prices


    def get_set_price(self, card_query, card_set):
        """Gets a single card's information from a set specific endpoint."""
        card_set = "-".join(card_set.split(" "))
        endpoint = f"{self.set_url}{card_set.lower()}/{card_query}"
        print(endpoint)
        prices = list()

        self.driver.get(endpoint)
        # Wait until a market price can be found, or no results were found.
        WebDriverWait(self.driver, 2).until(
            ec.visibility_of_element_located((
                By.XPATH, (
                    "//td[@class='price-point__data'] | "
                    "//div[@id='maincontentinnerpadding']")
            ))
        )

        try:
            self.driver.find_element_by_xpath(
                ".//div[@id='maincontentinnerpadding']")
            print("nothing found")
            return [-1]
        except NoSuchElementException:
            pass

        try:
            # Narrow down the webpage.
            price_guide = self.driver.find_element_by_xpath(
                ".//section[@class='price-guide']")
            market_section = price_guide.find_element_by_xpath(
                ".//div[@class='price-point price-point--market']")

            # Scrape the market prices.
            market_price = market_section.find_element_by_xpath(
                ".//td[@class='price-point__data']").text
            prices.append(market_price)
        except NoSuchElementException as e:
            # Put the not found value in the list instead if an element is not
            # found.
            print(e)
            prices.append(-1)

        return prices


    def close(self):
        """Stop the browser."""
        self.driver.close()
