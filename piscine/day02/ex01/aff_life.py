import matplotlib.pyplot as plt
from load_csv import load


def _guard_(func):
    '''Prevents throwing error in console'''
    def wrapper(*args, **kwargs):
        try:
            return (func(*args, **kwargs))
        except Exception as e:
            print(e)
            return None
    return wrapper


def aff_life():
    '''Shows graphic of life expectancy in France'''
    df = load('../life_expectancy_years.csv')

    # Matplotlib
    # Prepare data
    new_df = df.loc[df.country == 'France'].drop(columns=['country']).T
    new_df.columns = ['France']
    # Change years column to type int for round up
    new_df.index = new_df.index.astype(int)

    # Set graph title
    _, ax = plt.subplots()
    ax.set_title('France life expectancy projections')

    # Set axis labels
    plt.xlabel('Year')
    plt.ylabel('Life expectancy')

    # Plot and show
    plt.plot(new_df.France)
    plt.show()


@_guard_
def main():
    '''Main for tests and error handling'''
    aff_life()


if __name__ == "__main__":
    main()
