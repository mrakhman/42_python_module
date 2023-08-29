import sys
from time import sleep, time
# from tqdm import tqdm


def _guard_(func):
    '''Prevents throwing error in console'''
    def wrapper(*args, **kwargs):
        try:
            return (func(*args, **kwargs))
        except Exception as e:
            print(e)
            return None
    return wrapper


def ft_tqdm(lst: range) -> None:
    '''Creates progressbar for a given list'''
    start = time()
    progress_bar_size = 60
    list_len = len(lst)

    def show(progress):
        checked_cells = int(progress_bar_size * progress / list_len)
        elapsed_time = time() - start
        total_time = list_len * elapsed_time / progress if progress > 0 else 0
        eta = total_time - elapsed_time
        iterations_per_second = progress / elapsed_time

        print(f"{int(progress / list_len * 100)}%|\
{'█' * checked_cells}{' ' * (progress_bar_size - checked_cells - 1)}| \
{progress}/{list_len} \
[{elapsed_time / 60:.2f}<{eta / 60:.2f}, {iterations_per_second:.2f}it/s]\
", end='\r', file=sys.stdout, flush=True)

    show(0)
    for i, item in enumerate(lst):
        yield item
        show(i + 1)
    print("\n", flush=True, file=sys.stdout)


@_guard_
def main():
    '''Main for tests and error handling'''
    for elem in ft_tqdm(range(333)):
        sleep(0.005)
    print()

    # for elem in tqdm(range(333)):
    #     sleep(0.005)
    # print()


if __name__ == "__main__":
    main()
