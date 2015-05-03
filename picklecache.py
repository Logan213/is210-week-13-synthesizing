#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Week 13 Synthesizing Tasks"""

import os
import pickle


class PickleCache(object):
    """Docstring."""

    def __init__(self, file_path='datastore.pkl', autosync=False):
        """Docstring."""
        self.__file_path = file_path
        self.__data = {}
        self.autosync = autosync
        self.load()

    def __setitem__(self, key, value):
        """Docstring."""
        self.key = key
        self.value = value
        self.__data[key] = value

    def __len__(self):
        """Docstring."""
        return len(self.__data)

    def __getitem__(self, key):
        """Docstring."""
        return self.__data[key]

    def __delitem__(self, key):
        """Docsting."""
        del self.__data[key]

    def load(self):
        """Docstring."""
        fexists = os.path.exists(self.__file_path)
        fsize = os.path.getsize(self.__file_path)
        if fexists and fsize > 0:
            fhandler = open(self.__file_path, 'r')
            mydata = pickle.load(fhandler)
            self.__data.update(mydata)
            fhandler.close()
