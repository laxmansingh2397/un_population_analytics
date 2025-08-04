"""
This module analyzes Population data to calculate and plot
ASEAN Countries Population Over Years.

It reads data from the 'Population.csv' file, processes the
asean countres population of year 2004-2014, and displays the results in a bar chart.
"""
import csv
import matplotlib
from matplotlib import pyplot as plt
from matplotlib.ticker import FuncFormatter
matplotlib.use('Tkagg')


def calculate_asean_countries_population_ten_years():
    """
    Calculates the annual population of each ASEAN country from 2004 to 2014.

    Reads population data from a CSV file and extracts the population for each 
    ASEAN country for every year in the specified range.

    Returns:
        dict: A dictionary where each key is an ASEAN country and each value is 
        a list of populations for the years 2004 to 2014.
    """
    years = list(range(2004, 2015))
    asean_countries_population_ten_years = {"Brunei Darussalam": [0]*len(years),
    "Cambodia": [0]*len(years), "Indonesia": [0]*len(years),
    "Lao PDR": [0]*len(years), "Malaysia": [0]*len(years),
    "Myanmar": [0]*len(years), "Philippines": [0]*len(years),
    "Singapore": [0]*len(years), "Thailand": [0]*len(years), "Vietnam": [0]*len(years)}

    with open("../required_data/country_pop.csv", encoding="utf-8") as country_file:
        country_data = csv.DictReader(country_file)

        for countries in country_data:
            country = countries["country"]
            year = int(countries["year"])
            population = int(countries["population"])

            if country in asean_countries_population_ten_years:
                if year in years:
                    index = years.index(year)
                    asean_countries_population_ten_years[country][index] = population

    return asean_countries_population_ten_years


def plot_asean_countries_population_ten_years(asean_countries_population):
    """
    Plots a grouped bar chart for annual population of each ASEAN country from 2004 to 2014.

    Args:
        asean_countries_population (dict): Dictionary with country names as keys and lists of annual
                                           populations as values.
    """
    years = list(range(2004, 2015))
    countries = list(asean_countries_population.keys())
    n_countries = len(countries)
    bar_width = 0.8 / n_countries
    x = list(years)
    plt.figure(figsize=(14, 6))

    for i, country in enumerate(countries):
        x_country = [val + i * bar_width for val in x]
        plt.bar(x_country, asean_countries_population[country], width=bar_width, label=country)

    plt.xlabel("Year")
    plt.ylabel("Total Population")
    plt.title("ASEAN Country Population (2004-2014)")
    plt.xticks([val + bar_width * (n_countries / 2 - 0.5)
               for val in x], years, rotation=45)
    plt.gca().yaxis.set_major_formatter(FuncFormatter(lambda x, _: f'{x:,.0f}'))
    plt.legend(title="Country", bbox_to_anchor=(1.05, 1), loc="upper left")
    plt.tight_layout()
    plt.show()


def execute():
    """
    Runs the population calculation and plotting for ASEAN countries (2004–2014).
    """
    asean_countries_population_ten_years = calculate_asean_countries_population_ten_years()
    plot_asean_countries_population_ten_years(asean_countries_population_ten_years)


if __name__ == "__main__":

    execute()
