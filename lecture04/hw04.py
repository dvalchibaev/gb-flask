import json
import os
import requests
import sys
import threading
import multiprocessing
import asyncio
import time

"""
Написать программу, которая скачивает изображения с заданных URL-адресов и сохраняет их на диск. 
Каждое изображение должно сохраняться в отдельном файле, название которого соответствует 
названию изображения в URL-адресе.
Например, URL-адрес: https://example/images/image1.jpg -> файл на диске: image1.jpg
— Программа должна использовать многопоточный, многопроцессорный и асинхронный подходы.
— Программа должна иметь возможность задавать список URL-адресов через аргументы командной строки.
— Программа должна выводить в консоль информацию о времени скачивания каждого изображения 
    и общем времени выполнения программы.
"""


def parse_image(image_url: str, dir='', method='sync'):
    start_time = time.time()
    response = requests.get(image_url)
    file_name = image_url.split('/')[-1]
    if response.status_code == 200:
        with open(f'{dir}/{file_name}', 'wb') as image:
            image.write(response.content)
    else:
        print(f'Bad parse on {image_url}')
    print(f'({method=}) timing for image {file_name} is {time.time() - start_time}')


async def parse_image_async(image_url: str, dir=''):
    parse_image(image_url, dir=dir, method='async')


if __name__ == '__main__':
    args = sys.argv
    for i in ('threads', 'processes', 'async'):
        if not os.path.exists(f'output_images_{i}'):
            os.mkdir(f'output_images_{i}')
    if len(args) > 1:
        image_urls = args[1:]
    else:
        with open('images_urls.json', 'r') as f:
            image_urls = json.load(f)

    print('Doing threads...')
    start_time = time.time()
    threads = []

    for name in image_urls:
        thread = threading.Thread(target=parse_image, args=(name,),
                                  kwargs=({'dir': 'output_images_threads',
                                           'method': 'threads'}))
        threads.append(thread)

    for item in threads:
        item.start()

    for item in threads:
        item.join()

    print(f'Threads stopped. Total time: {time.time() - start_time}')

    print('Doing async...')
    start_time = time.time()
    tasks = []

    for name in image_urls:
        task = asyncio.ensure_future(parse_image_async(name, dir='output_images_async'))
        tasks.append(task)

    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))

    print(f'Async stopped. Total time: {time.time() - start_time}')

    print('Doing processes...')
    start_time = time.time()
    processes = []

    for name in image_urls:
        process = multiprocessing.Process(target=parse_image, args=(name,),
                                          kwargs=({'dir': 'output_images_processes',
                                                   'method': 'processes'}))
        processes.append(process)

    for item in processes:
        item.start()

    for item in threads:
        item.join()

    print(f'Processes stopped. Total time: {time.time() - start_time}')