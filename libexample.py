# pylint: disable=invalid-name
# pylint: disable=missing-function-docstring
# pylint: disable=missing-module-docstring

import os
import sys
from importlib.machinery import SourceFileLoader
from importlib.util import module_from_spec, spec_from_loader


def import_src(name, path):
    """Import a python module without a trailing '.py' file name extension."""
    spec = spec_from_loader(name, SourceFileLoader(name, path))
    module = module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def rm_fr(path):
    try:
        os.removedirs(path)
    except FileNotFoundError:
        pass
