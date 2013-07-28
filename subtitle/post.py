#!/usr/bin/python

import os
import sys
import re

def main():
    all_file_names = [name for name in os.listdir(".")]
    mod_file_names = [name for name in all_file_names if re.search(r"\.ass\.modified\.txt$", name, re.IGNORECASE)]
    #print filenames
    for mod_file_name in mod_file_names:
        ch_file_name = mod_file_name[:-13]
        if ch_file_name in all_file_names:
            fin_ch = open(ch_file_name, "r")
            fin_mod = open(mod_file_name, "r")
            fout = open(ch_file_name[:-4] + ".english.ass", "w")
            ch_file_content = fin_ch.read()
            head_match = re.search(r"^([\000-\377]+?)\0D\0i\0a\0l\0o\0g\0u\0e\0:", ch_file_content)
            fout.write(head_match.group(1))
            ch_matches = re.findall(r"(\0D\0i\0a\0l\0o\0g\0u\0e\0:[\000-\053\055-\177]*,[\000-\053\055-\177]*,[\000-\053\055-\177]*,[\000-\053\055-\177]*,[\000-\053\055-\177]*,[\000-\053\055-\177]*,[\000-\053\055-\177]*,[\000-\053\055-\177]*,[\000-\053\055-\177]*,)([\000-\377]*?\000\015\000\012|[\000-\377]*$)", ch_file_content)
            mod_file_content = fin_mod.read()
            mod_matches = re.findall(r"\0\[([\000-\177]*?)\0\]", mod_file_content)
            for a, b in zip(ch_matches, mod_matches):
                if b != mod_matches[-1]:
                    fout.write(a[0] + b + "\0\x0D\0\x0A")
                else:
                    fout.write(a[0] + b)
            fin_ch.close()
            fin_mod.close()
            fout.close()

if __name__ == "__main__":
    main()
