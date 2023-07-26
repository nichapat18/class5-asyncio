#1-1-simple-sync.py

import time     # import time module

# การสร้าง function
def sleep():    
    print(f'Time: {time.time() - start:.2f}')
    time.sleep(1)   # sleep for 1 second

# เป็นการ รวมผลรวม name กับ number
def sum(name, numbers):
    total = 0
    for number in numbers:
        print(f'Task {name} : Computing {total} + {number}')
        sleep()
        total += number
    print(f'Task {name}: Sum = {total}\n ')

#จุดเริ่มต้น
start = time.time()

#เป็นการดำเนินงานบวกตัวเลข
tasks = [
    sum("A", [1, 2]),
    sum("B", [1, 2, 3])
]
# เป็นการเอา start and end มาประมวลผล
end = time.time()
print(f'Time: {end-start:.2f} sec')