#!/usr/bin/env python
#-*- coding: utf-8 -*-

from os.path import dirname, realpath, isfile
from json import dump, load


class JsonManagerProd:

    def __init__(self):
        self.path = dirname(realpath(__file__)) + '/'

    def create_json(self, file, dictProd):
        data = dictProd
        path_data_json = self.path + file

        with open(path_data_json, 'w') as f:
            dump(data, f, indent=2, separators=(',', ': '))

    def read_json(self, file):
        if isfile(self.path + file):
            with open(self.path + file) as f:
                data = load(f)
            return data
        else:
            return False
        

class JsonManagerClient:

    def __init__(self):
        self.path = dirname(realpath(__file__)) + '/'

    def create_json(self, file, dictClient):
        data = dictClient
        path_data_json = self.path + file

        with open(path_data_json, 'w') as f:
            dump(data, f, indent=2, separators=(',', ': '))

    def read_json(self, file):
        data = []
        if isfile(self.path + file):
            with open(self.path + file) as f:
                data = load(f)
            return data
        else:
            return False

class JsonManagerPurchases:

    def __init__(self):
        self.path = dirname(realpath(__file__)) + '/'

    def create_json(self, file, dictPurchases):
        data = dictPurchases
        path_data_json = self.path + file

        with open(path_data_json, 'w') as f:
            dump(data, f, indent=2, separators=(',', ': '))

    def read_json(self, file):
        data = []
        if isfile(self.path + file):
            with open(self.path + file) as f:
                data = load(f)
            return data
        else:
            return False





