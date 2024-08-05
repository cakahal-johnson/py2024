# Write a function is_sheet_usable(sheet), that takes a numpy array. In the array, if a grid 
# location has a defect, the array will contain 1, otherwise it will contain 0. The function should 
# return True if the sheet can be used, otherwise False.

# Example:

def is_sheet_usable(sheet):
  # Assume that the sheet is usable by default
  usable = True
  # Loop through each row of the sheet
  for row in sheet:
    # Count the number of defects in the row
    defects = np.sum(row)
    # If the number of defects is more than 2, the sheet is not usable
    if defects > 2:
      usable = False
      break
  # Return the usability of the sheet
  return usable

sheet = np.array([
  [0, 0, 0, 0, 0],
  [0, 1, 1, 0, 0],
  [0, 1, 1, 0, 0],
  [0, 0, 0, 1, 1],
  [0, 0, 0, 1, 1]
])

is_sheet_usable(sheet) #-> False

# Error checking:

import numpy as np

def error_checking(sheet):
  # If sheet is not a numpy ndarray, raise TypeError
  if not isinstance(sheet, np.ndarray):
    raise TypeError("sheet must be a numpy ndarray")
  # If sheet has a shape other than 100×100, raise ValueError
  if sheet.shape != (100, 100):
    raise ValueError("sheet must have a shape of 100×100")
  # If sheet contains values other than 0 or 1, raise ValueError
  if not np.all(np.isin(sheet, [0, 1])):
    raise ValueError("sheet must contain only 0 or 1 values")
