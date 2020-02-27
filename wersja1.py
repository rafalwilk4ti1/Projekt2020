import argparse


def wewnetrzna(dane1,dane2,dane3):
    plik = open(dane1, encoding='utf-8', mode='w')

    for i in range(int(dane3)):
        plik.write(dane2+"\n")
    plik.close()



def glowna():
    parser = argparse.ArgumentParser(description='opis skryptu')
    parser.add_argument("filename", action="store_true", help="Nazwa tworzonego pliku")
    parser.add_argument("name", help="Linia tekstu która ma zostać napisana w pliku", action="store_true")
    parser.add_argument("count", help="Liczba linii tekstu", type=int)

    args = parser.parse_args()


    ilosc = wewnetrzna(args.count)
    nazwa = wewnetrzna(args.filename)
    tresc = wewnetrzna(args.name)


    if args.count and args.filename and args.name:
        wewnetrzna(ilosc, nazwa, tresc)

glowna()










