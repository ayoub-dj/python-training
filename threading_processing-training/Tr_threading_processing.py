from time import sleep
from threading import Thread, current_thread
from multiprocessing import Process, current_process

def process_one(name):
    print(f"Starting process one: {name}")
    
    def threading_one():
        current_thread_name = current_thread().name
        print(f"Starting thread: {current_thread_name}")
        
        for i in range(1, 5):
            print(f"{i} Thread from process one ({current_thread_name})")
            sleep(1)

    def threading_two():
        current_thread_name = current_thread().name
        print(f"Starting thread: {current_thread_name}")
        
        for i in range(1, 5):
            print(f"{i} Thread from process one ({current_thread_name})")
            sleep(1)

    threading_1 = Thread(target=threading_one, name='Thread_One')
    threading_2 = Thread(target=threading_two, name='Thread_Two')

    threading_1.start()
    threading_2.start()

    threading_1.join()
    threading_2.join()

def process_two(name):
    print(f"Starting process two: {name}")
    
    def threading_one():
        current_thread_name = current_thread().name
        print(f"Starting thread: {current_thread_name}")
        
        counter = 5
        while counter > 0:
            print(f"{counter} Thread from process two ({current_thread_name})")
            sleep(1)
            counter -= 1

    threading_1 = Thread(target=threading_one, name='Thread_One')

    threading_1.start()
    threading_1.join()

if __name__ == '__main__':
    try:
        process_1 = Process(target=process_one, args=("process_one",))
        process_2 = Process(target=process_two, args=("process_two",))

        process_1.start()
        process_2.start()

        process_1.join()
        process_2.join()

    except Exception as e:
        print(f"An error occurred: {e}")
