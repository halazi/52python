import codecs
import sys
import commands

def main():
    in_file_name = sys.argv[1]
    in_file_encoding = commands.getoutput("file -b --mime-encoding %s" % in_file_name)
    fin = codecs.open(in_file_name, "r", in_file_encoding)
    print fin.read()
    ## text processing here

    if len(sys.argv) == 2:
        out_file_name = in_file_name + ".txt"
    else:
        out_file_name = sys.argv[2]

if __name__ == '__main__':
    main()
