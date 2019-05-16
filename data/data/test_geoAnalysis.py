"""
Tests for geoAnalysis.py
"""

import geoAnalysis as ga

def test_calculate_distance():
	coord1 = [0,0,2]
	coord2 = [0,0,0]
	
	observed = ga.calculate_distance(coord1, coord2)
	
	assert observed == 2.0

def test_bond_check_True():
	bond_length = 1.0
	min = 0.5
	max = 2.0
	
	observed = ga.bond_check(bond_length, min, max)
	
	assert observed == True


def test_bond_check_False():
	bond_length = 0.25
	min = 0.5
	max = 2.0
	
	observed = ga.bond_check(bond_length, min, max)
	
	assert observed == False