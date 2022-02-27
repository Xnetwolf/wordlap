import time
import random
import os
import sys

def design():
	os.system("figlet -f small WORDLAP")
	print("")
	
def analyse(stringto):
	t1 = stringto.split("-")
	t2 = "".join([str(item) for item in t1])
	t = t2.split(" ")
	
	return t
	
def help():
	os.system("clear")
	os.system("figlet -f small WORDLAP-HELP")
	clear = "\033[1;14m"
	end = "\033[0m"
	violet = "\033[1;95m"
	red = "\033[1;91m"
	print(f"""
	This tool generate random words from provided chars or delfaut chars
	\033[1;95m## To use: \033[0m
		-help: Display that section 
		\033[1;91mNOTE: anyother command after -help will be shutdown and -help command is independant so It don't need -start command'\033[0m
		
		\033[1;14m-start\033[0m: get system ready for generating + in front of each querie
		\033[1;95m## Generate option\033[0m
		\033[1;14m-generate_lenght n\033[0m: n is the lenght you want for generated words to have
		{red}-double_lenght n1_n2: generatw words from n1 lenght to n2 lenght and make sure n1<n2(n1 smaller than n2) **This command is not yet functionnal{end}
		{violet}## output
		{clear}-output filename{end}: where genetated words will be saved. 
		{violet}## Customize Char to use
		{clear}-char (start typing your chars with no space between them) e.g: -char qwertzuiop+×÷=%/\$€£@*!{end}
		Make it as long as possible
		{violet}## Format of commands
		#For custom char{end}
		-start -[Generate option] -output [filename] -char [characters]
		{violet}#For delfaut char{end}
		-start -[Generate option] -output [filename]
		
		Don't worry the program detect if -char command is present or not omiting that command make program to use delfaut 
	""")
def generate_lenght(lenght, savefile, letters):
	
	#somw old codes
	r =  int(lenght)
	start = 1
	word = " "	
	f = open(savefile, "w")
	r = r + 1
	while start > 0:
		while len(word) < int(r):
				v = random.choice(letters)
				word = word + v
				while len(word) == int(r):
				      f.write(word +"\n")
				      word = " "
def double_lenght(lenght, savefile, letters):
	print("This function is not yet ready, bye")
	time.sleep(3)
	main()
	
def about():
	os.system("clear")
	os.system("figlet -f small ABOUT")
	print("""
	This tool was first created by \033[1;91mXnetwolf\033[0m then upgade by \033[1;92mAnonyminHack5\033[0m
	And a new version and more powerfull comes back 
upgrade by \033[1;91mXnetwolf\033[0m
	
	Thanks for Coming that way to know from where this 
tool come from
If you got any issue feel free to contact me(\033[1;91mXnetwolf\033[0m)
	
	\033[1;95m ##Contribute \033[0m
\033[1;93m Monero \033[0m: 4AjmBwYjyBvCthXeUUvymdfnaZyjJG6spTHetqgziEasc5N5LB6HkZ2aGBTYfHTp9X1SqugDxib5dM24dJg8A2eHURpxyRu
	""")

def main():
	design()
	inp = input("μ~> ")
	if inp == "about":
		about()
	inp_2 = analyse(inp)
	if inp_2[0] == "help" or inp == "help":
		help()
		sys.exit()
	elif inp_2[0] == "start":
		if inp_2[1] == "generate_lenght":
			lenght = inp_2[2]
			if inp_2[3] == "output":
				output = inp_2[4]
				if inp_2[5] == "char":
					letters = inp_2[5]
				else:
					letters = ("qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890@*!#:;&_()-',.?+×÷=%/\$€£￦¥°¿¡^[]<>~`§μ¬\"Г")
				print(f"string lenght: {lenght}")
				print(f"output file: {output}")
				print(f"char to use: {letters}")
				generate_lenght(lenght, output, letters)
		
		elif inp_2[1] == "double_lenght":
			lenght = inp_2[2]
			if inp_2[3] == "output":
				output = inp_2[4]
				if inp_2[5] == "char":
					letters = inp_2[5]
				else:
					letters = ("qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890@*!#:;&_()-',.?+×÷=%/\$€£￦¥°¿¡^[]<>~`§μ¬\"Г")
				print(f"string lenght: {lenght}")
				print(f"output file: {output}")
				print(f"char to use: {letters}")
				double_lenght(lenght, output, letters)
					
		

main()

			
			
