# SHA1 Hash breaker
Blockchain Assignment 2 - Georgia State University

This is a python code that breaks a given SHA1 by making a brute force attack that reads through an exhaustive list of common passwords.

## Installation

Use the package manager [python](https://www.python.org/downloads/) to install python 2.7.

## Run

Question a and b : 
<Input: Hash that has to be broken>
```bash
>>[path to python.exe] break_hash.py b7a875fc1ea228b9061041b7cec4bd3c52ab3ce3

Input Hash is : b7a875fc1ea228b9061041b7cec4bd3c52ab3ce3
Hash Value : letmein
Time Taken : 0.144999980927
Number of Attempts: 16

>>[path to python.exe] break_hash.py 801cdea58224c921c21fd2b183ff28ffa910ce31

Input Hash is : 801cdea58224c921c21fd2b183ff28ffa910ce31
Hash Value : vjhtrhsvdctcegth
Time Taken : 1.65599989891
Number of Attempts: 999968


```

Question c :
<Input: Salt, Hash that has to be broken>

```bash
>>[path to python.exe] break_hash.py f0744d60dd500c92c0d37c16174cc58d3c4bdd8e ece4bb07f2580ed8b39aa52b7f7f918e43033ea1

Salt Term :  f0744d60dd500c92c0d37c16174cc58d3c4bdd8e
Passowrd Hash : ece4bb07f2580ed8b39aa52b7f7f918e43033ea1
Hash Value : harib
Time Taken : 1.30200004578
Number of Attempts: 546588


```
