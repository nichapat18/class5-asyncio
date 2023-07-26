#Class 2-1-basic-gather.py

#import module
import asyncio
import time

# Output = วันและเวลา hello start/stop 
async def hello(i):
    print(f"{time.ctime()} hello {i} started")
    await asyncio.sleep(4)   # sleep for 4 second
    print(f"{time.ctime()} hello {i} done")

# การสร้าง main และสร้างtask2 ขึ้นมา
async def main():
    task1 = asyncio.create_task(hello(1))
    #await asyncio.sleep(3)
    task2 = asyncio.create_task(hello(2))
    #สร้าง gather เพื่อสร้าง short cut ขึ้นมา
    await asyncio.gather(task1, task2)

#
if __name__ == '__main__':  # สามารถเลือกรันที่ต้องการได้
    start = time.time()    # Time start
    asyncio.run(main())    # run main function
    end = time.time()      #end of time
    print(f'Time: {end-start:.2f} sec') 