import json
import os

# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    if field not in {'unordered_numbers', 'ordered_numbers', 'dna_sequence'}:
        return None

    file_path = os.path.join(cwd_path, file_name)

    with open(file_path, "r") as json_file:
        seq = json.load(json_file)

    return seq[field]

def main():
    file_name = "sequential.json"

    #read data
    seq = read_data(file_name, field='unordered_numbers')
    print(seq)
    pass

def linear_search(seq, cislo):
    """
    V neseřazeném seznamu nalezne pozice a četnost výskytu
    :param sekv: prohledávaná sekvence v "unordered_numbers"
    :param cislo: hledané číslo
    :return: slovnik[positions, count]
    """

    indicies = []
    count = 0

    idx = 0
    while idx < len(seq):
        if seq[idx] == cislo:
            indicies.append(idx)
            count =+ 1
        idx += 1

    return {
        'positions': indicies,
        'count': count,
    }


if __name__ == '__main__':
    main()