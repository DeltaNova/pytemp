#!/usr/bin/env python
################################################################################
#Python Temperature Converter - Author: Matthew Tunstall
#-------------------------------------------------------------------------------
#Aim: To take a command line temperature value and convert it to another scale
#Usage: pytemp -c -f 24  #Convert 24 degrees C to F
################################################################################
"""
Copyright (C) 2014  Matthew Tunstall

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
"""
################################################################################
USAGE = """
PyTemp - Python Temperature Converter
-------------------------------------
USAGE: pytemp.py [from units] [to units] [value]

Units:
------
-c or -C = Celsius
-f or -F = Fahrenheit
-k or -K = Kelvin

Example:
--------
To convert 20 Celsius to Fahrenheit
pytemp.py -c -f 20
"""
################################################################################
# Revision History
# ----------------
# 0.5 - Release Date [18/05/2014]
# 0.5 - Pylint 10/10 validation code cleanup
# 0.4 - Release Date [10/9/2006]
# 0.4 - Rewrite of codebase to clean and optimise
# 0.3 - Working bug free code
# 0.2 - Working code with some error checking
# 0.1 - Initial Code Outline
################################################################################
import sys     # To gain access to the argv command to access command line args.
ERROR = """
Something unexpected has occured for this message to be displayed.
Please submit a bug report \n"""
################################################################################
def abort(abort_message):
    """
    Abort routine to exit the program when error detected.
    """
    print USAGE
    print abort_message
    print "Application Terminating"
    sys.exit()
################################################################################
# Calculation Definitions
################################################################################
def f2c(temp):
    """
    Conversion Fahrenheit to Celsius.
    """
    from_scale = "Fahrenheit"
    to_scale = "Celsius"
    temp = temp - 32
    temp = temp*(5.0/9.0)
    return temp, from_scale, to_scale
################################################################################
def c2f(temp):
    """
    Conversion Celsius to Fahrenheit.
    """
    from_scale = "Celsius"
    to_scale = "Fahrenheit"
    temp = temp*(9.0/5.0)
    temp = temp + 32
    return temp, from_scale, to_scale
################################################################################
def f2k(temp):
    """
    Conversion Fahrenheit to Kelvin.
    """
    from_scale = "Fahrenheit"
    to_scale = "Kelvin"
    conv = f2c(temp) # conv is a tuple returned from the f2c() function.
    temp = conv[0] # The temperature is the first value in the tuple.
    temp = temp + 273.15
    return temp, from_scale, to_scale
################################################################################
def c2k(temp):
    """
    Conversion Celsius to Kelvin.
    """
    from_scale = "Celsius"
    to_scale = "Kelvin"
    temp = temp + 273.15
    return temp, from_scale, to_scale
################################################################################
def k2c(temp):
    """
    Conversion Kelvin to Celsius.
    """
    from_scale = "Kelvin"
    to_scale = "Celsius"
    temp = temp - 273.15
    return temp, from_scale, to_scale
################################################################################
def k2f(temp):
    """
    Conversion Kelvin to Fahrenheit.
    """
    from_scale = "Kelvin"
    to_scale = "Fahrenheit"
    conv = k2c(temp)    #conv is a tuple returned from the k2c() function
    temp = conv[0]      #The temperature is the first value in the tuple.
    temp = (temp*(9.0/5.0))+32
    return temp, from_scale, to_scale
################################################################################
# Conversion Calculations                                                      #
# -----------------------------------------------------------------------------#
# From              To Fahrenheit          To Celsius      To Kelvin           #
# Fahrenheit(F)     F                      (F-32)*(5/9)    (F-32)*(5/9)+273.15 #
# Celsius(C)        (C*(9/5))+32           C               C+273.15            #
# Kelvin(K)         (K-273.15)*(9/5)+32    K-273.15        K                   #
################################################################################
def getargs():
    """
    Get the command line arguments, check for the correct amount.
    """
    args = sys.argv[1:]  # Strip the first arg(the file name).
    argtest = []
    if args == argtest:
        abort("No arguments supplied")
    else:
        numargs = len(args)
        if numargs == 3:
            three_args = args
        elif numargs < 3:
            abort("Too few arguments supplied.")
        elif numargs > 3:
            abort("Too many arguments supplied.")
        else:
            abort(ERROR)
    return three_args
################################################################################
def lowerargs(args):
    """
    Take the arguments and convert to lower-case to aid processing.
    """
    low_args = []
    for arg in args:
        arg = arg.lower()
        low_args.append(arg)
    return low_args
################################################################################
def tofloat(arg):
    """
    Attempt to convert the input to a float. Return 1 if success, 0 for error.
    """
    try:
        arg = float(arg) # Execution moves to the else statement if successful.
    except ValueError:
        conversion_attempt = 0
    else:
        conversion_attempt = 1
    return conversion_attempt
################################################################################
def validtest1(args):
    """
    Check the argument types are in positions expected.
    """
    pos = []            # Position log, allows us to see which arg(s) validated
    for arg in args:
        pos.append(tofloat(arg))
    poschk = [0, 0, 1] # Ideal result, only the last arg will convert to a float
    if poschk == pos:
        args[2] = float(args[2]) # Make float conversion on last arg permanent
    else:
        abort("Invalid Set of Arguments")
    return args
################################################################################
def validtest2(args):
    """
    Check the arguments against those we are expecting. Abort if not.
    """
    argchk = ["-c", "-f", "-k"]
    testlist = [] # Create a test list to compare with argchk
    # Only the first two values need checking, we have already checked the third
    testlist.append(args[0])
    testlist.append(args[1])
    if args[0] == args[1]:
        abort("No point in converting to the same scale")
    arg_count = 0
    for item in testlist:
        if item in argchk:
            arg_count = arg_count + 1
    if arg_count != 2:
        abort("Invalid Set of Arguments")
################################################################################
def processargs(args):
    """
    Look at the arguments provided and select the correct conversion.
    """
    if args[0] == '-c':
        if args[1] == '-f':
            temp, from_scale, to_scale = c2f(args[2])
        else:
            temp, from_scale, to_scale = c2k(args[2])
    elif args[0] == '-f':
        if args[1] == '-k':
            temp, from_scale, to_scale = f2k(args[2])
        else:
            temp, from_scale, to_scale = f2c(args[2])
    elif args[0] == '-k':
        if args[1] == '-c':
            temp, from_scale, to_scale = k2c(args[2])
        else:
            temp, from_scale, to_scale = k2f(args[2])
    else:
        abort("Ooops, something has gone wrong")
    print str(args[2]) + ' ' + from_scale + ' = ' + str(temp) + " " + to_scale
################################################################################

def main():
    """
    pytemp.py main program loop
    """
    args = getargs()                #Get arguments from the command line
    args = lowerargs(args)          #Convert args to lower-case
    args = validtest1(args)         #Check arg types & positions
    validtest2(args)                #Checks arguments are valid
    processargs(args)               #Process Conversion
################################################################################
if __name__ == "__main__":
    # Someone is launching this directly
    main()
