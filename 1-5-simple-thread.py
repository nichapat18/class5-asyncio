#Class 1-5-simple-thread.py

# import module
import asyncio
import time

from concurrent.futures.thread import ThreadPoolExecutor

def sleep():       #สร้าง class function 
    print(f'Time: {time.time() - start:.2f}')
    time.sleep(1)
# จำลองการทำงาน

async def sum(name, numbers):
    _executor = ThreadPoolExecutor(2) # สร้างthread ที่มี 2 tasks ขึ้นมา
    total = 0
    for number in numbers:
        #นำตัวเลขมาบวกกันจนกว่าจะครบ loop แล้วแสดงค่า
        print(f'Task {name}: Computing {total}={number}')
        await loop.run_in_executor(_executor, sleep) # เรียก function async await เพื่อให้ทำงานอื่นขณะsleep ทำงานอยู่
        total = 0
    print(f'Task {name}: Sum = {total}\n')

start = time.time()
loop = asyncio.get_event_loop()  # สร้าง loop ขึ้นมาเพื่อรับค่า
tasks = [
    loop.create_task(sum("A", [1, 2])),
    loop.create_task(sum("B", [1, 2, 3])),
]
loop.run_until_complete(asyncio.wait(tasks))     # ทำงานจนครบ loop จนเสร็จ
loop.close()

end = time.time()
print(f'Time: {end-start:.2f} sec')