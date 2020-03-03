import argparse



def main():
    p = argparse.ArgumentParser(description="Script using to looking for extended files")
    p.add_argument("--log_name", help="name files where is extended files", dest="log_name", required=True)
    p.add_argument("--directory", help="name folder where will be downloading files", dest="directory", required=True)

    args = p.parse_args()

    log = args.log_name
    direct = args.directory

    look_for(log, direct)


def look_for(log, direct):
    with open(log, 'r') as f1:
        with open(direct,'w') as f2:
            for i in f1:
                if i.find(".rpm"):
                    f2.write(i)
    print("Look in your new file a check it out, what I have done! ")

print("Everything is correct")


main()


