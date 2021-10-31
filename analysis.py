dna_to_complement_dna = {'A': 'T', 'a': 't', 'T': 'A', 't': 'a', 'C': 'G', 'c': 'g', 'G': 'C', 'g': 'c'}
rna_to_complement_rna = {'A': 'U', 'a': 'u', 'U': 'A', 'u': 'a', 'C': 'G', 'c': 'g', 'G': 'C', 'g': 'c'}
dna_to_rna = {'A': 'U', 'a': 'u', 'T': 'A', 't': 'a', 'C': 'G', 'c': 'g', 'G': 'C', 'g': 'c'}
dna_commands = ['transcribe', 'reverse', 'complement', 'reverse complement']
rna_commands = ['reverse', 'complement', 'reverse complement']


def main():
    print('\n'
          'Welcome to the tool for analysis of nucleic acids\n'
          'Using this tool you can perform:\n'
          '    * transcribtion of DNA to RNA\n'
          '    * find reversed, complement and both reversed and complement sequence of DNA or RNA\n'
          '\n'
          'How to work with the tool\n'
          'In this tool you can call 4 functions:\n'
          '    * transcribe\n'
          '    * reverse\n'
          '    * complement\n'
          '    * reverse complement\n'
          'Functions reverse, complement and reverse complement you can apply for both DNA and RNA\n')
    while True:
        perform_analysis = input('Do you want to start analysis? Please write Y/N.\n')
        if perform_analysis in ['yes', 'Yes', 'Y', 'YES', 'y']:
            NA = input('Type on what type of nucleic acid you want to work.\n')
            while NA not in ['DNA', 'dna', 'RNA', 'rna']:
                print('NA')
                NA = input('Error. Try again\n')
            sequence = input('Please write sequence for analysis\n')
            if NA in ['DNA', 'dna']:
                test_for_correct_dna(sequence)
                complement_set = dna_to_complement_dna
                command = input('Type function to start.\n'
                                '*transcribe, *reverse, *complement, *reverse complement\n')
                while command not in dna_commands:
                    command = input('You typed not correct function. Please check spelling and type function again: \n')
                if command == 'transcribe':
                    transcribe(sequence)
                elif command == 'reverse':
                    reverse(sequence)
                elif command == 'complement':
                    complement(sequence, complement_set)
                elif command == 'reverse complement':
                    reverse_complement(sequence, complement_set)
            else:
                test_for_correct_rna(sequence)
                complement_set = rna_to_complement_rna
                command = input('Type function to start.\n'
                                '*reverse, *complement, *reverse complement\n')
                while command not in dna_commands:
                    command = input('You typed not correct function. Please check spelling and type function again: \n')
                if command == 'transcribe':
                    transcribe(sequence)
                elif command == 'reverse':
                    reverse(sequence)
                elif command == 'complement':
                    complement(sequence, complement_set)
                elif command == 'reverse complement':
                    reverse_complement(sequence, complement_set)
        else:
            print('Thank you for using our tool. Good luck!')
            break


def test_for_correct_dna(sequence):
    for i in sequence:
        while i not in 'ACTGacgt':
            sequence = input('Error: Invalid alphabet. Try again\n')
    return sequence


def test_for_correct_rna(sequence):
    for i in sequence:
        while i not in 'ACGUacgu':
            sequence = input('Error: Invalid alphabet. Try again\n')
    return sequence


def transcribe(sequence):
    complement_sequence = []
    transcribed_sequence = []
    for i in sequence:
        complement_sequence.append(dna_to_complement_dna[i])
    for i in complement_sequence:
        transcribed_sequence.append(dna_to_rna[i])
    print(''.join(transcribed_sequence))


def reverse(sequence):
    reversed_sequence = sequence[::-1]
    print(reversed_sequence)


def complement(sequence, complement_set):
    complement_sequence = []
    for i in sequence:
        complement_sequence.append(complement_set[i])
    print(''.join(complement_sequence))


def reverse_complement(sequence, complement_set):
    reversed_sequence = sequence[::-1]
    reversed_complement_sequence = []
    for i in reversed_sequence:
        reversed_complement_sequence.append(complement_set[i])
    print(''.join(reversed_complement_sequence))


if __name__ == "__main__":
    main()
