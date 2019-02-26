import time
import hashlib
from multiprocessing import Pool
import sys
import itertools


# Question 4 : graduate student: 34302959e138917ce9339c0b30ec50e650ce6b40
with open('dict.txt', 'r') as f:
    contents = f.readlines()
count = 0

contents = contents[300000:700000]


def brute_force(content):
    global count
    hash = "34302959e138917ce9339c0b30ec50e650ce6b40"
    dict = {}
    key1 = str(content.strip())
    for key2 in contents:
        key2_str=str(key2).strip()
        calculated_hash = (hashlib.sha1(key1+ " "+key2_str).hexdigest())
        if calculated_hash == hash:
            print("---------------------" + key1.strip()+" "+ key2_str.strip()+"--------------------")
            with open('found.txt', 'w') as f:
                f.write("---------------------" + key1.strip()+" "+ key2_str.strip()+"--------------------")
        calculated_hash = (hashlib.sha1(key2_str + " " + key1).hexdigest())
        if calculated_hash == hash:
            print("---------------------" + key2_str.strip() + " " + key1.strip() + "--------------------")
            with open('found.txt', 'w') as f:
                f.write("---------------------" + key2_str.strip() + " " + key1.strip() + "--------------------")
    count = count + 1


if __name__ == '__main__':
    start = time.time()
    if len(sys.argv) == 1:
        print("Invalid Arguments")
        exit(0)
    else:
        if len(sys.argv) == 2:
            print ("Input Hash is : " + sys.argv[1])
            pool = Pool()
            result = pool.map(brute_force, contents)
            pool.terminate()
    end = time.time()
    print("Hash Value : " + "If present can be found in found.txt generated in the workspace")
    print("Time Taken : " + str(end - start))
    print("Number of Attempts: " + str(count))
