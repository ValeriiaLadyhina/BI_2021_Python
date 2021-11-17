> Python tool for filtration of raw Illumina reads - FastQ Filtrator

## Introduction
FastQ Filtrator is a tool for filtering raw Illumina data based on three different parameters:

* GC composition
* Length of the reads
* Average quality of the read

## Installing
To start working with __FastQ Filtrator__ please download *__fastq_filtrator.py__* to a chosen folder on the computer.

## Start
To start the tool in your terminal please type the absolute path to the tool script and then print:
*__python fastq_filtrator.py__*

## Example
You can do a trial run of the tool on a data that is called *example.fastq* and check the output in two output files *example_filtered_out_reads.fastq* and *example_filtered_reads.fastq*

## Functions that are presented in the tool:
* fastq_filter - function performing filtration of the reads, parameters:
  * input_fastq - absolute path to fastq file, need to include filename extension *.fastq*
  * otput_file_prefix - created based on name of input fastq
  * gc_ bounds - lower and upper limit of GC content
    * by default lower = 0, upper = 100
  * length_bounds - lower and upper limit for read's length to keep it
    * default values are equeal to 0, 2**32
  * quality threshold - threshold index under which reads will not path filtering
    * default value 0
  * save_filtered - you can choose if you want to save only reads that passed filters (**filtered_reads.fastq*) or also 
    save in a separate file (**filtered_out_reads.fastq*) 
    * by default False - will create only one output fastq file, if you want to have two output fastq files please set 
      this parameter to True


* open_fastq_file - function will open fastq file and create dictionary with key - number of the read and 
  value [id of the read, sequenece, +, quality]


* quality_control - this function performs the basic statistics on the reads and will print out
  * mean, max, average values of GC content, length and quality of investigated reads. Also in this function you can set
    limits of GC content, length and quality that you would like to use for filtering and also make a choice to have one
    or two output files as described above.
  

* gc_content_filter - filter of reads based on GC content


* length_filter - filter of reads based on length


* quality_filter - filter of reads based on average quality of the read


* saving - function that will create one or two fastq files that will be saved in the same folder as located input file


* change_of_parameters - this function is used for personalisation of parameters such as gc, length and quality 
  threshold indexes and also choice of one or two output files to be created.
  
## Known bugs
If you will fill in name of input file that doesn't exist or you will write limits for filters in wrong format programme will end and you will need to restart it. Therefore until this problem won't be fixed please be very careful with your inputs. Thank you for your understanding :)


## Authors and acknowledgements
#### Main contributor
* Valeriia Ladyhina

## Feedback
 If you have any questions or complains please approach the author of FastQ Filtrator via email:
 *__valeriia.ladyhina@gmail.com__*
