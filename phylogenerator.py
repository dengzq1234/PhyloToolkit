#!/usr/bin/env python3

import random
import argparse

from ete4 import Tree

def parse_arguments():
    parser = argparse.ArgumentParser(description="Generate a random phylogenetic tree.")
    parser.add_argument("-n", "--number", type=int, help="Number of species.")
    parser.add_argument("-l", "--name-list", help="List of species names.")
    parser.add_argument("-m", "--model", type=str, choices=['yule', 'uniform'], default='yule', help="Random tree model.")
    parser.add_argument("-o", "--output", type=str, required=True, help="Output filename.")
    return parser.parse_args()


def parse_file_of_names(filename):
    with open(filename, "r") as f:
        return f.read().splitlines()
    
def generate_random_tree_by_number(count, model='yule'):
    names = [f"Taxa_{i}" for i in range(count)]
    return generate_random_tree(names, model)

def generate_random_tree(names, model='yule'):
    tree = Tree()
    tree.populate(size=len(names), names=names, dist_fn=random.random, support_fn=random.random)
    return tree

if __name__ == "__main__":
    args = parse_arguments()
    if args.name_list:
        names = parse_file_of_names(args.name_list)
        tree = generate_random_tree(names, args.model)
    elif args.number:
        tree = generate_random_tree_by_number(args.number, args.model)
    else:
        print("Please provide either a list of names or a number.")
        exit(1)

    if tree:
        tree.write(args.output, format_root_node=True)


