def fastq_filter(input_fastq, output_file_prefix, gc_bounds=(0, 100), length_bounds=(0, 2**32), quality_threshold=0,
                 save_filtered=False):
    sequence_dictionary, sequence_dictionary_original = open_fastq_file(input_fastq)
    sequence_dictionary = quality_control(sequence_dictionary)
    parameters = input('Do you want to change any parameters? Please type Y/N.\n By default:\n\n'
                       '* gc_bounds = (0,100)\n'
                       '* length_bounds = (0,2**32)\n'
                       '* quality_threshold = 0\n'
                       '* save_filtered = False\n\n')
    if parameters == 'Y':
        gc_bounds, length_bounds, quality_threshold, save_filtered = change_of_parameters(gc_bounds,
                                                                                          length_bounds,
                                                                                          quality_threshold,
                                                                                          save_filtered)
    else:
        pass
    sequence_dictionary, list_to_be_removed = gc_content_filter(sequence_dictionary, gc_bounds)
    sequence_dictionary, list_to_be_removed = length_filter(sequence_dictionary, length_bounds, list_to_be_removed)
    sequence_dictionary, list_to_be_removed = quality_filter(sequence_dictionary, quality_threshold, list_to_be_removed)
    saving(sequence_dictionary, sequence_dictionary_original, output_file_prefix, save_filtered, list_to_be_removed)


