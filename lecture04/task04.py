"""
Создать программу, которая будет производить подсчет количества слов
в каждом файле в указанной директории и выводить результаты в консоль.
Используйте потоки.
"""
import threading
import os
# import multiprocessing
import asyncio


# def count_words(file: str):
#     with open(file, 'r') as f:
#         text = f.read()
#         count = len(text.split())
#     print(count)
async def count_words(file: str):
    with open(file, 'r') as f:
        text = f.read()
        count = len(text.split())
    print(count)


# threads = []
# processes = []
tasks = []
files = next(os.walk('../lecture04/'))[2]
files.remove('task04.py')
files.remove('task01.py')
print(files)
#
# for file in files:
#     thread = threading.Thread(target=count_words, args=(file,))
#     threads.append(thread)
# for file in files:
#     process = multiprocessing.Process(target=count_words, args=(file,))
#     processes.append(process)
for file in files:
    task = asyncio.ensure_future(count_words(file))
    tasks.append(task)

# for item in threads:
#     item.start()
# for item in processes:
#     item.start()
loop = asyncio.get_event_loop()
#
# for item in threads:
#     item.join()
# for item in processes:
#     item.join()
loop.run_until_complete(asyncio.wait(tasks))
