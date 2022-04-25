# cp2kpy

A collection of python scripts used for running CP2k calculations

# vasp_xyz.py

A python script that convert *.vasp generated from VESTA (File > export data > *.vasp (Cartesian, convert to primitive cell)) 

How to use:

from vasp_xyz import *

vasp_to_xyz('unit_cell.vasp')

source: https://github.com/compchem-cybertraining/Tutorials_CP2K/tree/master/0_structure_preparation/3_BA2_PbI4

# xyz_shift.py

A python script that shift XYZ coordinate by c Å.
