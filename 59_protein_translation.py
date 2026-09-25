"""
Module to translate RNA sequences into proteins.
"""

def proteins(strand: str):
    """Function returns the names of the proteins of a given RNA sequence.

    args:
        strand (str): RNA strand

    return:
        list: names of the proteins"""

    translator = {"Methionine": ["AUG"], "Phenylalanine": ["UUU", "UUC"], "Leucine": ["UUA", "UUG"],
                  "Serine": ["UCU", "UCC", "UCA", "UCG"], "Tyrosine": ["UAU", "UAC"],
                  "Cysteine": ["UGU", "UGC"], "Tryptophan": ["UGG"], "STOP": ["UAA", "UAG", "UGA"]}

    proteins_list = []

    for index in range(2, len(strand), 3):
        for key, value in translator.items():
            if strand[index - 2:index + 1] in value:
                protein = key
                break

        if protein == "STOP":
            break
        proteins_list.append(protein)

    return proteins_list