from Bio.Seq import Seq
import seaborn as sns
import matplotlib.pyplot as plt


class Bacteria():

    def __init__(self):
        pass


class RNA():

    def __init__(self, rna):
        self.rna_seq = Seq(rna)

    def traslation(self):
        return str(self.rna_seq.translate())

    def reversed_transcription(self):
        return str(self.rna_seq.back_transcribe())


class PositiveSet(set):

    def __init__(self, set_):
        self.set_ = set_
        positive_set = set()
        for ele in self.set_:
            if ele > 0:
                positive_set.add(self.set_)
        self.positive_set = positive_set

    def add(self):
        pass


class FastaStatistics():

    def __init__(self, path):
        self.path = path

    def sequences_number(self):
        return len([1 for line in open(self.path) if line.startswith(">")])

    def hist_len_of_sequences(self):
        length_list = []
        with open(self.path) as fasta:
            for line in fasta:
                if not line.startswith(">"):
                    length_list[-1] += len(line)
                else:
                    length_list.append(0)
        ax = sns.histplot(length_list)
        ax.set(xlabel='sequence length distribution', ylabel='number')
        plt.show()

    def GC_composition(self):
        self.gc_composition = []
        self.length_list = []
        with open(self.path) as fasta:
            for line in fasta:
                if not line.startswith(">"):
                    gc_line = len([i for i, letter in enumerate(line) if letter in ('G', 'C')])
                    self.gc_composition[-1] += gc_line
                    self.length_list[-1] += len(line)
                else:
                    self.gc_composition.append(0)
                    self.length_list.append(0)
                    if self.gc_composition[-1] != 0:
                        self.gc_composition = self.gc_composition / self.length_list * 100
        return self.gc_composition

    def hist_four_mer(self):
        self.reads = []
        four_mers = {}
        for record in SeqIO.parse(self.path, 'fasta'):
            self.reads.append(record.seq)
        for read in self.reads:
            for i in range(len(read) - 4):
                four_mer = str(read[i:i + 4])
                if four_mer not in four_mers.keys():
                    four_mers[four_mer] = 1
                else:
                    four_mers[four_mer] += 1

        plt.figure(figsize=(140, 20))
        plt.bar(four_mers.keys(), four_mers.values())
        plt.xlabel('Four-mers', fontsize=5)
        plt.ylabel('Number of four-mers')
        plt.title('Four-mers distribution', fontsize=14)

    def __str__(self):
        return self.path

    def output(self):
        return self.GC_composition(), self.sequnces_number()

