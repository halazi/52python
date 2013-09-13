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
        tmp_data = " ".join(split_data[i+1].split())
        if len(tmp_data) > 0:
            for j in range(len(tmp_data)-1, -1, -1):
                if ord(tmp_data[j]) >= 0x4E00 and ord(tmp_data[j]) <= 0x9FFF:
                    if j >= len(tmp_data) - 1 or tmp_data.find(" ", j, len(tmp_data)) == -1:
                        out_data += "{" + tmp_data + "}" + "\r\n" + "[]" + "\r\n"
                        break
                    else:
                        out_data += "{" + tmp_data[0:j+1] + "}" + "\r\n" + "[" + tmp_data[j+1:].strip() + "]" + "\r\n"
                        break
        else:
            out_data += "{}\r\n[]\r\n"

    #print(out_data)
    if len(sys.argv) == 2:
        out_file_name = in_file_name + ".txt"
    else:
        out_file_name = sys.argv[2]
    out_file_encoding = in_file_encoding
    fout = open(out_file_name, "wt", encoding=out_file_encoding)
    fout.write(out_data)
    fout.close()

if __name__ == '__main__':
    main()
