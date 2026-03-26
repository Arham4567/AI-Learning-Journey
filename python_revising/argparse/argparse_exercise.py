import argparse

parser = argparse.ArgumentParser(description="Student Info")

parser.add_argument("name")
parser.add_argument("--age", type=int)
parser.add_argument("--city", default="Lahore")

args = parser.parse_args()

print("Name:", args.name)
print("Age:", args.age)
print("City:", args.city)