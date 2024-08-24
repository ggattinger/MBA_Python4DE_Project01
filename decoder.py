import sys
import csv

csv_file = 'dict.csv'

def read_csv(csv_file):
    result_dict = {}
    with open(csv_file, mode='r') as file:
        csv_reader = csv.reader(file, delimiter=";")
        for row in csv_reader:
            key = row[0]
            value = row[1]
            result_dict[key] = value
    return result_dict

def translate(mensagem):
    code = ''
    msg = ''
    last_pos = ''
    i = 0
    for pos in mensagem:
        i += 1
        if pos == ' ' and last_pos == ' ':
            msg += ' '
        elif pos == ' ' and last_pos != ' ':
            mc = morse_dict.get(code)
            msg += mc
            code = ''
        else:
            code += pos
        if i == len(mensagem):
            mc = morse_dict.get(code)
            msg += mc
        last_pos = pos
    return msg

if __name__ == "__main__":
    morse_dict = read_csv(csv_file)
    msg = translate(sys.argv[1])
    print(msg)