import argparse
import re
import os
import wget


def main():
    p = argparse.ArgumentParser(description="Script using to looking for extended files")
    p.add_argument("--log_name", help="name files where is extended files", dest="log_name", required=True)
    p.add_argument("--directory", help="name folder where will be downloading files", dest="directory", required=True)

    args = p.parse_args()

    log = args.log_name
    direct = args.directory

    look_for(log, direct)


def look_for(log, direct):
    list = []
    with open(log, 'r') as f1:
        for line in f1.readlines():
            list.append([line])
            for i in line.split(","):
                list[-1].append(i)
                #print(i)
                urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', i)
                listToString = ' '.join([str(elem) for elem in urls])
                print(listToString)
                directory = os.mkdir(direct)
                x = os.getcwd()
                os.chdir(direct)
                y = os.getcwd()
                if(".rpm" in listToString):
                    wget.download(listToString, y)








main()
