def test_for_sequence_normality(sequence):
    for i in sequence:
        if i not in 'ATCGatcg':
            return 'Error'


def transcribe():
    print('Please write sequence for analysis')
    sequence = str(input())
    if test_for_sequence_normality(sequence) == "Error":
        return print('Error: Invalid Alphabet')
    complement_sequence = []
    transcribed_sequence = []
    dna_to_complement_dna = {'A':'T', 'a':'t', 'T':'A','t':'a','C':'G','c':'g','G':'C','g':'c'}
    dna_to_rna = {'A':'U', 'a':'u', 'T':'A','t':'a','C':'G','c':'g','G':'C','g':'c'}
    for i in sequence:
        complement_sequence.append(dna_to_complement_dna[i])
    for i in complement_sequence:
        transcribed_sequence.append(dna_to_rna[i])
    print(''.join(transcribed_sequence))
    return


def reverse():
    print('Please write sequence for analysis')
    sequence = str(input())
    if test_for_sequence_normality(sequence) == "Error":
        return print('Error: Invalid Alphabet')
    reversed_sequence = sequence[::-1]
    return print(reversed_sequence)


def complement():
    print('Please write sequence for analysis')
    sequence = str(input())
    if test_for_sequence_normality(sequence) == "Error":
        return print('Error: Invalid Alphabet')
    complement_sequence = []
    dna_to_complement_dna = {'A': 'T', 'a': 't', 'T': 'A', 't': 'a', 'C': 'G', 'c': 'g', 'G': 'C', 'g': 'c'}
    for i in sequence:
        complement_sequence.append(dna_to_dna[i])
    print(''.join(complement_sequence))
    return


def reverse_complement():
    print('Please write sequence for analysis')
    sequence = str(input())
    if test_for_sequence_normality(sequence) == "Error":
        return print('Error: Invalid Alphabet')
    reversed_sequence = sequence[::-1]
    dna_to_complement_dna = {'A':'T', 'a':'t', 'T':'A','t':'a','C':'G','c':'g','G':'C','g':'c'}
    reversed_complement_sequence = []
    for i in reversed_sequence:
        reversed_complement_sequence.append(dna_to_complement_dna[i])
    return print(''.join(reversed_complement_sequence))


def exit():
    print('Thank you for using our package. Good Luck!')


if __name__ == "__main__":
    while True:
        command = input()
        if command == 'transcribe':
            transcribe()
        elif command == 'complement':
            complement()
        elif command == 'reverse':
            reverse()
        elif command == 'reverse complement':
            reverse_complement()
        elif command == 'exit':
            exit()
            break

