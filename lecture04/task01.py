"""
Написать программу, которая считывает список из 10 URL-адресов и
одновременно загружает данные с каждого адреса.
После загрузки данных нужно записать их в отдельные файлы.
Используйте потоки.
Используйте процессы.
"""
import threading
import multiprocessing
import requests
import asyncio


urls = ['https://www.google.com/?hl=ru',
        'https://www.python.org/',
        'https://gb.ru/education',
        'https://ru.wikipedia.org',
        'https://flask.palletsprojects.com/en/2.3.x/']


# def get_urls(url: str, filename: str):
#         response = requests.get(url)
#         with open(f'{filename}', 'w') as f:
#                 f.write(response.text)
#         print(f'{filename} OK')
async def get_urls(url: str, filename: str):
        response = requests.get(url)
        with open(f'{filename}', 'w') as f:
                f.write(response.text)
        print(f'{filename} OK')



# threads = []
# processes = []
tasks = []

# for url in urls:
#         thread = threading.Thread(target=get_urls, args=(url, f'file_{url.split("/")[3]}'))
#         threads.append(thread)
#
# for i, url in enumerate(urls, start=1):
#         process = multiprocessing.Process(target=get_urls, args=(url, f'file_{i}'))
#         processes.append(process)
for i, url in enumerate(urls, start=1):
        task = asyncio.ensure_future(get_urls(url, f'file_{i}'))
        tasks.append(task)
#
# for item in threads:
#         item.start()
# for item in processes:
#         item.start()
loop = asyncio.get_event_loop()
#
# for item in threads:
#         item.join()

# for item in processes:
#         item.join()

loop.run_until_complete(asyncio.wait(tasks))
