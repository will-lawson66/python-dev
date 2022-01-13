import multiprocessing
import os
import time

def worker_main(queue):
    print(os.getpid(),"working")
    while True:
        item = queue.get(block=True) #block=True means make a blocking call to wait for items in queue
        if item is None:
            break

        print(os.getpid(), "got", item)
        time.sleep(5) # simulate a "long" operation


def main():
    the_queue = multiprocessing.Queue()
    the_pool = multiprocessing.Pool(3, worker_main,(the_queue,))
            
    for i in range(12):
        the_queue.put("hello")
        the_queue.put("world")
    
    for i in range(3):
        the_queue.put(None)

    # prevent adding anything more to the queue and wait for queue to empty
    the_queue.close()
    the_queue.join_thread()

    # prevent adding anything more to the process pool and wait for all processes to finish
    the_pool.close()
    the_pool.join()

if __name__ == '__main__':
    main()