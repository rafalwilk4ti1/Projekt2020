import argparse
import os
import webbrowser
import requests
import wget

def main():
    parser = argparse.ArgumentParser(description='Browser a text file to find downloaded files from file log ')
    parser.add_argument('-ln', '--logname', type=str, metavar= '', required = True, help = 'Name of the file')
    parser.add_argument('-d', '--directory', type=str, metavar= '', required = True, help = 'Name of the directory which we will put the downloaded files')
    parser.add_argument('-dfn', '--duplicate_file_name', type=str, metavar = '', required = True, help = 'Check if the current file is downloaded')
    args = parser.parse_args()

    file = args.logname
    directory = args.directory
    duplicate = args.duplicate_file_name

    real_file = read_file(file)
    finding = finding_rwt(real_file)
    i = selection_files(finding)
    p = list_of_duplicates(finding)
    type_duplicates__in_file(p, duplicate)
    download(i, directory)


def read_file(file):
    log_name = open(file, 'r')
    var = log_name.readlines()
    var2 = str(var)
    return var2

def finding_rwt(read_file):
    var3 = read_file
    lista = var3.split()
    lista.sort()
    clear_lista = []
    for x in lista:
        if x.endswith(".rpm") or x.endswith(".whl") or x.endswith("tar.gz"):
            clear_lista.append(x)

    return clear_lista

def selection_files(clear_lista):
    duplicates = []
    for duplicate in clear_lista:
        duplicates.append(duplicate)
    for y in duplicates:
        if y in duplicates and duplicates.count(y) != 1:
            clear_lista.remove(y)

    return clear_lista

def list_of_duplicates(clear_lista):
    duplicates = []
    for i in clear_lista:
        duplicates.append(i)
    for x in clear_lista:
        if x in clear_lista and clear_lista.count(x) > 1:
            duplicates.append(x)

    return duplicates

def type_duplicates__in_file(duplicates,duplicate_file_name):
    file = open(duplicate_file_name, "w")
    for x in duplicates:
        file.write(x)
    file.close()


def download(list_of_files, directory):
    os.mkdir(directory)
    directory = os.getcwd()
    active = True
    while active:
        for http in list_of_files:
            wget.download(http,directory)

    active = False


main()





