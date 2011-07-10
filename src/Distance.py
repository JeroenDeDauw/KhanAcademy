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

def findRouteDistance( points ):
    if len( points ) < 2:
        return 0

    distance = 0
    previousPoint = points[0]

    for point in points[1:]:
        distance += findDistance( previousPoint, point )
        previousPoint = point

    return distance

def findDistance( start, end ):
    return sqrt( reduce( lambda sum, pair : sum + abs( pair[0] - pair[1] ) ** 2, zip( start, end ), 0 ) )

def show_help():
    print """
Distance.py [-? help]

Find the distance between sets of coordinates in n-space.

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

    print findRouteDistance( parseRoute( raw_input() ) )

if __name__ == '__main__':
    main()
