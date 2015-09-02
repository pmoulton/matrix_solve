#!/usr/bin/env python

import argparse
import numpy as np
from numpy.linalg.linalg import LinAlgError
__author__ = "Paul Moulton"

def read_row(input_prompt):
	"""Reads a matrix row from standard input and returns a list of integers"""
	try:
		input_row = raw_input(input_prompt).split(" ")
	except EOFError as e:
		raise ValueError("Please enter a matrix row")

	# check for trailing space
	if input_row[-1] == "":
		input_row = input_row[:-1]

	return [int(item) for item in input_row]

def read_matrix():
	"""Reads a matrix from std.in and returns two matrices a, b in the form A * x = b"""
	print("\nInput an augmented matrix row by row")
	print("2x + y = 5 -> '2 1 5'")
	print("3x + 4y = 15 -> '3 4 15' \n")

	full_matrix = []

	# read first row of matrix
	input_row = read_row("Row 1: ")

	full_matrix.append(input_row)

	width = len(input_row)
	height = width - 1
	
	# read remaining height - 1 rows
	for row in range(1, height):
		input_row = read_row("Row {0}: ".format(row + 1))

		if len(input_row) == width:
			full_matrix.append(input_row)
		else:
			raise ValueError("Row {0} of length {1} does not equal original row length {2}".format(row + 1, len(input_row), width))	

	a = np.array([row[:-1] for row in full_matrix])
	b = np.array([row[-1] for row in full_matrix])
	return (a, b)

def solve_matrix(a, b):
	try:
		x = np.linalg.solve(a, b)
		return x
	except LinAlgError as e:
		print(e)

if __name__ == "__main__":

	parser = argparse.ArgumentParser(description="Run this script in Python interactively to solve a matrix")
	args = parser.parse_args()

	a, b = read_matrix()
	x = solve_matrix(a, b)
	print x
