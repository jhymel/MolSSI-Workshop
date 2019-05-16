# Geometry Analysis Program

import numpy as np
import os
import sys

def calculate_distance(atom1,atom2):
	"""
	Calculate the distance between two atoms

	Parameters
	----------
	atom1: list
		A list of coordinates [x, y, z]
	atom2: list
		A list of coordinates [x, y, z]
	
	Returns
	-------
	bond_length: float
		The distance between atoms.

	Examples
	--------
	>>> calculate_distance([0,0,0], [0,0,1])
	1.0
	
	
	"""
	x_dist = atom1[0] - atom2[0]
	y_dist = atom1[1] - atom2[1]
	z_dist = atom1[2] - atom2[2]
	bond_length = np.sqrt(x_dist**2 + y_dist**2 + z_dist**2)
	return (bond_length)

def bond_check(bond_distance, minimum=0, maximum=1.5):
	"""
	Determines whether or not there is a bond between two atoms

	Parameters
	----------
	bond_distance: float
		Calculated distance between two atoms.
	minimum: float
		Minimum distance in order to be a bond.
	maximum: float
		Maximum distance in order to be a bond.

	Returns
	-------
	True: boolean
		bond_distance meets the specified minimum and maximum values in order to be a bond.
	False: boolean
		bond_distance does not meet the specified minimum and maximum values in order to be a bond.
		
	Example
	-------
	>>> bond_check(1.0, 0.5, 2.0)
	True

	"""
	
	# Check that bond_distance is a float
	if not isinstance(bond_distance, float):
		raise TypeError('bond_distance must be type float')
	if (bond_distance > minimum) and (bond_distance < maximum):
		return True
	else:
		return False

def open_xyz(filename):
	xyz_file = np.genfromtxt(fname=filename, skip_header=2, dtype='unicode')
	symbols = xyz_file[:0]
	coord = (xyz_file[:,1:])
	coord = coord.astype(np.float)
	return symbol, coord

if __name__ == '__main__':

	if len(sys.argv) < 2:
		raise IndexError('No file name given. Script requires an xyz file')

	structure = sys.argv[1]

	dist = np.genfromtxt(fname=structure, skip_header = 2, dtype = 'unicode')

	atoms = dist[:,0]

	for i in range(len(atoms)):
    		for j in range(len(atoms)):
        		#if (i != j):
        		    distance = np.sqrt(((float(dist[i,1])-float(dist[j,1]))**2)+((float(dist[i,2])-float(dist[j,2]))**2)+((float(dist[i,3])-float(dist[j,3]))**2))
        		    if (distance > 0) and (distance < 1.5):
        		        if (j > i):
        		            print(atoms[i] + ' to ' + atoms[j] + ': ' + '%.3f' %(distance))
        		            #print('%s to %s: %.3f' %(atoms[i], atoms[j], distance))





