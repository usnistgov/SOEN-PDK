''' Translation functions that take Cells/Devices in different types of languages
    and convert them to Cells/Devices in other languages
'''
import os
import pya


def celltype_to_write_unboundmeth(celltype):
    ''' Takes a class that represents a layout Cell and gives its class' write method.
        (there is always some version of this, although some languages don't explicitly call it Cell)

        This uses try-excepted on-the-fly importing because not everybody is going to have every language installed.
        But if they don't, then their celltype is not going to be from that language.
    '''
    def not_supported_error(language_name):
        raise NotImplementedError(('The translator does not yet support {}.\n'.format(language_name)
                                    + 'Supported languages are: pya, phidl\n'
                                    + 'Future support will include: gdspy, nazca, ipkiss'))

    try: import pya  # ok I know we already imported this, but in the future it can also be on-the-fly (i.e. converting phidl to nazca)
    except ImportError: pass
    else:
        if issubclass(celltype, pya.Cell):
            return pya.Cell.write

    try: import phidl
    except ImportError: pass
    else:
        if issubclass(celltype, phidl.Device):
            write_default = phidl.Device.write_gds
            # we don't want that extra hierarchy layer, 'topcell', so give an extra argument to prevent it
            return lambda *args, **kwargs: write_default(*args, **kwargs, auto_rename=False)

    try: import gdspy
    except ImportError: pass
    else:
        not_supported_error('gdspy')

    try: import nazca
    except ImportError: pass
    else:
        not_supported_error('nazca')

    try: import ipkiss
    except ImportError: pass
    else:
        not_supported_error('ipkiss')

    raise TypeError('celltype: {} is not recognized as a layout cell object'.format(celltype.__name__))


def anyCell_to_pyaCell(initial_cell, pya_cell):
    ''' Transfers the geometry of some initial_cell into a klayout format.
        This initial_cell can be any type of layout object, even in a different language.

        It must provide a way to write its geometry to a layout and have only one top cell.
        This function will figure out what that way is, based on the class of initial_cell.
        The supported types and their mapping to write methods are contained in celltype_to_write_unboundmeth.
    '''
    write_unboundmeth = celltype_to_write_unboundmeth(type(initial_cell))
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

