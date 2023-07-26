#3-basic-fac.py

#import module
import asyncio
import time

# Computing factorial(2), currently i=2 ...
# Computing factorial(3), currently i=2 ...
# Computing factorial(4), currently i=2 ...
# Computing factorial(3), currently i=3 ...
# Computing factorial(4), currently i=3 ...
# Computing factorial(4), currently i=4 ...
# [2, 6, 24]
# Time: 3.03 sec

#สร้าง factorial 
async def factorial(n):
    f = 1
    for i in range(2, n+1):
        print(f'Computing factorial({n}), currently i={i} ...')   
        await asyncio.sleep(1)  # sleep for 1 second
        f *= i
    return f

#สร้าง class main 
async def main():
    L = await asyncio.gather(factorial(2), factorial(3), factorial(4))
    print(L)  # [2,6,24]

# สร้างเวลาที่กำหนดทั้งหมด
if __name__ == '__main__':  # สามารถเลือกรันที่ต้องการได้
    start = time.time()
    asyncio.run(main())  # run main function
    end = time.time()    # time end
    print(f'Time: {end-start:.2f} sec')