import logging
import threading
import time
from multiprocessing import Process

tickets_1 = ["000000", "250000"]
tickets_2 = ["250001", "500000"]
tickets_3 = ["500001", "750000"]
tickets_4 = ["750001", "999999"]

total_tickets = 0


def check_ticket(ticket):
    start = ticket[0]
    end = ticket[1]
    lucky = 0
    logging.info("Thread %s: starting", threading.currentThread().name)

    for num in range(int(start), int(end) + 1):
        i = str(num).rjust(6, "0")
        if (int(i[0]) + int(i[1]) + int(i[2])) == (int(i[3]) + int(i[4]) + int(i[5])):
            lucky += 1

    logging.info("Thread %s: finishing", threading.currentThread().name)

    print(f"{threading.currentThread().name} - {lucky} tickets")

    global total_tickets
    total_tickets += lucky


if __name__ == '__main__':
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    logging.info("Main: before creating thread")
    # thread1 = threading.Thread(target=check_ticket, args=(tickets_1,))
    # thread2 = threading.Thread(target=check_ticket, args=(tickets_2,))
    # thread3 = threading.Thread(target=check_ticket, args=(tickets_3,))
    # thread4 = threading.Thread(target=check_ticket, args=(tickets_4,))

    process1 = Process(target=check_ticket, args=(tickets_1,))
    process2 = Process(target=check_ticket, args=(tickets_2,))
    process3 = Process(target=check_ticket, args=(tickets_3,))
    process4 = Process(target=check_ticket, args=(tickets_4,))

    logging.info("Main: before running thread")
    beginning_time = time.time()
    print(f"Begin threads {beginning_time}")

    # thread1.start()
    # thread2.start()
    # thread3.start()
    # thread4.start()

    process1.start()
    process2.start()
    process3.start()
    process4.start()

    logging.info("Main: wait for the thread to finish")

    # thread1.join()
    # thread2.join()
    # thread3.join()
    # thread4.join()

    process1.join()
    process2.join()
    process3.join()
    process4.join()

    ending_time = time.time()
    print(f"End threads {ending_time}")
    logging.info("Main: all done")

    print("Total lucky tickets: ", total_tickets)
    print(f"Spent time: {ending_time - beginning_time}")
