''' Translation functions that take Cells/Devices in different types of languages
    and convert them to Cells/Devices in other languages
'''

import os
import pya

def anyCell_to_pyaCell(initial_cell, pya_cell, write_unboundmeth=None):
    ''' Transfers the geometry of some initial_cell into a klayout format.
        This initial_cell can be any type of layout object, even in a different language.
        It must provide a way to write its geometry to a layout and have only one top cell.

        write_unboundmeth is a callable thing that will take the initial_cell and a filename,
        and save a gds at that location. This is typically a method of the initial_cell's class.

        For example: if type(initial_cell) == phidl.Device, then write_unboundmeth == Device.write_gds

        If write_unboundmeth is None, we will try to guess what it is based on the type of the initial_cell.
    '''
    # if write_unboundmeth is None:
    #     write_unboundmeth = celltype_to_write_unboundmeth(type(initial_cell))
    # Save the geometry of the initial cell
    tempfile = os.path.realpath('temp_externalCell_to_pyaCell.gds')
    write_unboundmeth(initial_cell, tempfile)
    # Import the gds into pya.Cell format
    templayout = pya.Layout()
    templayout.read(tempfile)
    tempcell = templayout.top_cell()
    os.remove(tempfile)
    # Transfer the geometry of the imported cell to the one specified
    pya_cell.name = tempcell.name
    pya_cell.copy_tree(tempcell)
    return pya_cell


def phidlDevice_to_pyaCell(initial_cell, pya_cell):
    ''' The phidl version of anyCell_to_pyaCell that gets the correct write method '''
    from phidl import Device
    write_default = Device.write_gds
    # we don't want that extra hierarchy layer, 'topcell', so give an extra argument to prevent it
    write_unboundmeth = lambda *args, **kwargs: write_default(*args, **kwargs, auto_rename=False)
    return anyCell_to_pyaCell(initial_cell, pya_cell, write_unboundmeth)


def pyaCell_to_pyaCell(initial_cell, pya_cell):
    ''' This is a dumb function. You would never do this.
        It's just for the purpose of illustrating abstraction with anyCell_to_pyaCell
    '''
    write_unboundmeth = pya.Cell.write
    return anyCell_to_pyaCell(initial_cell, pya_cell, write_unboundmeth)
