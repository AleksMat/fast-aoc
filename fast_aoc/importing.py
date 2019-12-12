"""
Module implementing importing utilities
"""
import importlib.util


def import_module(module_name, module_path):
    """ Imports a module from anywhere on file storage

    :param module_name: A name of a module
    :type module_name: str
    :param module_path: A module file path
    :type module_path: str
    """

    spec = importlib.util.spec_from_file_location(module_name, module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    return module
