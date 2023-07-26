#Class 1-2-simple-async-wrong.py

# import module ขึ้นมา
import asyncio
import time

#suspend execution of calling thread for however many second
async def sleep():
    print(f'Time: {time.time() - start:.2f}')
    time.sleep

#การคำนวน name and numbers
async def sum(name, numbers):
    total = 0
    for number in numbers:       
        print(f'task {name}: Computing {total}+{number}')  #
        await sleep()
        total += number
    print(f'Task {name}: Sum = {total}\n')

#execute the script the s
start = time.time()
loop = asyncio.get_event_loop()
tasks = [
    #schedule the execution of coroutine coro
    loop.create_task(sum("A", [1, 2])),
    loop.create_task(sum("B", [1, 2, 3])),
    ]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

#เมื่อคำนวนเสร็จแล้วก็นำมาลบกันในขั้นสุดท้าย
end = time.time()
print(f'Time: {end-start:.2f} sec') # แสดงผลลัพธ์ ขึ้นสุดท้ายออกมา