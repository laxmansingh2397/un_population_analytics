"""
This module analyzes Population data to calculate and plot
SAARC Countries Population Over Years.

It reads data from the 'Population.csv' file, processes the
saarc countries population over years, and displays the results in a bar chart.
"""
import csv
import matplotlib
from matplotlib import pyplot as plt
from matplotlib.ticker import FuncFormatter
matplotlib.use('Tkagg')


def calculate_saarc_countries_population_over_years():
    """
    Calculates the total population of all SAARC countries for each year from 1960 to 2023.

    Reads from a CSV file containing country, year, and population columns, and sums the population
    for defined SAARC countries per year.

    Returns:
        list: A list where each element is the total SAARC population
        for a given year (from 1960 to 2023).
    """
    years = list(range(1960, 2024))
    saarc_countries_population_over_years = {"India": [0]*len(years),
    "Maldives": [0]*len(years), "Bhutan": [0]*len(years), "Sri Lanka": [0]*len(
    years), "Nepal": [0]*len(years), "Afghanistan": [0]*len(years),
    "Bangladesh": [0]*len(years), "Pakistan": [0]*len(years)}

    with open("../required_data/country_pop.csv", encoding="utf-8") as country_file:
        country_data = csv.DictReader(country_file)

        for countries in country_data:
            year = int(countries["year"])
            country = countries["country"]
            population = countries["population"]

            if country in saarc_countries_population_over_years:
                if year in years:
                    index = years.index(year)
                    saarc_countries_population_over_years[country][index] = int(
                    population)
    total_population_per_year_saarc_countries = []

    for year in range(len(years)):
        year_sum = sum(
        saarc_countries_population_over_years[country][year] for country in saarc_countries_population_over_years)

        total_population_per_year_saarc_countries.append(year_sum)

    return total_population_per_year_saarc_countries


def plot_saarc_countries_population_over_years(saar_countries_population):
    """
    Plots a bar chart of the total SAARC countries' population
    over years using actual population numbers on the y-axis.

    Args:
        saar_countries_population (list): List of total SAARC population
        for each year (from 1960 to 2023).
    """
    years = list(range(1960,2024))
    plt.figure(figsize=(14,6))
    plt.title("SAARC Counties Population Over Years")
    plt.bar(years, saar_countries_population, color="yellow")
    plt.xlabel("Years")
    plt.ylabel("Total Population")
    plt.xticks(rotation=45, ha="right")
    plt.gca().yaxis.set_major_formatter(FuncFormatter(lambda x, _: f'{x:,.0f}'))
    plt.tight_layout()
    plt.show()


def execute():
    """
    Executes the process: calculates and plots the SAARC countries' total population over years.
    """
    saarc_countries_population_over_years = calculate_saarc_countries_population_over_years()
    plot_saarc_countries_population_over_years(saarc_countries_population_over_years)


if __name__ == "__main__":

    execute()
