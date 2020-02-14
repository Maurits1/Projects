#!/usr/bin/env python3

import sys
import time
import numpy
import numba
from numba import jit

if (len(sys.argv) > 1):
    aantalUitTeZoeken = int(sys.argv[1])
else:
    aantalUitTeZoeken = 100

print(str(aantalUitTeZoeken))
# aantalUitTeZoeken = 10000

isGeenPrime = False
q = 0
laatstePrime = 3
startTijd=time.time()

primenummers = set([2, 3])

@jit(nopython=True)
def isPrimeFunc(x, primenummers):
    for pgetal in primenummers:
        p, q = divmod(x, pgetal)
        if q == 0:
            return False
    return True

@jit(nopython=True)
def primeZoeken(aantalTeDoen):
    getal = 3
    primenummers = set([2, 3])

    while(getal <= aantalTeDoen):
        if(isPrimeFunc(getal, primenummers)):
            primenummers.add(getal)
            laatstePrime = getal
        getal += 2
    return primenummers, laatstePrime


antwoord, laatstePrime = primeZoeken(aantalUitTeZoeken)

print("Laatst gevonden prime nummer: " + str(laatstePrime))
print("Totaal aantal primes gevonden: " + str(len(antwoord)))

print("")
# print("Aantal prime nummers in " + str(aantalTeDoen) +  ": " + str(len(primenummers)))
# print("Hoogste prime gevonden: " + str(laatstePrime))
print("Totale tijd: " + str(time.time()-startTijd) + " seconden")
