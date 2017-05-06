#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
# en python2 se requiere -*- coding: utf-8 -*-
# en python3 se requiere .encode("utf-8")

''' Resolucion de ejercicio T1000
https://docs.python.org/2/library/hashlib.html#module-hashlib
'''
import hashlib

def handShakeDecode(fullDocument):
    elementsString = fullDocument.split(";")
    robots = []
    for element in elementsString:
        aux = element.strip("[]").split(",")
        robots.append({"name": aux[0], "key": aux[2]})
    return robots

if __name__ == "__main__":

    mFile = open("handshakes.lst", "r")
    robots = handShakeDecode(mFile.read())
    mFile.close()

    fileWords = open("Spanish.dic", "r")
    for line in fileWords:
        coded = hashlib.sha1(line.replace('\n', '')).hexdigest()
        for element in robots:
            if coded in element["key"]:
                element["decoded"] = line
                print(element["name"]+"-"+element["decoded"])
