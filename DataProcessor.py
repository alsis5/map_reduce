#!/usr/bin/python
# -*- coding: utf-8 -*-

class DataProcessor:
    def __init__(self):
        pass

    def cleanStrip (self, strip):
        clean_strip = strip.lower()
        clean_strip = clean_strip.replace(".", " ")
        clean_strip = clean_strip.replace(",", " ")
        clean_strip = clean_strip.replace("\n", " ")
        clean_strip = clean_strip.replace("\t", " ")
        clean_strip = clean_strip.replace("à", "a")
        clean_strip = clean_strip.replace("À", "a")
        clean_strip = clean_strip.replace("È", "e")
        clean_strip = clean_strip.replace("è", "e")
        clean_strip = clean_strip.replace("É", "e")
        clean_strip = clean_strip.replace("é", "e")
        clean_strip = clean_strip.replace("Í", "i")
        clean_strip = clean_strip.replace("í", "i")
        clean_strip = clean_strip.replace("Ó", "o")
        clean_strip = clean_strip.replace("ó", "o")
        clean_strip = clean_strip.replace("Ò", "o")
        clean_strip = clean_strip.replace("ò", "o")
        clean_strip = clean_strip.replace("ç", "c")
        clean_strip = clean_strip.replace("\xc2\xb7", "·")
        clean_strip = clean_strip.replace("!", " ")
        clean_strip = clean_strip.replace("¡", " ")
        clean_strip = clean_strip.replace(":", " ")
        clean_strip = clean_strip.replace("?", " ")
        clean_strip = clean_strip.replace("¿", " ")
        clean_strip = clean_strip.replace("\"", " ")
        clean_strip = clean_strip.replace("»", " ")
        clean_strip = clean_strip.replace("(", " ")
        clean_strip = clean_strip.replace(")", " ")
        clean_strip = clean_strip.replace("«", " ")
        clean_strip = clean_strip.replace(";", " ")
        clean_strip = clean_strip.replace("- ", " ")
        clean_strip = clean_strip.replace(" -", " ")

        legal_chars = "abcdefghijklmnñopqrstuvwxyzç1234567890·'"
        for char in strip:
            if char not in legal_chars:
                char = ""

        return clean_strip
