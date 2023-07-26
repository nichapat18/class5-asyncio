# Class 1-4 simple-async-right2.py

# import module 
import asyncio
import time             #import time module

#สร้าง Class sleep
async def sleep():                      
    print(f'Time: {time.time() - start:.2f}')    # suspend execution of calling thread for 1 second
    await asyncio.sleep(1)

#คำนวน name and number
async def sum(name, numbers):
    total = 0
    for number in numbers:
        print(f'Task{name}: Computing {total}+{number}')    #นำตัวเลขมาบวกกันจนกว่าจะครบ loop แล้วแสดงค่า
        await sleep()
        total += number
    print(f'Task {name}: Sum = {total}\n')

# สร้าง function main 
async def main():
    await asyncio.gather(sum("A", [1, 2]), sum("B", [1, 2, 3]))  # การเรียกใช้งานหลายอันพร้อมกัน

if __name__ == '__main__':     # สามารถเลือกรันที่ต้องการได้
    start = time.time()        # Time start
    asyncio.run(main())        #  run main function
    end = time.time()          # Time end
    print(f'Time: {end-start:.2f} sec')     # คำนวนเสร็จแล้วนำมาลบในขั้นสุดท้าย    