"""
This module analyzes Population data to calculate and plot
India Population Over Years.

It reads data from the 'Population.csv' file, processes the
india population over years, and displays the results in a bar chart.
"""
import csv
import matplotlib
from matplotlib import pyplot as plt
matplotlib.use('Tkagg')


def calculate_india_population_by_years():
    """
    Reads population data from a CSV file and calculates India's population for each year.

    Returns:
        dict: A dictionary where the keys are years (str) and the values
        are the population (str) of India for that year.
    """
    india_population_over_years = {}

    with open("../required_data/country_pop.csv", encoding="utf-8") as country_file:
        country_data = csv.DictReader(country_file)

        for countries in country_data:
            country = countries["country"]
            year = countries["year"]
            population = countries["population"]

            if country == "India":
                india_population_over_years[year] = population
    return india_population_over_years


def plot_india_population_by_years(total_india_population_over_years):
    """
    Plots a bar chart showing India's population over years.

    Args:
        total_india_population_over_years (dict): A dictionary where
        keys are years (str) and values are population (str) for India.
    """
    plt.figure(figsize=(16,6))
    plt.title("India Population Over Years")
    plt.bar(total_india_population_over_years.keys(),
             total_india_population_over_years.values(), color="skyblue")
    plt.xlabel("Years")
    plt.ylabel("Total Population")
    plt.xticks(rotation=90, ha="right")
    plt.yticks(fontsize=6)
    plt.tight_layout()
    plt.show()


def execute():
    """
    Executes the workflow for reading India's population data and
    generating the population bar plot.
    """
    india_population_by_years = calculate_india_population_by_years()
    # print(india_population_by_years)
    plot_india_population_by_years(india_population_by_years)



if __name__ == "__main__":

    execute()
