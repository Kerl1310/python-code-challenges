import sys


def dna_strand(strand):
    '''
    Returns the complementary strand of DNA for a given strand.
    '''
    complementary_strand = ""
    for symbol in strand:
        if symbol == 'A':
            complementary_strand += 'T'
            continue
        elif symbol == 'T':
            complementary_strand += 'A'
            continue
        elif symbol == 'C':
            complementary_strand += 'G'
            continue
        elif symbol == 'G':
            complementary_strand += 'C'
            continue
    return complementary_strand


if len(sys.argv) > 1:
    print(dna_strand(sys.argv[1]))
