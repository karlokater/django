"""
argparse Tutorial. 
Kommandozeilen-Argumente parsen und nutzen
"""
import argparse

parser = argparse.ArgumentParser()
parser.epilog = "Nutzunghinweis: ...."
parser.add_argument("--name", type=str, required=True)
parser.add_argument("--age", type=int, required=True)

args = parser.parse_args()
name = args.name
age = args.age

print(name, type(age))