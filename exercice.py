#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

def is_even_len(string):
	nb_lettre = 0
	for letter in string:
		nb_lettre +=1
	return nb_lettre % 2 ==0


def get_num_char(string, char):
	frequence = 0
	for letter in string:
		if letter == char:
			frequence += 1
	return frequence


def get_first_part_of_name(name):
	list = name.split("-")
	return "Bonjour" + " " + list[0].capitalize()


def get_random_sentence(animals, adjectives, fruits):
	return "Aujourd'hui, j'ai vu un " + animals[random.randrange(0,2)] + " s'emparer d'un panier " + adjectives[random.randrange(0,2)] + " plein de " + fruits[random.randrange(0,2)]


if __name__ == "__main__":
	spam = "Bonjour!"
	parity = "pair" if is_even_len(spam) else "impair"
	print(f"Le nombre de caractère dans la chaine '{spam}' est {parity}.")

	eggs = "Hello, world!"
	print(f"Le nombre d'occurrence de l dans '{eggs}' est : {get_num_char(eggs, 'l')}.")

	parrot = "jean-marc"
	print(f"Pour {parrot}, on a '{get_first_part_of_name(parrot)}'.")

	animals = ("chevreuil", "chien", "pigeon")
	adjectives = ("rouge", "officiel", "lourd")
	fruits = ("pommes", "kiwis", "bananes")
	print(get_random_sentence(animals, adjectives, fruits))
