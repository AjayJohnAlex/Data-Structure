import time
import threading

def calc_square(num_list):
    
    print("Calculating squares.........")
    for i in num_list:
        time.sleep(0.3)
        print(f"Square of {i} -> {i**2}")

def calc_cube(num_list):
    
    print("\n Calculating cubes.........")
    for i in num_list:
        time.sleep(1)
        print(f"Cube of {i} -> {i**3}")

num_list = [1,2,3,4,5,6]
t = time.time()

# NORMAL EXECUTION W/O threading
calc_square(num_list)
calc_cube(num_list)
# time taken : 2.4-2.5 secs, execution sequential -> first rntire squares and then entire cubes
#  for time.sleep(0.2)

print(f"\n Execution Time: {round(time.time() - t,2)} secs ")
# EXECUTION WITH THREAIDNG

time2 = time.time()

# creating the threads
t1 = threading.Thread(target=calc_square, args=(num_list,))
t2 = threading.Thread(target=calc_cube, args=(num_list,))


# Starting the threads
t1.start()
t2.start()

# to ensure that the thread is terminated
t1.join()
t2.join()

print(f"\nExecution Time: {round(time.time() - time2,2)} secs ")
# time taken :1.26 sec and execution sequentionally ,one square, then cube and so on....
#  for time.sleep(0.2)

