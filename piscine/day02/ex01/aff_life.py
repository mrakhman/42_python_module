import seaborn as sns
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
    # plt.plot(df.country, df['1800'])
    # plt.show()

    # print(df.loc[df.country == 'France'].T)
    # new_df = df.loc[df.country == 'France']
    # print(new_df[0])
    # print(new_df.iloc[:[0]].values.flatten().tolist(),
    #       new_df.iloc[:[1]].values.flatten().tolist())

    print(df.loc[df.country == 'France'])

    new_df = df.loc[df.country == 'France'].drop(columns=['country']).T
    new_df.columns = ['France']
    new_df.index = new_df.index.astype(int)
    plt.plot(new_df.France)
    # print(new_df, new_df.France)
    plt.show()

    # Seaborn load dataset
    # years = sns.load_dataset(df)
    # Create visualization
    # sns.relplot(
    #     data=df
    # )


@_guard_
def main():
    '''Main for tests and error handling'''
    aff_life()


if __name__ == "__main__":
    main()
