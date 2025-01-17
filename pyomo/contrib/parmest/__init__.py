#  ___________________________________________________________________________
#
#  Pyomo: Python Optimization Modeling Objects
#  Copyright (c) 2008-2022
#  National Technology and Engineering Solutions of Sandia, LLC
#  Under the terms of Contract DE-NA0003525 with National Technology and
#  Engineering Solutions of Sandia, LLC, the U.S. Government retains certain
#  rights in this software.
#  This software is distributed under the 3-clause BSD License.
#  ___________________________________________________________________________

from pyomo.common.deprecation import relocated_module_attribute

relocated_module_attribute(
    'create_ef', 
    'pyomo.contrib.parmest.utils.create_ef', 
    '6.4.2', 
    '6.5.0')
relocated_module_attribute(
    'ipopt_solver_wrapper ', 
    'pyomo.contrib.parmest.utils.ipopt_solver_wrapper ', 
    '6.4.2', 
    '6.5.0')
relocated_module_attribute(
    'mpi_utils ', 
    'pyomo.contrib.parmest.utils.mpi_utils ', 
    '6.4.2', 
    '6.5.0')
relocated_module_attribute(
    'scenario_tree ', 
    'pyomo.contrib.parmest.utils.scenario_tree ', 
    '6.4.2', 
    '6.5.0')


