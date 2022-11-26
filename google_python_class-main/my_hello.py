# if you just run the script it'll print classic 'Hello World!'
# if you run the script with an argument, e.g. 'Mike', it'll print 'Hello Mike!'

import sys

def main():
	if len(sys.argv) >= 2:
		name = sys.argv[1]  # getting the name from a command line (the first argument)
	else:
		name = 'World'
	print(f'Hello {name}!')

# Standard boilerplate to call main() function
if __name__ == '__main__':
	main()
