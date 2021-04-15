import argparse


def main():
    parser = argparse.ArgumentParser(description='opis skryptu')
    parser.add_argument("--filename", help="Nazwa tworzonego pliku", type=str, dest="filename", required=True)
    parser.add_argument("--name", help="Linia tekstu która ma zostać napisana w pliku", type=str, dest="name", required=True)
    parser.add_argument("--count", help="Liczba linii tekstu", type=int, required=True)

    args = parser.parse_args()

    amount = int(args.count)
    title = str(args.filename)
    content = args.name

    make(amount,title,content)



def make(amount,title,content):


    print("Great you called your file!")
    new = open(title, encoding='utf-8', mode='w')
    print("Congratulations, you have chosen how many lines will be in your file")
    for i in range(amount):
        new.write(content+"\n")
print("Fantastic, you've done")



main()
