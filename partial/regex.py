import re
import readline

# NOMBRE*|APELLIDOS*|DNI*|EDAD|COLEGIO

if __name__ == "__main__":
	p = re.compile("^([a-z|A-Z]+)"
					"(\|[a-z|A-Z]+)"
					"(\|[0-9]{8})"
					"(\|[0-9]{2})"
					"(\|[a-z]*){1}$"
					)

	while(True):
		line = input('line: ')

		if(line == 'q'):
			break    

		if(p.match(line)):
			print('Yes')
		else:
			print('Not')