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


Dataset = pd.core.frame.DataFrame


def load(path: str) -> Dataset:
    '''Loads and returns dataset from a given path'''
    try:
        df = pd.read_csv(path)
        print('Loading dataset of dimensions', df.shape)
        return df
    except Exception:
        print('Error: Unable to load file')
        return None


@_guard_
def main():
    '''Main for tests and error handling'''
    # print(load('../life_expectancy_years.csv'))
    pass


if __name__ == "__main__":
    main()
