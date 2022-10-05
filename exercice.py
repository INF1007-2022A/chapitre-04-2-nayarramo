#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

def get_first_part_of_name(name):
	premier = name.split("-")[0]
	nom = premier[0].upper() + premier[1:].lower()
	return f"Bonjour {nom}"

def get_random_sentence(animals, adjectives, fruits):
	
	return f"Aujourd’hui, j’ai vu un {animals[random.randrange(0,len(animals))]} s’emparer d’un panier {adjectives[random.randrange(0,len(adjectives))]} plein de {fruits[random.randrange(0,len(fruits))]}."

def encrypt(text, shift):
	return ""

def decrypt(encrypted_text, shift):
	return ""


if __name__ == "__main__":
	parrot = "jEaN-MARC"
	print(f"Pour {parrot}, on a '{get_first_part_of_name(parrot)}'.")

	animals = ("chevreuil", "chien", "pigeon")
	adjectives = ("rouge", "officiel", "lourd")
	fruits = ("pommes", "kiwis", "mangues")
	print(get_random_sentence(animals, adjectives, fruits))
	
	print(encrypt("ABC", 1))
	print(encrypt("abc 123 XYZ", 3))
	print(decrypt("DEF 123 ABC", 3))
