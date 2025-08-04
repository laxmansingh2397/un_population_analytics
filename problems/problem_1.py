import csv
import matplotlib
matplotlib.use('Tkagg')
from matplotlib import pyplot as plt

def calculate_india_population_by_years():
    
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
    
    plt.figure(figsize=(16,6))
    plt.title("India Population Over Years")
    plt.bar(total_india_population_over_years.keys(), total_india_population_over_years.values(), color="skyblue")
    plt.xlabel("Years")
    plt.ylabel("Total Population")
    plt.xticks(rotation=90, ha="right")
    plt.yticks(fontsize=6)
    plt.tight_layout()
    plt.show()


def execute():

    india_population_by_years = calculate_india_population_by_years()
    # print(india_population_by_years)
    plot_india_population_by_years(india_population_by_years)



if __name__ == "__main__":

    execute()
