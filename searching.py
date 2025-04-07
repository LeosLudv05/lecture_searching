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
    #read data
    seq = read_data(file_name, field='dna_sequence')
    vzor = "ATA"
    #pattern_search
    matches = pattern_search(seq, vzor)
    print(matches)
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


def pattern_search(seq, vzor):
    """
    Algoritmus sekvenčního vyhledávání vzorů, který v řetězci DNA nalezne pozice výskytu zadaného vzoru.
    :param indexy: tuple s indexy
    :param seq: Prohledávaná sekvence
    :param vzor: Hledaný vzor v DNA
    :return: tuple(indexy výskytu)
    """
    indexy = set()
    velikost_vzoru = len(vzor)
    left_idx = 0
    right_idx = velikost_vzoru
    while right_idx < len(seq):
        for idx in range(velikost_vzoru):
            if vzor[idx] != seq[left_idx + idx]:
                break
        else:
                indexy.add(left_idx + velikost_vzoru // 2)
        left_idx += 1
        right_idx += 1


    return indexy


def binary_search(seznam, cislo):
    """
    Bude binárně vyhledávat zda-li se ve vzestupně seřazené posloupnosti nachází libovolné požadované číslo a vrátí jeho pozici.
    :param seznam:
    :param cislo:
    :return:
    """




if __name__ == '__main__':
    main()