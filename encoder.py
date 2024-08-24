import sys
import csv

csv_file = 'dict.csv'

def read_csv(csv_file):
    result_dict = {}
    with open(csv_file, mode='r') as file:
        csv_reader = csv.reader(file, delimiter=';')
        for row in csv_reader:
            key = row[1]
            value = row[0]
            result_dict[key] = value
    return result_dict

def translate(mensagem):
    msg = ''
    # i = 0
    for pos in mensagem:
        pos = pos.upper()
        if pos == ' ':
            mc = ' '
            msg += mc
        else:
            mc = morse_dict.get(pos)
            msg += mc + ' '
    return msg

if __name__ == "__main__":
    morse_dict = read_csv(csv_file)
    msg = translate(sys.argv[1])
    print(msg)