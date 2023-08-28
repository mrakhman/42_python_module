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


def normalize_value(val):
    if val[-1] == 'k':
        val = int(float(val[:-1]) * 1000)
        return val
    if val[-1] == 'M':
        val = int(float(val[:-1]) * 1000000)
        return val
    return int(float(val))


def aff_pop():
    '''Display 2 graphics of population: in France and another country'''
    df = load('../population_total.csv')
    country2 = 'Belgium'

    # Prepare data
    new_df = df.loc[df.country.isin([country2, 'France'])].drop(
        columns=['country']).T
    new_df = new_df.iloc[:251]  # untill year 2050
    new_df.columns = [country2, 'France']
    # years column to type int for x-axis ticks
    new_df.index = new_df.index.astype(int)
    new_df['France-int'] = new_df.France.map(normalize_value)
    country2_col_name = country2 + '-int'
    new_df[country2_col_name] = new_df[country2].map(normalize_value)

    # pd.set_option('display.max_rows', None)
    # print(new_df)

    # Set graph title
    _, ax = plt.subplots()
    ax.set_title('Population projections')

    # Set axis labels
    plt.xlabel('Year')
    plt.ylabel('Population')

    # Set ticks for y-axis
    plt.yticks(ticks=new_df['France-int'], labels=new_df['France'])
    plt.locator_params(axis='y', nbins=5)

    # Plot and show
    plt.plot(new_df['France-int'], label='France')
    plt.plot(new_df[country2_col_name], label=country2)
    plt.legend(loc="upper left")
    plt.show()


@_guard_
def main():
    '''Main for tests and error handling'''
    aff_pop()


if __name__ == "__main__":
    main()
