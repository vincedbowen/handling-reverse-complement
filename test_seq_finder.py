import pytest
from seq_finder import * 


def test_seq_in_db_simple():
    assert find_substring('attgcat', 'at') == True
    assert find_substring('attgcat', 'g') == True
    assert find_substring('attgcat', 'attgcat') == True
    assert find_substring('attgcat', 'att') == True
    assert find_substring('attgcat', 'tgca') == True
    assert find_substring('attgcat', 'cat') == True

def test_seq_in_reverse_complement_simple():
    assert find_substring('attgcat', 'atg') == True
    assert find_substring('attgcat', 'aa') == True
    assert find_substring('attgcat', 'atgcaat') == True
    assert find_substring('attgcat', 'gcaa') == True
    assert find_substring('attgcat', 'caa') == True
    assert find_substring('attgcat', 'aat') == True

def test_seq_not_in_db_simple():
    assert find_substring('attgcat', 'ccatgc') == False
    assert find_substring('attgcat', 'ttagc') == False
    assert find_substring('attgcat', 'ccatg') == False
    assert find_substring('attgcat', 'atcgcat') == False
    assert find_substring('attgcat', 'atgcata') == False
    assert find_substring('attgcat', 'taa') == False

def test_assignment_examples():
    assert find_substring('ATTAAAGGTTTATACCTTCCCAGGTAACAAACCAACCAACTTTCGATCTCTTGTAGATCTGTTCTCTAAA', 'TTAAAGGT') == True
    assert find_substring('ATTAAAGGTTTATACCTTCCCAGGTAACAAACCAACCAACTTTCGATCTCTTGTAGATCTGTTCTCTAAA', 'GGATCCT') == False
    assert find_substring('TTTAGAGAACAGATCTACAAGAGATCGAAAGTTGGTTGGTTTGTTACCTGGGAAGGTATAAACCTTTAAT', 'GGATCCT') == False
    assert find_substring('TTTAGAGAACAGATCTACAAGAGATCGAAAGTTGGTTGGTTTGTTACCTGGGAAGGTATAAACCTTTAAT', 'ACCTTTAA') == True
    assert find_substring('TTTAGAGAACAGATCTACAAGAGATCGAAAGTTGGTTGGTTTGTTACCTGGGAAGGTATAAACCTTTAAT', 'TTAAAGGT') == True
    assert find_substring('ATTAAAGGTTTATACCTTCCCAGGTAACAAACCAACCAACTTTCGATCTCTTGTAGATCTGTTCTCTAAA', 'ACCTTTAA') == True

def test_funky_resets():
    assert find_substring('aaaagta', 'aag') == True
    assert find_substring('aaaagta', 'aaaaaa') == False
    assert find_substring('aaaagta', 'ctttt') == True
    assert find_substring('agtaaaa', 'tta') == True


if __name__ == "__main__":
    pytest.main()