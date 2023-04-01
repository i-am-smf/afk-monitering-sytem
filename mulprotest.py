import multiprocessing

def prnt_cu(n):
    for i in range(200,400,1):
        print(i)

def prnt_squ(n):
    for j in range(1,200,1):
        print(j)

if __name__ == "__main__":

    proc1 = multiprocessing.Process(target=prnt_squ, args=(5, ))
    proc2 = multiprocessing.Process(target=prnt_cu, args=(5, ))

    proc1.start()
    proc2.start()

    proc1.join()
    proc2.join()

    print("Both Processes Completed!")