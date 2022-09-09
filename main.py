import logging
import threading
import time
from multiprocessing import Process, current_process, Queue

tickets_1 = ["000000", "250000"]
tickets_2 = ["250001", "500000"]
tickets_3 = ["500001", "750000"]
tickets_4 = ["750001", "999999"]

# for th
# total_tickets_th = 0


def check_ticket(ticket):
    start = ticket[0]
    end = ticket[1]
    lucky = 0

    # for th
    # logging.info("Thread %s: starting", threading.currentThread().name)

    # # for mp
    print(f"{current_process().name} starting")

    for num in range(int(start), int(end) + 1):
        i = str(num).rjust(6, "0")
        if (int(i[0]) + int(i[1]) + int(i[2])) == (int(i[3]) + int(i[4]) + int(i[5])):
            lucky += 1

    # for th
    # logging.info("Thread %s: finishing", threading.currentThread().name)

    # # for mp
    print(f"{current_process().name} finishing")

    # for th
    # global total_tickets_th
    # total_tickets_th += lucky

    # # for mp

    print(f"Lucky tickets: {lucky}")


if __name__ == '__main__':

    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    # logging.info("Main: before creating thread")
    # thread1 = threading.Thread(target=check_ticket, args=(tickets_1,))
    # thread2 = threading.Thread(target=check_ticket, args=(tickets_2,))
    # thread3 = threading.Thread(target=check_ticket, args=(tickets_3,))
    # thread4 = threading.Thread(target=check_ticket, args=(tickets_4,))

    logging.info("Main: before creating process")
    process1 = Process(target=check_ticket, args=(tickets_1,))
    process2 = Process(target=check_ticket, args=(tickets_2,))
    process3 = Process(target=check_ticket, args=(tickets_3,))
    process4 = Process(target=check_ticket, args=(tickets_4,))

    logging.info("Main: before running thread/process")
    beginning_time = time.time()
    print(f"Begin {beginning_time}")

    # thread1.start()
    # thread2.start()
    # thread3.start()
    # thread4.start()

    process1.start()
    process2.start()
    process3.start()
    process4.start()

    logging.info("Main: wait for the thread/process to finish")

    # thread1.join()
    # thread2.join()
    # thread3.join()
    # thread4.join()

    process1.join()
    process2.join()
    process3.join()
    process4.join()

    ending_time = time.time()
    print(f"End time {ending_time}")
    logging.info("Main: all done")
    print(f"Spent time: {ending_time - beginning_time}")

    # for th
    # print("Total lucky tickets th: ", total_tickets_th)

    # for mp

    # total_tickets_mp = 0
    # while not queue.empty():
    # total_tickets_mp += queue.get()
    # print('item no: ', queue.get())
    # print("Total lucky tickets mp: ", total_tickets_mp)

