''' All of these things are not specific to this technology.
    Eventually, this module could be part of an independent PDK specification package.

    It is a bad idea to have this "python" directory permanently because
    this is a technology specification package, not a functional codebase.
'''
# Todo: handle TypeList and TypeLayer arguments
# Going to be difficult to handle: arguments that are other phidl.Device objects or functions

import pya
import os

def cellname_to_kwargs(cellname):
    ''' Converts the naming convention for parameter-based cell naming back into a dict of kwargs '''
    # this function has not been tested yet
    func_kwargs = dict()
    func_name, paramstr = cellname.split('__')  # double underscore has been sanitized
    for oneparamstr in paramstr.split('_'):  # todo: unsanitize _ and =
        name, val = oneparamstr.split('=')
        try:
            val = int(val)
        except ValueError:
            try:
                val = float(val)
            except ValueError:
                pass
        func_kwargs[name] = val
    return func_kwargs


def pytype_to_PCelltype(arg_type):
    # this has been tested only with floats so far
    if issubclass(arg_type, int):
        return pya.PCellDeclarationHelper.TypeInt
    if issubclass(arg_type, float):
        return pya.PCellDeclarationHelper.TypeDouble
    if issubclass(arg_type, (list, tuple)):
        return pya.PCellDeclarationHelper.TypeList
    if issubclass(arg_type, str):
        return pya.PCellDeclarationHelper.TypeString
    if issubclass(arg_type, bool):
        return pya.PCellDeclarationHelper.TypeBoolean
    if issubclass(arg_type, NoneType):
        return pya.PCellDeclarationHelper.TypeNone


import inspect
def my_argspec(function):
    signature = inspect.signature(function)
    args = list()
    kwargs = dict()
    for key, param in signature.parameters.items():
        kwargs[key] = param.default
    return args, kwargs


class WrappedPCell(pya.PCellDeclarationHelper):
    ''' I think this is not specific to phidl implementation. It just needs some function.
        Oh wait, yes it is (barely) because of write_gds.
    '''
    generating_function = None

    def kwarg_to_param(self, key, default=None):
        self.param(key, pytype_to_PCelltype(type(default)), key, default=default)

    def __init__(self, generating_function):
        self.generating_function = generating_function
        super().__init__()
        args, kwargs = my_argspec(self.generating_function)
        for arg in args:
            self.kwarg_to_param(arg)
        for key, default in kwargs.items():
            self.kwarg_to_param(key, default)

    def display_text_impl(self):
        text = self.generating_function.__name__ + '_'
        for pdecl, pval in zip(self.get_parameters(), self.get_values()):
            # sanitize _'s and ='s
            if isinstance(pval, str):
                pval.replace('_', '[_]')
                pval.replace('=', '[=]')
            text += '_{}={}'.format(pdecl.name, pval)
        return text

    def get_params_as_kwargs(self):
        # todo: handle non-keyword args
        all_args = list()
        all_kwargs = dict()
        for pdecl, pval in zip(self.get_parameters(), self.get_values()):
            all_kwargs[pdecl.name] = pval
        return all_args, all_kwargs

    def produce_impl(self):
        tempfile = os.path.realpath('temp.gds')
        # Produce the geometry
        args, kwargs = self.get_params_as_kwargs()
        phidl_Device = self.generating_function(*args, **kwargs)
        phidl_Device.write_gds(tempfile, auto_rename=False)

        # Load the geometry into a klayout format
        templayout = pya.Layout()
        templayout.read(tempfile)
        tempcell = templayout.top_cell()
        os.remove(tempfile)

        # Import the new cell into this pcell implementation
        self.cell.name = tempcell.name
        self.cell.copy_tree(tempcell)


class WrappedLibrary(pya.Library):
    tech_name = None
    all_funcs_to_wrap = None
    description = None

    def __init__(self):
        if self.tech_name is None:
            raise NotImplementedError('WrappedLibrary must be subclassed.')

        print("Initializing '%s' Library." % self.tech_name)

        # Not doing fixed GDS in this Library

        # Create all the new klayout-format PCells
        for func in self.all_funcs_to_wrap:
            self.layout().register_pcell(func.__name__, WrappedPCell(func))  # generic version

        self.register(self.tech_name)

        if int(pya.Application.instance().version().split('.')[1]) > 24:
            # KLayout v0.25 introduced technology variable:
            self.technology = self.tech_name
