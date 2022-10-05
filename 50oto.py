import random
import math

alphabeta = [
    'a', 'i', 'u', 'e', 'o',
    'ka', 'ki', 'ku', 'ke', 'ko',
    'ga', 'gi', 'gu', 'ge', 'go',
    'sa', 'shi', 'su', 'se', 'so',
    'za', 'ji', 'zu', 'ze', 'zo',
    'ta', 'chi', 'tsu', 'te', 'to',
    'da', 'de', 'do',
    'na', 'ni', 'nu', 'ne', 'no',
    'ha', 'hi', 'fu', 'he', 'ho',
    'ba', 'bi', 'bu', 'be', 'bo',
    'pa', 'pi', 'pu', 'pe', 'po',
    'ma', 'mi', 'mu', 'me', 'mo',
    'ya', 'yu', 'yo',
    'ra', 'ri', 'ru', 're', 'ro',
    'wa', 'wo',
    'n']

def main():
    random.shuffle(alphabeta)
    lw = 10
    nlines = math.ceil(len(alphabeta) / lw)
    for i in range(nlines):
        print('\t'.join(alphabeta[lw*i:min([lw*(i+1),len(alphabeta)])]))

if __name__ == '__main__':
    main()