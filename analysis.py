def test_for_sequence_normality1(sequence):
    for i in sequence:
        if i not in 'ATCGatcg':
            return 'Error'


def test_for_sequence_normality2(sequence):
    for i in sequence:
        if i not in 'ATCGatcgUu':
            return 'Error'


def transcribe():
    '''

    :return:
    '''
    print('Please write sequence for analysis')
    sequence = input()
    if test_for_sequence_normality(sequence) == "Error":
        return print('Error: Invalid Alphabet')
    complement_sequence = []
    transcribed_sequence = []
    dna_to_complement_dna = {'A': 'T', 'a': 't', 'T': 'A', 't': 'a', 'C': 'G', 'c': 'g', 'G': 'C', 'g': 'c'}
    dna_to_rna = {'A': 'U', 'a': 'u', 'T': 'A', 't': 'a', 'C': 'G', 'c': 'g', 'G': 'C', 'g': 'c'}
    for i in sequence:
        complement_sequence.append(dna_to_complement_dna[i])
    for i in complement_sequence:
        transcribed_sequence.append(dna_to_rna[i])
    print(''.join(transcribed_sequence))



def reverse():
    print('Please write sequence for analysis')
    sequence = input()
    if test_for_sequence_normality2(sequence) == "Error":
        return print('Error: Invalid Alphabet')
    reversed_sequence = sequence[::-1]
    print(reversed_sequence)


def complement():
    print('Please write sequence for analysis')
    sequence = input()
    if test_for_sequence_normality(sequence) == "Error":
        return print('Error: Invalid Alphabet')
    complement_sequence = []
    dna_to_complement_dna = {'A': 'T', 'a': 't', 'T': 'A', 't': 'a', 'C': 'G', 'c': 'g', 'G': 'C', 'g': 'c'}
    for i in sequence:
        complement_sequence.append(dna_to_complement_dna[i])
    print(''.join(complement_sequence))



def reverse_complement():
    print('Please write sequence for analysis')
    sequence = input()
    if test_for_sequence_normality(sequence) == "Error":
        return print('Error: Invalid Alphabet')
    reversed_sequence = sequence[::-1]
    dna_to_complement_dna = {'A': 'T', 'a': 't', 'T': 'A', 't': 'a', 'C': 'G', 'c': 'g', 'G': 'C', 'g': 'c'}
    reversed_complement_sequence = []
    for i in reversed_sequence:
        reversed_complement_sequence.append(dna_to_complement_dna[i])
    print(''.join(reversed_complement_sequence))


def exit():
    print('Thank you for using our package. Good Luck!')

command = input("Enter command: ")

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

