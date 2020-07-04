"""
Multiprocessing will be helpful for CPU based operations
"""

import time
import multiprocessing
import concurrent.futures

start = time.perf_counter()


def do():
    print('Sleeping 1 second...')
    time.sleep(1)
    print('Done Sleeping...')


def do_with_args(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    print(f'Done Sleeping...{seconds}')


def do_with_args_and_return(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return f'Done Sleeping...{seconds}'

# # This will just run the do function without any Multiprocessing
# do()
# do()


# # This is the basic Multiprocessing concept (Manual way to do the task)
# p1 = multiprocessing.Process(target=do)
# p2 = multiprocessing.Process(target=do)

# p1.start()
# p2.start()

# p1.join()
# p2.join()

# processes = []

# for _ in range(10):
#     t = multiprocessing.Process(target=do_with_args, args=[2])
#     t.start()
#     processes.append(t)

# for process in processes:
#     process.join()


with concurrent.futures.ProcessPoolExecutor() as executor:
    # f1 = executor.submit(do_with_args, 2)
    # f2 = executor.submit(do_with_args, 1)

    # results = [executor.submit(do_with_args, 2) for _ in range(10)]

    secs = [5, 4, 3, 2, 1]
    results = [executor.submit(do_with_args, sec) for sec in secs]

    # results = [executor.submit(do_with_args_and_return, sec) for sec in secs]
    # for f in concurrent.futures.as_completed(results):
    #     print(f.result())

    # results = executor.map(do_with_args_and_return, secs)
    # for result in results:
    #     print(result)


finish = time.perf_counter()
print(f'Finished in {round(finish-start, 2)} second(s)')
