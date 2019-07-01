import re

if __name__ == '__main__':
	names = []
	N = int(input().strip())
	for a0 in range(N):
    	firstName,emailID = input().strip().split(' ')
    	firstName,emailID = [str(firstName),str(emailID)]
    	if emailID.endswith('@gmail.com'):
        	names.append(firstName)

for name in sorted(names):
    print(name)