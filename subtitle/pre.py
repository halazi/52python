#!/usr/bin/python

import os
import sys
import re

def main():
    filenames = [name for name in os.listdir(".") if re.search(r"\.ass$", name, re.IGNORECASE)]
    #print filenames
    for filename in filenames:
        fin = open(filename, "r")
        fout = open(filename + '.original.txt', "w")
        fout.write("\xfe\xff")
        infilecontent = fin.read()
        all_matches = re.findall(r"\0D\0i\0a\0l\0o\0g\0u\0e\0:[\000-\053\055-\177]*,[\000-\053\055-\177]*,[\000-\053\055-\177]*,[\000-\053\055-\177]*,[\000-\053\055-\177]*,[\000-\053\055-\177]*,[\000-\053\055-\177]*,[\000-\053\055-\177]*,[\000-\053\055-\177]*,([\000-\377]*?\000\015\000\012|[\000-\377]*$)", infilecontent)
        for match in all_matches:
            if match != all_matches[-1]:
                fout.write(match + "\0[\0]\0\x0D\0\x0A")
            else:
                fout.write(match + "\0\x0D\0\x0A\0[\0]\0\x0D\0\x0A")
        fin.close()
        fout.close()

if __name__ == "__main__":
    main()
