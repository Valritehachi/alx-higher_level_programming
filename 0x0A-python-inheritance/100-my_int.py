#!/usr/bin/python3

class MyInt(int):

    def __init__(self, value):
        self = value

    def __eq__(self, other):
        return (self - other != 0)

    def __ne__(self, other):
        return (self - other == 0)
 
