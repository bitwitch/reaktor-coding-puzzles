"""
The key to solving this is in these lines:

"The sequencer classified the strand as a template strand for protein synthesis.
Confirmation required by synthesizing the DNA coding strand."

Since the unknown nucleotides can bond with the synthetic nucleotides, then we
know that the synthetic nucleodtides can appear on a synthetic DNA coding
strand that corresponds to the template strand given. By transcribing the
template strand to the corresponding coding strand and then substituting in the
synthetic nucleotides, which are hex representations of ascii characters, the
code "GREENFUTURE" appears in the sequence. This is the password.

+ ------------ +------------- +
|   UNKNOWN    |  SYNTHETIC   |  Ascii character
|  NUCLEOTIDE  |  NUCLEOTIDE  |
+ ------------ + ------------ +
|      V       |      55      |   U
|      W       |      4E      |   N
|      X       |      46      |   F
|      Y       |      52      |   R
|      Z       |      45      |   E

"""

subs = {
    "V": "U",
    "W": "N",
    "X": "F",
    "Y": "R",
    "Z": "E"
}

compliment = {
    "G": "C",
    "A": "T",
    "T": "A",
    "C": "G"
}

codons = {
    "AUG": "M",
    "CUA": "L",
    "CGU": "R",
    "ACC": "T",
    "GUA": "V",
    "GAU": "D",
    "AUC": "I",
    # ...
}


# "ATGCTACGTACCGATGREENFUTUREAATCTGATCGTGAGCT"

def get_coding_strand(seq):
    result = ""
    for c in seq:
        if c in compliment:
            result += compliment[c]
        else:
            result += c
    return result

def substitute(seq):
    result = ""
    for c in seq:
        if c in subs:
            result += subs[c]
        else:
            result += c
    return result

def translate(seq):
    transl = ""
    i = 0
    step = 3
    while i < len(seq) - step:
        codon = seq[i:i+step]

        # STOP codons
        if codon in ["UGA", "UAG", "UAA"]:
            break

        if codon in codons:
            transl += codons[codon]
        else:
            transl += '?'
            print(f"Unknown codon: {codon}")
        i += step

    return transl


if __name__ == "__main__":
    seq = "TACGATGCATGGCTACYZZWXVAVYZTTAGACTAGCACTCGA"
    seq = get_coding_strand(seq)
    seq = substitute(seq)
    print(seq)


