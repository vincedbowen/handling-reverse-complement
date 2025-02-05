import argparse


def find_substring(dna_sequence, search_str):
    # Generate the complement of the current base
    complement = {'a': 't', 't': 'a', 'c': 'g', 'g': 'c'}

    # Generate lengths of sequences to save a little bit of time in the for loop
    dna_len = len(dna_sequence)
    search_len = len(search_str)

    # Coerce sequences to lower cases
    dna_sequence = dna_sequence.lower()
    search_str = search_str.lower()

    # Set the search query iterator to begin searching at the beginning of the search string 
    forward_iterator = 0
    backward_iterator = 0

    for forward in range(dna_len):
        # Set the backwards pointer
        backward = dna_len - 1 - forward 

        # Check individual base pairs in forward direction 
        if(search_str[forward_iterator] == dna_sequence[forward]):
            # if the forward iterator gets to the last element and it matches, the whole sequence is in the database so return 
            if(forward_iterator == search_len - 1):
                print(f"Match found in DNA sequence at slice: {forward - search_len + 1}, {forward}")
                return True
            # Increase the accessor of the search string
            forward_iterator += 1
        else: 
            # Reset the accessor of the search string 
            if forward_iterator > 0:
                forward_iterator = 0
                # Check if current base starts a new match
                if search_str[0] == dna_sequence[forward]: 
                    forward_iterator = 1

        # Check backwards with the reverse compliment 
        if(complement[(search_str[backward_iterator])] == (dna_sequence[backward])):
            if(backward_iterator == search_len - 1):
                print(f"Match found in reverse complement sequence at slice: {backward - 1}, {backward + search_len - 2}")
                return True
            backward_iterator += 1
        else:
            # Reset the accessor of the search string that moves backwards
            if backward_iterator > 0:
                backward_iterator = 0
                if complement[(search_str[0])]== dna_sequence[backward]:
                    backward_iterator = 1

    return False


def main():
    # Get arguments from the command line
    parser = argparse.ArgumentParser()
    parser.add_argument("-db", "--database", help = "database sequence")
    parser.add_argument("-q", "--query", help = "query sequence")
    args = parser.parse_args()
    db = args.database
    query = args.query

    # Find the query sequence in the database
    find_substring(db, query)

if __name__ == "__main__":
    main()