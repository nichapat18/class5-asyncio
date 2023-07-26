#Class2.3-basic-gather-more.py

#import module 
import asyncio
import time

# สร้าง function hello
async def hello(i):
    print(f"{time.ctime()} hello {i} started")

    await asyncio.sleep(4)  # sleep for 4 seconds
    print(f"{time.ctime()} hello {i} done")

#สร้าง main function
async def main():
    coros = [hello(i) for i in range(10)]
    await asyncio.gather(*coros)        # execute multiple coroutines

if __name__ == '__main__':  # สามารถเลือกรันที่ต้องการได้
    start = time.time()   # Time start
    asyncio.run(main())   # Main function
    end = time.time()     #Time end
    print(f'Time: {end-start:.2f} sec')