# Handling Reverse Complement

This algorithm allows the searching of a DNA sequence while only storing one copy of the DNA sequence and one copy of the search query. Additionally, the algorithm will find the string no matter the combination of original sequence or reverse complement sequence in the database of search query. The only requirement is that both the database and search query are inputted from 5 prime to 3 prime. 

## Getting Access
1. Clone the repository to your local machine
2. `cd handling-reverse-complement`
3. `pip install -r requirements.txt`

## Tests

There are 5 test suites, equating to 28 individual tests. The tests can be run with 
```
pytest test_seq_finder.py -v
```

## Running with your own Database and Search Query
If you want to use your own DNA sequence and search query, you can run 
```
python seq_finder.py -db <your sequence> -q <your search query>
```
The script will print the indices of where the query is found, or nothing if it is not in the sequence. Here is an example
```
python seq_finder.py -db attgcat -q atg

Match found in reverse complement sequence at slice: 3, 5
```