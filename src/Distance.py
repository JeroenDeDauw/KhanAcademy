#!/usr/bin/python2.7

'''
Created on July 10, 2011

@licence GNU GPL v3+
@author: Jeroen De Dauw < jeroendedauw@gmail.com >

http://www.khanacademy.org/exercises?exid=distance_formula
'''

import getopt
import sys
from math import sqrt

def parseRoute( points, pointSeparator = ",", coordSeparator = " " ):
    points = map( lambda coordinates : [float( nr ) for nr in coordinates.split( coordSeparator ) if len( nr ) > 0], points.split( pointSeparator ) )
    dimensionality = reduce( lambda maximun, coordinates: max( maximun, len( coordinates ) ), points, 0 )
    return map( lambda coordinates : tuple( coordinates + [0] * ( dimensionality - len( coordinates ) ) ), points )

def findRouteDistance( points, assquare = False ):
    if len( points ) < 2:
        return 0

    assquare = assquare and len( points ) == 2
    distance = 0
    previousPoint = points[0]

    for point in points[1:]:
        distance += findDistance( previousPoint, point, assquare )
        previousPoint = point

    return distance

def findDistance( start, end, assquare = False ):
    distance = reduce( lambda sum, pair : sum + ( max( pair ) - min( pair ) ) ** 2, zip( start, end ), 0 )
    return distance if assquare else sqrt( distance )

def show_help():
    print """
Distance.py [-? help]

Find the distance between sets of coordinates in n-space.

  --assquare
                Output the number that needs to be squared instead of the squared number if there are only 2 points.
  -?, --help
                Shows this help.
    """

def main():
    try:
        opts, arg = getopt.getopt( sys.argv[1:], "?", ["assquare", "help"] )
    except getopt.GetoptError, err:
        print str( err )
        show_help()
        sys.exit( 2 )

    assquare = False

    for opt, arg in opts:
        if opt in ( "-?", "--help" ):
            show_help()
            sys.exit()
        elif opt in ( "--assquare" ):
            assquare = True
        else:
            assert False, "unhandled option"

    sys.stdout.write( str( findRouteDistance( parseRoute( sys.stdin.readline() ), assquare ) ) )

if __name__ == '__main__':
    main()
