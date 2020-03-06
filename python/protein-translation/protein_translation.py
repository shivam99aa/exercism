def proteins(strand):
    strand2protein = {"AUG": "Methionine",
                      "UUU": "Phenylalanine", "UUC": "Phenylalanine",
                      "UUA": "Leucine", "UUG": "Leucine",
                      "UCU": "Serine", "UCC": "Serine", "UCA": "Serine", "UCG": "Serine",
                      "UAU": "Tyrosine", "UAC": "Tyrosine",
                      "UGU": "Cysteine", "UGC": "Cysteine",
                      "UGG": "Tryptophan",
                      "UAA": "STOP", "UAG": "STOP", "UGA": "STOP"}

    codonslist = [strand[0+i:i+3] for i in range(0, len(strand), 3)]
    protein = []
    for codon in codonslist:
        if codon not in strand2protein.keys() or strand2protein[codon] == "STOP":
            return protein
        else:
            protein.append(strand2protein[codon])
    return protein
