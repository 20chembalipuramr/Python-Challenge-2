from random import randint
from time import sleep
import os
curRes=""
spinRes=[]
money = 100
fruits=["🍒","🔔","🍋","🍊","⭐","💀"]

def newUser():
	os.system('clear')
	newsername = input("What would you like your Username to be?\n")
	newspasword = input("What would you like your password to be?\n")
	confNewspasword = input("Please confirm your password\n")
	if newspassword != confNewspasword:
		print("Your passwords did not match, try again")
		newUser()
	else:
		f1 = open("information", "r")
		numUsers=f1.read()
		f1.close()
		f2 = open("information", "w")
		numUsers+=1
		f2.write(numUsers)
		f3.close()
		f4 = open("usernames", "a")
		f4.append("\n")
		f4.append(newsername)
		f4.close()
		f5 = open("passwords", "a")
		f5.append("\n")
		f5.append(newspasword)
		f5.close()
		f6 = open("money", "a")
		f6.append("\n")
		f6.append(100)
		f6.close()

def preLogin():
	logOrSig = input ("Would you like to login or create an account?\n(LOGIN/CREATE)\n")
	if logOrSig == 'LOGIN':
		login()
	elif logOrSig == 'CREATE':
		newUser()

def login():
  intusername = open("usernames.txt", "t")
  usernames =  (username.read())# i have no idea how this works

  intpassword = open("passwords.txt", "t")
  
	username = input("Please enter your username!\n")
  password = input("Please enter your password\n")
  if username = #hopen the                   

def choice():
	start = input("Do you want to play the fruit machine? (YES/NO)\n")
	os.system('clear')
	if start == "YES":
		run1()
	elif start == "NO":
			print ("💀")
	else:
		print ("Your input was invalid, sending you back to the start!")
		sleep(1)
		os.system('clear')
		choice()

def spinSpinner():
	global money
	spinRes=[]
	curRand=randint(0,5)
	curRes1=fruits[curRand]
	spinRes.append(curRes1)
	curRand=randint(0,5)
	curRes2=fruits[curRand]
	spinRes.append(curRes2)
	curRand=randint(0,5)
	curRes3=fruits[curRand]
	spinRes.append(curRes3)
	print(spinRes)
	if curRes1 == "🔔" and curRes2 == "🔔" and curRes3 == "🔔":
		money += 500
		print("You have won 500p for having three bells!")
		sleep(2)
		os.system('clear')
		run1()
	elif curRes1 == "💀" and curRes2 == "💀" and curRes3 == "💀":
		money = 0
		print("You lost all of your money from getting 3 skulls :skull:")
		L()
	elif curRes1 == "💀" and curRes2 == "💀" or curRes1 == "💀" and curRes3 == "💀" or curRes2 == "💀" and curRes3 == "💀":
		money -= 100
		print("You have lost 100p for having two skulls!")
		sleep(2)
		os.system('clear')
		run1()
	elif curRes1 == curRes2 and curRes1 == curRes3:
		money += 100
		print("You have won 100p for having three of the same thing")
		sleep(2)
		os.system('clear')
		run1()
	elif curRes1 == curRes2 or curRes2 == curRes3 or curRes3 == curRes1:
		money += 50
		print("You have won 50p for having a duplicate in your spin!")
		sleep(2)
		os.system('clear')
		run1()
	else:
		print("You did not win anything this time")
		sleep(2)
		os.system('clear')
		run1()

def L():
	print("You do not have enough money to play again\nPlease share with your friends: https://replit.com/@RohanCHEMBALIPU/Python-Challenge-2")

def run1():
	global money
	print("You have "+str(money)+"p left")
	spin = input("Do you want to spin again? (YES/NO)\n")
	if spin == "YES" and money>20:
		money -=20
		spinSpinner()
	elif spin == "NO":
		print ("💀")
	else:
		os.system('clear')
		print ("Your input was invalid, sending you back!")
		sleep(1)
		os.system('clear')
		run1()

login()