#!/usr/bin/python2.7

'''
Created on June 22, 2011

@licence GNU GPL v3+
@author: Jeroen De Dauw < jeroendedauw@gmail.com >

http://www.khanacademy.org/exercises?exid=simplifying_radicals
'''
import getopt
import sys
from numpy.lib.scimath import sqrt

class Radical:

    def __init__( self, number = 0, order = 2, multiplier = 1 ):
        self.number = number
        self.order = order
        self.multiplier = multiplier

    def __repr__( self ):
        order = int( self.order ) if self.order % 1 == 0 else float( self.order )
        multiplier = int( self.multiplier ) if self.multiplier % 1 == 0 else float( self.multiplier )
        number = int( self.number ) if self.number % 1 == 0 else float( self.number )

        txt = "" if multiplier == 1 else str( multiplier )

        if number != 1:
            if multiplier != 1:
                txt += " x "
            root = "sqrt" if order == 2 else "{}root".format( order )
            txt += "{}( {} )".format( root, number )
        elif multiplier == 1:
            txt = "1"

        return txt

    def simplify( self ):
        devisors = self.get_possible_divisors()

        for devisor in reversed( devisors ):
            if self.number % devisor == 0:
                self.number /= devisor
                self.multiplier *= sqrt( devisor ) if self.order == 2 else pow( devisor, 1.0 / self.order )
                break

    def get_possible_divisors( self ):
        devisors = []
        base = 2

        while True:
            devisor = pow( base, self.order )

            if devisor <= self.number:
                devisors.append( devisor )
                base += 1
            else:
                break

        return devisors

def request_numbers():
    print "Enter the number, order of expression and multiplier, space separated, last 2 optional:"
    numbers = raw_input().split( " " )

    return ( 
        float( eval( numbers[0] ) ),
        2 if len( numbers ) < 2 else float( eval( numbers[1] ) ),
        1 if len( numbers ) < 3 else float( eval( numbers[2] ) )
    )

def show_help():
    print """
Divisibility.py [-? help]

Finds the smallest common multiple.

  -?, --help
                Shows this help.
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
        radical = Radical( *request_numbers() )
        radical.simplify()
        print radical.__repr__()

if __name__ == '__main__':
    main()
