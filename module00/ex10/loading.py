import sys
from time import sleep, time

def ft_progress(lst):
    start = time()
    progress_bar_size = 60
    list_len = len(lst)

    def show(progress):
        checked_cells = int(progress_bar_size * progress / list_len)
        elapsed_time = time() - start
        total_time = list_len * elapsed_time / progress if progress > 0 else 0
        eta = total_time - elapsed_time
        print(f"ETA: {eta:.2f}s [{int(progress / list_len * 100)}%][{'=' * checked_cells}>{'.' * (progress_bar_size - checked_cells - 1)}] | elapsed time {elapsed_time:.2f}s     ", end='\r', file=sys.stdout, flush=True)

    show(0)
    for i, item in enumerate(lst):
        yield item
        show(i + 1)
    print("\n", flush=True, file=sys.stdout)


if __name__ == "__main__":
    listy = range(1000)
    ret = 0
    for elem in ft_progress(listy):
        ret += (elem + 3) % 5
        sleep(0.01)
    print()
    print(ret)


    # listy = range(3333)
    # ret = 0
    # for elem in ft_progress(listy):
    #     ret += elem
    #     sleep(0.005)
    # print()
    # print(ret)
