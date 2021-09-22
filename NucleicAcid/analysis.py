def test_for_sequence_normality(sequence):
    for i in sequence:
        if i not in 'ATCGatcg':
            return 'Error'


def transcribe():
    print('Please write sequence for analysis')
    sequence = str(input())
    if test_for_sequence_normality(sequence) == "Error":
        return 'Error: Invalid Alphabet'
    transcribed_sequence = []
    for i in sequence:
        if i == 'A':
            transcribed_sequence.append('T')
        elif i == 'a':
            transcribed_sequence.append('t')
        elif i == 'T':
            transcribed_sequence.append('U')
        elif i == 't':
            transcribed_sequence.append('u')
        elif i == "G":
            transcribed_sequence.append('C')
        elif i == 'g':
            transcribed_sequence.append('c')
        elif i == 'C':
            transcribed_sequence.append('G')
        else:
            transcribed_sequence.append('g')
    return ''.join(transcribed_sequence)


def reverse():
    print('Please write sequence for analysis')
    sequence = str(input())
    if test_for_sequence_normality(sequence) == "Error":
        return 'Error: Invalid Alphabet'
    reversed_sequence = sequence[::-1]
    return reversed_sequence


def complement():
    print('Please write sequence for analysis')
    sequence = str(input())
    if test_for_sequence_normality(sequence) == "Error":
        return 'Error: Invalid Alphabet'
    complement_sequence = []
    for i in sequence:
        if i == 'A':
            complement_sequence.append('T')
        elif i == 'a':
            complement_sequence.append('t')
        elif i == 'T':
            complement_sequence.append('A')
        elif i == 't':
            complement_sequence.append('a')
        elif i == "G":
            complement_sequence.append('C')
        elif i == 'g':
            complement_sequence.append('c')
        elif i == 'C':
            complement_sequence.append('G')
        else:
            complement_sequence.append('g')
    return ''.join(complement_sequence)


def reverse_complement():
    print('Please write sequence for analysis')
    sequence = str(input())
    if test_for_sequence_normality(sequence) == "Error":
        return 'Error: Invalid Alphabet'
    reversed_sequence = sequence[::-1]
    reversed_complement_sequence = []
    for i in reversed_sequence:
        if i == 'A':
            reversed_complement_sequence.append('T')
        elif i == 'a':
            reversed_complement_sequence.append('t')
        elif i == 'T':
            reversed_complement_sequence.append('A')
        elif i == 't':
            reversed_complement_sequence.append('a')
        elif i == "G":
            reversed_complement_sequence.append('C')
        elif i == 'g':
            reversed_complement_sequence.append('c')
        elif i == 'C':
            reversed_complement_sequence.append('G')
        else:
            reversed_complement_sequence.append('g')
    return ''.join(reversed_complement_sequence)


def exit():
    print('Thank you for using our package. Good Luck!')
