#!/usr/bin/python2.7

'''
Created on June 20, 2011

@licence GNU GPL v3+
@author: Jeroen De Dauw < jeroendedauw@gmail.com >

http://www.khanacademy.org/exercises?exid=divisibility
'''
import getopt
import sys
import itertools
from Crypto.Util.number import isPrime

def getJoinedFactorials( lists ):
    if len( lists ) < 2:
        return lists

    for item in lists[0]:
        if reduce( lambda inList, lst: inList and item in lst, lists[1:], True ):
            for lst in lists[1:]:
                lst.remove( item )

    return list( itertools.chain( *lists ) )

def getNextPrime( lowerBound ):
    ''' Lower bound not included '''
    nextPrime = 0
    lowerBound = long( lowerBound )

    while nextPrime == 0:
        lowerBound += 1
        if isPrime( lowerBound ):
            nextPrime = lowerBound

    return nextPrime

def getDivisorsForNumber( number ):
    divisors = [1]
    currentDivisor = 2

    while number > 1:
        while ( number % currentDivisor ) == 0:
            number /= currentDivisor
            divisors.append( currentDivisor )
        currentDivisor = getNextPrime( currentDivisor )

    return divisors

def getSmallestMultiple( numbers, answers ):
    factorization = getJoinedFactorials( [ getDivisorsForNumber( number ) for number in numbers ] )

    for answer in answers:
        allowedDivisors = list( factorization ) # Make an actual copy so stuff does not get removed from original list.
        divisors = getDivisorsForNumber( answer )
        isCorrect = True

        for divisor in divisors[1:]:
            if divisor in allowedDivisors:
                allowedDivisors.remove( divisor )
            else:
                isCorrect = False
                break

        if isCorrect:
            return answer

    return 0

def requestNumbers():
    numbers = {}
    print "Enter the numbers for which you want to find the smallest multiple, space separated."
    numbers['divisors'] = [ int( j ) for j in raw_input().split( " " ) ]
    print "Enter the answers to validate."
    numbers['answers'] = [ int( j ) for j in raw_input().split( " " ) ]
    return numbers

def show_help():
    print """
Divisibility.py [-? help]

Finds the smallest common multiple.

  -?, --help
                Shows this help.
                
Example: $ python Divisibility.py 4242 4 2 
    """

def main():
    try:
        opts, arg = getopt.getopt( sys.argv[1:], "?", ["help"] )
    except getopt.GetoptError, err:
        print str( err )
        show_help()
        sys.exit( 2 )

    for opt, arg in opts:
        if opt in ( "-?", "--help" ):
            show_help()
            sys.exit()
        else:
            assert False, "unhandled option"

    while True:
        numbers = requestNumbers()
        answer = getSmallestMultiple( numbers['divisors'], numbers['answers'] )
        print "All numbers divisible by both {} are also divisible by {}".format( numbers['divisors'], answer )

if __name__ == '__main__':
    main()
