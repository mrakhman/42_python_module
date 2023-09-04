import matplotlib.pyplot as plt
from load_csv import load
import pandas as pd


def _guard_(func):
    '''Prevents throwing error in console'''
    def wrapper(*args, **kwargs):
        try:
            return (func(*args, **kwargs))
        except Exception as e:
            print(e)
            return None
    return wrapper


def projection_life():
    '''Display projection of life expectancy
     in relation to the gross domestic product'''
    df_life_expectancy = load('../life_expectancy_years.csv')
    df_gdp = load(
        '../income_per_person_gdppercapita_ppp_inflation_adjusted.csv')

    # Prepare data
    new_life_expectancy = df_life_expectancy[['country', '1900']]
    new_df = pd.concat([new_life_expectancy, df_gdp['1900']], axis=1)
    new_df.columns = ['country', 'life_expectancy', 'gdp']
    new_df = new_df.dropna()

    # Set graph title
    _, ax = plt.subplots()
    ax.set_title('Year 1900')

    # Set axis labels
    plt.xlabel('Gross domestic product')
    plt.ylabel('Life expectancy')

    # # Plot and show
    plt.scatter(new_df['gdp'], new_df['life_expectancy'])
    plt.legend(['gdp by life expectancy'], loc='lower right')
    plt.show()


@_guard_
def main():
    '''Main for tests and error handling'''
    projection_life()


if __name__ == "__main__":
    main()
