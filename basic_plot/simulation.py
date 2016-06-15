"""
.. class:: Simulation
   :platform: Unix
   :synopsis: Defines the Simulation class representing a single GS2 simulation.

"""

import os

import numpy as np
from netCDF4 import Dataset

class Simulation():
    """ Represents a single GS2 simulation."""

    def __init__(self, options):
        """
        Instantiate the Simulation object.

        Parameters
        ----------

        options : dict
            Dictionary of options. The options required for initialization are
            documented below.
        'ifile' : str, optional
            Path to GS2 input file.
        'ipath' : str, optional
            Path to GS2 run folder.
        'opath' : str, optional
            Path where output should be written. Default will be in the GS2 run
            folder determined either from 'ifile' or 'ipath'.
        """

        if 'ifile' in options:
            self.nc_file = Dataset(options['ifile'], 'r')
        elif 'ipath' in options:
            input_file_path = find_gs2_input_file(options['ipath'])
            self.nc_file = Dataset(input_file_path, 'r')

    def find_gs2_input_file(run_folder_path):
        """Find the GS2 output file given the path to the run directory."""

        files = os.listdir(run_folder_path)

        for f in files:
            if f.find('.out.nc') != -1:
                return f

    def run(options):
        """Run some commands."""
        pass

    def plot(options):
        """Plot data from a GS2 output file."""
        graph_data = get_graph_data(options)

    def write(options):
        """Write GS2 data to a file in the output directory."""
        pass

    def return_results(options):
        """Return results to the caller."""
        pass

    def get_graph_data(options):
        """
        Read data for an individual graph.

        Returns:
        --------

        graph_data : dict
            A dictionary containing all the data for the graph specified in
            the options dictionary.

        """
        graph_data = {}

        var_obj = self.nc_file.variables[options['var']]
        dims = var_obj.dimensions

        graph_data['x'] = self.nc_file.variables[dims[0]][:]
        graph_data['y'] = var_obj[:]

        return graph_data



