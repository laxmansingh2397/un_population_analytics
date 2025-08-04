"""
This module analyzes Population data to calculate and plot
ASEAN Countries Population Over Years.

It reads data from the 'Population.csv' file, processes the
asean countres population in year 2014, and displays the results in a bar chart.
"""
import csv
import matplotlib
from matplotlib import pyplot as plt
matplotlib.use('Tkagg')


def calculate_asean_countries_population_in_2014():
    """
    Calculates the population of each ASEAN country for the year 2014.

    Reads population data from the specified CSV file and extracts the population
    numbers of the ASEAN countries for the year 2014.

    Returns:
        dict: A dictionary where the keys are ASEAN country names and values are
        the population figures (as strings) for 2014.
    """
    asean_countries_population_2014 = {"Brunei Darussalam": "",
    "Cambodia" : "", "Indonesia" : "", "Lao PDR" : "", "Malaysia" : "",
    "Myanmar" : "", "Philippines" : "", "Singapore" : "", "Thailand" : "", "Vietnam" : ""}

    with open("../required_data/country_pop.csv", encoding="utf-8") as country_file:
        country_data = csv.DictReader(country_file)

        for countries in country_data:
            year = countries["year"]
            population = countries["population"]
            asean_countries = countries["country"]

            if year == "2014" and asean_countries in asean_countries_population_2014:
                asean_countries_population_2014[asean_countries] = population

    return asean_countries_population_2014


def plot_asean_countries_population_in_2014(asean_countries_population):
    """
    Plots a bar chart of the population of ASEAN countries in 2014.

    Args:
        asean_countries_population (dict): A dictionary with ASEAN country names as keys
            and their population as values for the year 2014.
    """
    plt.figure(figsize=(14,6))
    plt.title("ASEAN Countries Population In 2014")
    plt.bar(asean_countries_population.keys(), asean_countries_population.values(), color="blue")
    plt.xlabel("ASEAN Countries")
    plt.ylabel("Total Population")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()


def execute():
    """
    Executes the program workflow: calculates and plots ASEAN country populations for 2014.

    Calls functions to calculate ASEAN populations and display the results in a bar chart.
    """
    asean_countries_population = calculate_asean_countries_population_in_2014()
    plot_asean_countries_population_in_2014(asean_countries_population)


if __name__ == "__main__":

    execute()