def open_fastq_file(input_fastq):
    with open(input_fastq, 'r') as file:
        fastq_file = file.readlines()
    sequence_dictionary = {}
    sequence_dictionary_original = {}
    for i in range(0, len(fastq_file)-1, 4):
        id_code = fastq_file[i].replace("\n", "")
        sequence = fastq_file[i+1].replace("\n", "")
        third_line = fastq_file[i+2].replace("\n", "")
        quality_score = fastq_file[i+3].replace("\n", "")
        sequence_dictionary[i//4] = [id_code, sequence, third_line, quality_score]
    sequence_dictionary_original = sequence_dictionary
    return sequence_dictionary, sequence_dictionary_original


def quality_control(sequence_dictionary):
    length_of_reads = []
    gc_values = []
    quality_values = []
    for key in sequence_dictionary:
        sequence = sequence_dictionary[key][1]
        gc_composition = ((sequence.count('G')+sequence.count('C'))/len(sequence))*100
        gc_values.append(round(gc_composition, 1))
        sequence_dictionary[key].append(round(gc_composition, 1))
        length_of_reads.append(len(sequence))
        sequence_dictionary[key].append(len(sequence))
        quality = []
        for i in sequence_dictionary[key][3]:
            quality.append(ord(i)-33)
        sequence_dictionary[key].append(numpy.mean(quality))

        quality_values.append(numpy.mean(quality))
    print('Basic statistics on reads quality:\n')
    print('* GC composition: min =', min(gc_values), ', max =', max(gc_values), ', average =', numpy.mean(gc_values))
    print('* Length of reads: min =', min(length_of_reads), ', max =', max(length_of_reads),
          ', average =', numpy.mean(length_of_reads))
    print('* Quality of reads: min =', min(quality_values), ', max =', max(quality_values),
          ', average =', numpy.mean(quality_values), '\n\n')
    return sequence_dictionary


def gc_content_filter(sequence_dictionary, gc_bounds):
    list_to_be_removed = []
    if gc_bounds != (0, 100):
        for key in sequence_dictionary.keys():
            if sequence_dictionary[key][4] < gc_bounds[0] or sequence_dictionary[key][4] > gc_bounds[1]:
                list_to_be_removed.append(key)
        for i in list_to_be_removed:
            sequence_dictionary.pop(i)
    return sequence_dictionary, list_to_be_removed


def length_filter(sequence_dictionary, length_bounds, list_to_be_removed):
    if length_bounds != (0, 2**32):
        list_to_be_removed = []
        for key in sequence_dictionary.keys():
            if sequence_dictionary[key][5] < length_bounds[0] or sequence_dictionary[key][5] > length_bounds[1]:
                list_to_be_removed.append(key)
        for i in list_to_be_removed:
            sequence_dictionary.pop(i)
    return sequence_dictionary, list_to_be_removed


def quality_filter(sequence_dictionary, quality_threshold, list_to_be_removed):
    if quality_threshold != 0:
        list_to_be_removed = []
        for key in sequence_dictionary.keys():
            if sequence_dictionary[key][6] < quality_threshold:
                list_to_be_removed.append(key)
        for i in list_to_be_removed:
            sequence_dictionary.pop(i)
    return sequence_dictionary, list_to_be_removed


def saving(sequence_dictionary, sequence_dictionary_original, output_file_prefix, save_filtered, list_to_be_removed):
    with open((output_file_prefix + "_filtered_reads.fastq"), 'w') as file1:
        for key in sequence_dictionary.keys():
            file1.writelines([sequence_dictionary[key][0], sequence_dictionary[key][1],
                             sequence_dictionary[key][2], sequence_dictionary[key][3]])
    file1.close()
    if save_filtered == True:
        with open((output_file_prefix + "_filtered_out_reads.fastq"), 'w') as file2:
            for i in list_to_be_removed:
                print(i)
                file2.writelines([sequence_dictionary_original[key][0], sequence_dictionary_original[key][1],
                                 sequence_dictionary_original[key][2], sequence_dictionary_original[key][3]])


def change_of_parameters(gc_bounds, length_bounds, quality_threshold,
                         save_filtered):
    answer = 'N'
    while answer == 'N':
        parameters_to_change = int(input('1 - GC Bounds,\n2 - Length Bounds,\n3 - Quality Threshold,\n4 - '
                                         'Create an output file for reads that did not pass quality control\n\n'
                                         'Please enter the number of parameter you want to change:\n\n'))
        while parameters_to_change not in [1, 2, 3, 4]:
            parameters_to_change = int(input('You typed incorrect index. Please try again.\n\n'
                                             '1 - GC Bounds,\n2 - Length Bounds,\n3 - Quality Threshold,\n4 - '
                                             'Create an output file for reads that did not pass quality control\n\n'
                                             'Please enter the number of parameter you want to change:\n\n'))
        if parameters_to_change == 1:
            gc_bounds = [int(x) for x in input('Example 0 100 - print two numbers with delimiter - space\n\n'
                                               'Enter lower and upper bound for GC content in between 0 '
                                               'to 100.\n ').split()]
            lower, upper = gc_bounds[0], gc_bounds[1]
            while ((lower or upper) not in range(0, 100)) or upper < lower:
                print(lower, upper)
                gc_bounds = [int(x) for x in input('You put incorrect value. Please try again.\n'
                                                   'Enter lower and upper bound for GC '
                                                   'content in between 0 to 100 with delimiter space.\n').split()]
                lower, upper = gc_bounds[0], gc_bounds[1]
        elif parameters_to_change == 2:
            length_bounds = input('Enter lower and upper limit for length of reads divided by space.\n')
            while ',' not in length_bounds or ' ' in length_bounds:
                length_bounds = input('Wrong format. Please repeat your input.\n Write lower boundary and upper '
                                      'boundary with delimiter space\n')
            length_bounds = length_bounds.split(',')
            lower, upper = int(length_bounds[0]), int(length_bounds[1])
            while ((lower or upper) not in range(0, 2**32)) or upper < lower:
                length_bounds = input('Your input is outside supported values 0 - 4294967296. Please try again.'
                                      'Enter lower and upper limit for length of reads.\n')
                length_bounds = length_bounds.split(',')
                lower, upper = int(length_bounds[0]), int(length_bounds[1])
        elif parameters_to_change == 3:
            quality_threshold = input('Enter minimal value of quality for read to be accepted. '
                                      'The number has to be in'
                                      'range from 0 to 40.\n')
            while int(quality_threshold) not in range(0, 40):
                quality_threshold = input('You wrote incorrect value.Please try again.\n'
                                          'Enter minimal value of quality for read to be accepted. '
                                          'The number has to '
                                          'be in range from 0 to 40.\n')
        else:
            save_filtered = input('Do you want to save both reads that passed filter and reads that did not in two '
                                  'separate files? Then please print True, if you want to save only fastq file'
                                  ' with '
                                  'reads that passed filtering please type False:\n\nEnter you answer '
                                  'True or False\n\n')
        print('Please check if parameters are correct:\n'
              'GC Bounds (lower:', gc_bounds[0], 'upper:', gc_bounds[1], ')\n'
              'Length Bounds (lower:', length_bounds[0], 'upper:', length_bounds[1], '),\n Quality Threshold = ',
              quality_threshold, ',\nSave Filtered = ', save_filtered, '?\n\n')
        answer = input('Enter Y/N\n')
    return gc_bounds, length_bounds, quality_threshold, save_filtered


if __name__ == "__main__":

    import numpy

    welcoming_message = '''Welcome to FastQ Filtrator.\nYou can use this programme to perform quality assessment of
     your fastq files based on GC content, read length and quality to filter your raw Illumina sequencing data. It is
     a first version of the tool,therefore I would ask you to be careful with your input of the name of file to be
     analyzed.\n
     The programme takes 4 parameters\n:
        * GC Bounds is parameter describing GC content (default: 0, 100).
        * Length Bounds defines frames for read length (default: 0, 2**32).
        * Quality Threshold (QT) - the minimal mean quality of the read based on phred33 scale (default: 0).
        * Save Filtered. By default settings programme will save only reads that passed quality control. If you want to
        save also reads that didn't pass thresholds in a separate output file please change this parameter to True.'''
    print(welcoming_message)
    input_fastq = input('Enter name of input fastq file including filename extension.You can enter either just name of '
                        'the file if it is located in the same folder as the script or print the absolute path '
                        'to it.\n')
    output_file_prefix = input_fastq.replace('.fastq', '')
    gc_bounds = (0, 100)
    length_bounds = (0, 2**32)
    quality_threshold = 0
    save_filtered = False
    answer = 'Y'
    while answer == 'Y':
        fastq_filter(gc_bounds, length_bounds, quality_threshold,
                     save_filtered, input_fastq, output_file_prefix)
        answer = input("Do you want to perform analysis on other data?\n Please write Y, "
                       "if you want to end your work with FastQ Filtrator print N\n\n")
    print('Thank you for using FastQ Filtrator version 0.1, that was developed by Valeriia Ladyhina. '
          'If you have any suggestions, questions or complains please report to valeriia.ladyhina@gmail.com')
