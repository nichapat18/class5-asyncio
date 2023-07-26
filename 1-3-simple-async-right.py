#Class 1-3-simple-async-right.py

#import module
import asyncio
import time

# suspend execution of calling thread for 1 second
async def sleep():
    print(f'Time: {time.time() - start:.2f}') 
    await asyncio.sleep(1) 

# คำนวน name and numbers
async def sum(name, numbers):
    total = 0
    for number in numbers:
        print(f'task {name}: Computing {total}+{number}')    #นำตัวเลขมาบวกกันจนกว่าจะครบ loop แล้วแสดงค่า
        await sleep()
        total += number
    print(f'Task {name}: Sum = {total}\n')

#execute the script the time start
start = time.time()

loop = asyncio.get_event_loop()
tasks = [
    # schdule the excution of coroutine coro
    loop.create_task(sum("A", [1, 2])),
    loop.create_task(sum("B", [1, 2, 3])),
]
loop.run_until_complete(asyncio.wait(tasks))  #run untill complete 
loop.close()

# เมื่อคำนวนเสร็จแล้ว นำมาลบในขึ้นสุดท้าย
end = time.time()
print(f'Time: {end-start:.2f} sec')