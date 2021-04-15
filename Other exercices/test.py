import argparse

def petla():
    f = open("plik1.txt", "w+")

    for i in range(10):
        f.write("rafal %d\r\n" %(i+1))

    f.close()

p = argparse.ArgumentParser()
p.add_argument('a', help='--filename plik1')
p.add_argument('b', help='--name rafal')
p.add_argument('c', help='--count 10')
argument = p.parse_args()

