#!/usr/bin/python
from multiprocessing import Process,Queue
from random import randint
import time

def printrand():
   #Checks whether Queue is empty and runs
   while q.empty():
      rand = randint(0.100)
      time.sleep(1)
      print(rand)


if __name__ == "__main__":
   #Queue is a data structure used to communicate between process 
   global q
   q = Queue()
   #creating the process
   p = Process(target=printrand)
   #starting the process
   p.start()
   while True:
      ip = input("Write something: ")
      #if user enters stop the while loop breaks
      if ip=="stop":
         #Populating the queue so that printramd can read and quit the loop
         q.put(ip)
         break
   #Block the calling thread until the process whose join() 
   #method is called terminates or until the optional timeout occurs.
   p.join()