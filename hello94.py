import sys
f=open("param2.txt","r")
line1=f.readline()
line2=f.readline()
sys.stdout.write(line1)
sys.stdout.write(line2)
sys.stderr.write("No Error occured \n")
