#import mudule
import asyncio
import time

# Output = วันและเวลา hello start/stop 
async def hello(i):
    print(f"{time.ctime()} hello {i} started")
    await asyncio.sleep(4)   #sleep for 4 seconds
    print(f"{time.ctime()} hello {i} done")

# สร้าง main function
async def main():
    task1 = asyncio.create_task(hello(1)) # returns immediately,  the task is created
    #await asyncio.sleep(3)
    task2 = asyncio.create_task(hello(2))
    await task1
    await task2

#สร้างเวลาที่กำหนดทั้งหมด
if __name__ == '__main__':  # สามารถเลือกรันที่ต้องการได้
    start = time.time()    # time start
    asyncio.run(main())    # run main function
    end = time.time()      # end of time
    print(f'Time: {end-start:.2f} sec')  #เมื่อคำนวนเสร็จแล้วให้นำค่ามาลบกันในขั้นสุดท้าย