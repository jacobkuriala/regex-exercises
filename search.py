"""
Search Exercises

These functions return a list of strings matching a condition.

"""
import re

with open('dictionary.txt') as dict_file:
    dictionary = dict_file.read()


def get_extension(filename):
    """Return the file extension for a full file path."""
    result = re.search(r'(\.)'                  # locate the dot
                       r'(?P<extn>[\w\d]+)$',   # create a named gp that can be used to return the extension
                       filename, re.VERBOSE)
    if (result):
        return result.group('extn')
    else:
        return False


def tetravocalic(dictionary=dictionary):
    """Return a list of all words that have four consecutive vowels."""
    return list(re.findall(r'\b.*?[AEIOUaeiou]{4}.*?\b', dictionary))



def hexadecimal(dictionary=dictionary):
    """Return a list of all words consisting solely of the letters A to F."""
    return re.findall(r'\b[A-Fa-f][A-Fa-f]*\b', dictionary)


def hexaconsonantal(dictionary=dictionary):
    """Return a list of all words with six consecutive consonants."""
    return re.findall(r'\b.*[^AEIOUaeiou]{6}.*\b', dictionary)


def possible_words(partial_word, dictionary=dictionary):
    """
    Return possible word matches from a partial word.

    Underscores in partial words represent missing letters.  Examples:
        C_T (cat, cot, cut)
        _X_ (axe)
    """
    partial_re = re.sub(r'_', r'.',partial_word)
    searchstr = r'\b' + partial_re + r'\b'
    return re.findall(searchstr, dictionary, re.IGNORECASE)

#not working
def five_repeats(letter, dictionary=dictionary):
    """Return all words with at least five occurrences of the given letter."""
    """So i think this answers what non-capturing gp does.
    (it does not explicitly extract what a group captures and
     retains what it matches within the re in which it exists."""
    srhstr = r'\b[\w]*?(?:' + letter + r'[\w]*?){5,}\b'
    return re.findall(srhstr, dictionary)

def abbreviate(phrase):
    """Return an acronym for the given phrase."""

    return ''.join(letter.upper() for letter in re.findall(r"""\b[\w\d]     #check for starting alphanumeric characters
                                                           |[A-Z]           #check for capitalized characters
                                                           """
                                                           , phrase, flags=re.VERBOSE))



def palindrome5(dictionary):
    """Return a list of all five letter palindromes."""
    #re.findall(r'\b(?P<first>.)(?P<second>.)(?P<third>.)(?P=second)(?P=first)\b',dictionary)
    return [match.group() for match in re.finditer(r'\b(\w)(\w)(\w)\2\1\b', dictionary)]


def double_double(dictionary=dictionary):
    """
    Return words with a double repeated letter with one letter between.

    Example double double words:
    - freebee
    - assessed
    - voodoo
    check finditer
    """
    #re.findall(r'\b.*?(\w)\1.\1\1.*?\b',dictionary)
    return [match.group() for match in re.finditer(r'\b.*?(\w)\1.\1\1.*?\b', dictionary)]



def repeaters(dictionary=dictionary):
    """
    Return words that consist of the same letters repeated two times.

    Example double double words:
    - tutu
    - cancan
    - murmur
    """
    return [match.group() for match in re.finditer(r'\b(\w+?)\1\b', dictionary)]
