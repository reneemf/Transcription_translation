#Convert DNA to protein using table
RNA_codon_table = {

# Second Base

# U C A G

# U

'UUU': 'Phe', 'UCU': 'Ser', 'UAU': 'Tyr', 'UGU': 'Cys', # UxU

'UUC': 'Phe', 'UCC': 'Ser', 'UAC': 'Tyr', 'UGC': 'Cys', # UxC

'UUA': 'Leu', 'UCA': 'Ser', 'UAA': '---', 'UGA': '---', # UxA

'UUG': 'Leu', 'UCG': 'Ser', 'UAG': '---', 'UGG': 'Trp', # UxG

# C

'CUU': 'Leu', 'CCU': 'Pro', 'CAU': 'His', 'CGU': 'Arg', # CxU

'CUC': 'Leu', 'CCC': 'Pro', 'CAC': 'His', 'CGC': 'Arg', # CxC

'CUA': 'Leu', 'CCA': 'Pro', 'CAA': 'Gln', 'CGA': 'Arg', # CxA

'CUG': 'Leu', 'CCG': 'Pro', 'CAG': 'Gln', 'CGG': 'Arg', # CxG

# A

'AUU': 'Ile', 'ACU': 'Thr', 'AAU': 'Asn', 'AGU': 'Ser', # AxU

'AUC': 'Ile', 'ACC': 'Thr', 'AAC': 'Asn', 'AGC': 'Ser', # AxC

'AUA': 'Ile', 'ACA': 'Thr', 'AAA': 'Lys', 'AGA': 'Arg', # AxA

'AUG': 'Met', 'ACG': 'Thr', 'AAG': 'Lys', 'AGG': 'Arg', # AxG

# G

'GUU': 'Val', 'GCU': 'Ala', 'GAU': 'Asp', 'GGU': 'Gly', # GxU

'GUC': 'Val', 'GCC': 'Ala', 'GAC': 'Asp', 'GGC': 'Gly', # GxC

'GUA': 'Val', 'GCA': 'Ala', 'GAA': 'Glu', 'GGA': 'Gly', # GxA

'GUG': 'Val', 'GCG': 'Ala', 'GAG': 'Glu', 'GGG': 'Gly' # GxG

}
singleletter = {'Cys': 'C', 'Asp': 'D', 'Ser': 'S', 'Gln': 'Q', 'Lys': 'K',

'Trp': 'W', 'Asn': 'N', 'Pro': 'P', 'Thr': 'T', 'Phe': 'F', 'Ala': 'A',

'Gly': 'G', 'Ile': 'I', 'Leu': 'L', 'His': 'H', 'Arg': 'R', 'Met': 'M',

'Val': 'V', 'Glu': 'E', 'Tyr': 'Y', '---': '*'}

nucleotide_string = 'ATGGCGACTGTCGAACCGGAAACCACCCCTACTCCTAATCCCCCGACTACAGAAGAGGAGAAAACGGAATCTAATCAGGAGGTTGCTAACCCAGAACACTATATTAAACATCCCCTACAGAACAGATGGGCACTCTGGTTTTTTAAAAATGATAAAAGCAAAACTTGGCAAGCAAACCTGCGGCTGATCTCCAAGTTTGATACTGTTGAAGACTTTTGGGCTCTGTACAACCATATCCAGTTGTCTAGTAATTTAATGCCTGGCTGTGACTACTCACTTTTTAAGGATGGTATTGAGCCTATGTGGGAAGATGAGAAAAACAAACGGGGAGGACGATGGCTAATTACATTGAACAAACAGCAGAGACGAAGTGACCTCGATCGCTTTTGGCTAGAGACACTTCTGTGCCTTATTGGAGAATCTTTTGATGACTACAGTGATGATGTATGTGGCGCTGTTGTTAATGTTAGAGCTAAAGGTGATAAGATAGCAATATGGACTACTGAATGTGAAAACAGAGAAGCTGTTACACATATAGGGAGGGTATACAAGGAAAGGTTAGGACTTCCTCCAAAGATAGTGATTGGTTATCAGTCCCACGCAGACACAGCTACTAAGAGCGGCTCCACCACTAAAAATAGGTTTGTTGTTTAA'

new_nu = nucleotide_string.replace('T','U')
"""replace T with U to match RNA_codon_table"""
#print new_nu to check if this section works

def RNA_to_protein(n, RNA_codon_table):
    """converts RNA to protein 3 letter abbreviations"""
    protein_sequence = ""
    for i in range (0, len(n), 3):
        codon = n[i:i+3]
        protein_sequence += RNA_codon_table[codon]
    return protein_sequence
#print RNA_to_protein(new_nu, RNA_codon_table) to check if this section works
three_protein = RNA_to_protein(new_nu, RNA_codon_table)
#print three_protein to check if this section works


def protein_three_to_one(m, singleletter):
    """converts protein 3 letter abbreviations to single letter"""
    single_sequence = ""
    for i in range (0, len(m), 3):
        three_letter = m[i:i+3]
        single_sequence += singleletter[three_letter]
    return single_sequence
print protein_three_to_one(three_protein, singleletter)
