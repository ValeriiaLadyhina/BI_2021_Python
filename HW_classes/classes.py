from Bio.Seq import Seq
from Bio import SeqIO
import seaborn as sns
import matplotlib.pyplot as plt
import random


class Bacteria():

    def __init__(self, name, antibiotic, AMR=0, number=100000):
        self.bacteria_name = name
        self.bacteria_number = number
        self.AMR = AMR
        self.antibiotic = antibiotic
        self.antibitotic_possible_for_treatment = {'E.coli': 'amoxicillin', 'Salmonella': 'metronidazole'}
        self.chance_to_develope_AMR = {'amoxicillin': 15, 'metronidazole': 5, 'colistin': 25}
        self.treatment = {'amoxicillin': 6, 'metronidazole': 12, 'colistin': 24}
        self.speed_of_growth = {'E.coli': 1.3, 'Salmonella': 1.13}

    def development_of_AMR(self):
        chance = random.randint(0, self.chance_to_develope_AMR[self.antibiotic])
        self.AMR = (self.bacteria_number - self.AMR) * chance + self.AMR
        return self.AMR

    def infection_treatment(self):
        if self.antibiotic != self.antibitotic_possible_for_treatment[self.bacteria_name]:
            return 'Choose another treatment, as this one is not suitable'
        else:
            self.bacteria_number = (self.bacteria_number - self.AMR) * 0.5 + self.AMR
            return self.bacteria_number

    def bacterial_grows(self):
        self.bacteria_number = self.bacteria_number * self.speed_of_growth[self.bacteria_name]
        return self.bacteria_number

    def model(self):
        treatment = 1
        self.infection_treatment()
        self.development_of_AMR()
        for i in range(168):  # hour in one week of treatment
            self.bacterial_grows()
            if i % self.treatment[self.antibiotic] == 0:
                treatment += 1
                self.infection_treatment()
                self.development_of_AMR()
        if self.bacteria_number / self.AMR >= 0.8:
            print('We have to treat with last line antibiotics')
        elif 0.4 < self.bacteria_number / self.AMR < 0.8:
            print('We have to choose other antibiotic')
        else:
            print('Patient is going to recover soon')


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
        self.positive_set = set()
        for ele in self.set_:
            if ele > 0:
                self.positive_set.add(ele)

    def add(self, *elements):
        for ele in elements:
            if ele > 0:
                self.positive_set.add(ele)
        return set(self.positive_set)

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

