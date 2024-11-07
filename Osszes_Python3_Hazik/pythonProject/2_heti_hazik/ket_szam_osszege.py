import sys

def osszeg(first_number, second_number):
	print(first_number+second_number)

def main():
	osszeg(int(sys.argv[1]),int(sys.argv[2]))

if __name__ == "__main__":
	main()