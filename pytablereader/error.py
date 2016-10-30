# encoding: utf-8

"""
.. codeauthor:: Tsuyoshi Hombashi <gogogo.vm@gmail.com>
"""

from __future__ import absolute_import


class ValidationError(Exception):
    """
    Raised when data is not properly formatted.
    """


class InvalidNameError(Exception):
    """
    Base name error class.
    """


class InvalidTableNameError(InvalidNameError):
    """
    Raised when invalid table name used.
    """


class InvalidHeaderNameError(InvalidNameError):
    """
    Raised when table header name is invalid.
    """


class InvalidFilePathError(InvalidNameError):
    """
    Raised when invalid file path used.
    """


class InvalidDataError(ValueError):
    """
    Raised when data is invalid to load.
    """


class EmptyDataError(InvalidDataError):
    """
    Raised when data is not included valid table data.
    """


class OpenError(IOError):
    """
    Raised when failed to open a file.
    """


class LoaderNotFoundError(Exception):
    """
    Raised when appropriate loader not found.
    """
