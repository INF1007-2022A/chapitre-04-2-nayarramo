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
	texte = ""
	for letter in text:
		if 97 <= ord(letter) <= 122-shift:
			texte += chr(ord(letter) + shift - 32)
		elif 122-shift <= ord(letter) <= 122:
			texte += chr(64+shift-(122-ord(letter)))
		elif 65 <= ord(letter) <= 90-shift:
			texte += chr(ord(letter) + shift)
		elif 90-shift <= ord(letter) <= 90:
			texte += chr(64+shift-(90-ord(letter)))
		else:
			texte+=letter

	return texte

def decrypt(encrypted_text, shift):
	texte = ""
	for letter in encrypted_text:
		if 97+shift <= ord(letter) <= 122:
			texte += chr(ord(letter) - shift - 32)
		elif 97 <= ord(letter) <= 97+shift:
			texte += chr(91-shift+(ord(letter)-97))
		elif 65+shift <= ord(letter) <= 90:
			texte += chr(ord(letter) - shift)
		elif 65 <= ord(letter) <= 65+shift:
			texte += chr(91-shift+(ord(letter)-65))
		else:
			texte+=letter
	return texte


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
