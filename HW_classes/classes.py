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

    def sequnces_number(self):
        return len([1 for line in open(self.path) if line.startswith(">")])

    def hist_len_of_sequences(self):
        self.length_list = []
        with open(self.path) as fasta:
            for line in fasta:
                if not line.startswith(">"):
                    self.length_list[-1] += len(line)
                else:
                    self.length_list.append(0)
        ax = sns.histplot(self.length_list)
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
