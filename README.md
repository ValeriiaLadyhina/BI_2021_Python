> Python library for the practice in bioinformatics. Homework modules os and sys

## Introduction
A python repository for practical course in © Bioinformatics Institute by Valeriia Ladyhina.
In this repository you will find utilits that are similar by their functional to Linux utilits.

## Main features
* cat.py
* ls.py
* mkdir.py
* rm.py
* sort.py
* tail.py
* wc.py

## cat.py 

### Functions: 
* open and print the whole file
* can be used in pipeline with other utilits for example _wc.py_

### Usage
`python cat.py [FILE] ` \n
FILE - input file \n
 -h, --help  show help message \n 
 
## ls.py 

### Functions: 
* print files that are located in the current directory

### Usage
`python ls.py [DIR] ` \n
DIR - path to the directory you want to check \n
 -h, --help  show help message \n
 -a --all    count all files including hidden ones  \n
 
## mkdir.py 

### Functions: 
* create directory

### Usage
`python mkdir.py [DIR] `
DIR - name of a directory to be created
 -h, --help  show help message
 -p --parents  no error if the directory already existed
 
## rm.py 

### Functions: 
* remove directory or file

### Usage
`python rm.py [PATH] `
PATH - path to a file or a directory that has to be removed
 -h, --help  show help message
 -r  recursively remove non-empty directory
 
## sort.py 

### Functions: 
* sort lines in file
* can be used in pipeline after cat

### Usage
`python sort.py [FILE] `
FILE - file that you want to sort
 -h, --help  show help message
 
## tail.py 

### Functions: 
* print last 10 lines of the file/files

### Usage
`python tail.py [FILE...] `
FILE - file that you want to print end of
 -h, --help  show help message
 -n will allow to prine one by one last 10 lines of multiple files
 
## wc.py 

### Functions: 
* words, lines or characters count in file

### Usage
`python wc.py [FILE...] `
FILE - file that you want to print end of
 -h, --help  show help message
 -w, --words words count
 -l, --lines kines count
 -c, --characyers characters count


## Authors and acknowledgements
#### Main contributor
* Valeriia Ladyhina

## Utilits __grep.py__ and __install.py__ are in the process of development.
