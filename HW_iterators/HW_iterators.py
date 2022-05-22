import random

sequence_change = ['deletion', 'insertion', 'AA_change']
sequence_change_weights = [2, 3, 5]
AA = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'Y',
      'Z']
'''
Task 1
Generator that reads fasta files
'''


def fasta_generator(path_to_file):
    with open(path_to_file, 'r') as file:
        seq_id = ''
        for line in file:
            if line.startswith('>'):
                if seq_id == '':
                    seq_id = line.strip()
                    sequence = ''
                else:
                    seq_id = line.strip()
                    end_sequence = sequence
                    sequence = ''
                    yield end_seq_id, end_sequence
            else:
                end_seq_id = seq_id
                sequence += line.strip()


'''
Task 2
Class that reads fasta files and makes to them random changes such as deletion, insertion and change of amino acid
'''


class FastaRandom:

    def __init__(self, path_to_file):
        self.__file_path = path_to_file
        self.__generator = fasta_generator(path_to_file)

    def __iter__(self):
        return self

    def change_generator(self, seq):
        change = random.randint(0, 1)
        if change == 0:
            pass
        else:
            change_type = random.choice(sequence_change)
            if change_type == 'deletion':
                seq = self._deletion(seq)
            if change_type == 'insertion':
                seq = self._insertion(seq)
            else:
                seq = self._aa_change(seq)
        return seq

    def _deletion(self, seq):
        start = random.randint(0, len(seq))
        end = random.randint(start, len(seq))
        return seq[:start] + seq[end:]

    def _insertion(self, seq):
        insertion_seq = ''
        start = random.randint(0, len(seq))
        for i in range(random.randint(1, 10)):
            insertion_seq += random.choice(AA)
        return seq[:start] + insertion_seq + seq[start + 1:]

    def _aa_change(self, seq):
        start = random.randint(0, len(seq))
        if len(seq) - start > 20:
            for i in range(random.randint(0, 20)):
                seq[start + i] = random.choice(AA)
        else:
            for i in range(random.randint(0, len(seq) - 20)):
                seq[start + i] = random.choice(AA)
        return seq

    def __next__(self):
        try:
            end_seq_id, end_sequence = next(self.__generator)
        except StopIteration:
            self.__generator = fasta_generator(self.__file_path)
            end_seq_id, end_sequence = next(self.__generator)
        return end_seq_id, end_sequence


'''
Task 3
Generator iter_append
'''


def iter_append(iterable, item):
    yield from iterable
    yield item


'''
Task 4
Function to unpack nested lists
'''


def flatten_nested_list(lst):
    for i in lst:
        if isinstance(i, list):
            yield from flatten_nested_list(i)
        else:
            yield i
