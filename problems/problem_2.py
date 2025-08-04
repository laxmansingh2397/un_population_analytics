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
    
    asean_countries_population_2014 = {"Brunei Darussalam": "", "Cambodia" : "", "Indonesia" : "", "Lao PDR" : "", "Malaysia" : "", "Myanmar" : "", "Philippines" : "", "Singapore" : "", "Thailand" : "", "VietNam" : ""}

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
    
    plt.figure(figsize=(14,6))
    plt.title("ASEAN Countries Population In 2014")
    plt.bar(asean_countries_population.keys(), asean_countries_population.values(), color="blue")
    plt.xlabel("ASEAN Countries")
    plt.ylabel("Total Population")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()


def execute():

    asean_countries_population = calculate_asean_countries_population_in_2014()
    # print(asean_countries_population)
    plot_asean_countries_population_in_2014(asean_countries_population)


if __name__ == "__main__":

    execute()
