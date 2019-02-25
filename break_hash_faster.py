import time
import hashlib
from multiprocessing import Pool
import sys
import itertools
import csv

# Question 1 : testing program hash: b7a875fc1ea228b9061041b7cec4bd3c52ab3ce3

# Question 2 : medium hacker hash: 801cdea58224c921c21fd2b183ff28ffa910ce31


def save_hashes_in_file(contents):
    with open("hashes.csv","w") as f:
        f.write('hash,content\n')
        for content in contents:
            f.write(hashlib.sha1(content.strip()).hexdigest()+","+content.strip()+"\n")


def question1_question2(hashes, hash_given):
    count = 0
    for hash in hashes:
        if hash_given in hash:
            hash_value = hash.split(",")[1]
            break
        count += 1

    return hash_value, count

# Question 3 : leet hacker hash: ece4bb07f2580ed8b39aa52b7f7f918e43033ea1




if __name__ == '__main__':
    start = time.time()
    hash_value = ""
    count = ""
    # with open('dict.txt', 'r') as f:
    #     contents = f.readlines()
    with open('hashes.csv','r') as f:
        hashes = f.readlines()
    # save_hashes_in_file(contents)
    if len(sys.argv) == 1:
        print("Invalid Arguments")
        exit(0)
    else:
        if len(sys.argv) == 2:
            print ("Input Hash is : " + sys.argv[1])
            hash_value, count = question1_question2(hashes, sys.argv[1])
    end = time.time()
    print("Hash Value : " + hash_value)
    print("Time Taken : " + str(end - start))
    print("Number of Attempts: " + str(count))



