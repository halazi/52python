import sys
import re

def main():
    in_file_name = sys.argv[1]
    fin_tmp = open(in_file_name, "rb")
    bom = fin_tmp.read()[0:2]
    fin_tmp.close()
    if bom == b"\xfe\xff":
        in_file_encoding = "utf-16be"
    else:
        in_file_encoding = "utf-16le"
    fin = open(in_file_name, "rt", encoding=in_file_encoding)
    in_data = fin.read()
    fin.close()

    split_data = re.split(r"([0-9\-]+:[0-9\-]+:[0-9\-]+:[0-9\-]+ [0-9\-]+:[0-9\-]+:[0-9\-]+:[0-9\-]+)", in_data)
    out_data = split_data[0].strip()
    for i in range(1, len(split_data), 2):
        out_data += split_data[i]
        out_data += " "
        out_data += " ".join(split_data[i+1].split())
        out_data += "\n"
    print(out_data)

    if len(sys.argv) == 2:
        out_file_name = in_file_name + ".txt"
    else:
        out_file_name = sys.argv[2]
    out_file_encoding = in_file_encoding
    #fout = open(out_file_name, "wt", encoding=out_file_encoding)
    #fout.write(out_data)
    #fout.close()

if __name__ == '__main__':
    main()
