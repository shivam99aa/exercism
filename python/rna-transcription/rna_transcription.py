def to_rna(dna_strand):
    rna_strand = ""
    dna2rna = {"G": "C",
               "C": "G",
               "T": "A",
               "A": "U"
            }
    for dna in dna_strand.upper():
        try:
            rna_strand = rna_strand + dna2rna[dna]
        except KeyError:
            rna_strand = rna_strand + "_"
    return rna_strand
