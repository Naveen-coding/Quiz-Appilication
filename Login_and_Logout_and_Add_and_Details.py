import json
user=[]
class Login():
	def __init__(self,name,password):
		global user
		print('\n==========LOGIN PANEL==========')
		with open('user_accounts.json', 'r',encoding="utf8") as user_accounts:
			users = json.load(user_accounts)
			if name not in users.keys():
				print("An account of that name doesn't exist.\nPlease create an account first.")
			elif name in users.keys():
				if users[name][0] != password:
					print("Your password is incorrect.\nPlease enter the correct password and try again.")
				elif users[name][0] == password:
					print("You have successfully logged in as a ",users[name][1])
					user.append(name)
					user.append(users[name][1])
class Logout():
	def __init__(self):
		global user
		if len(user) == 0:
			print("you are already logged out")
		else:
			user=[]
			print("you are successfully logged out")
class Add():
	def __init__(self):
		global user
		if len(user)==0:
			print("Login first")
		elif len(user) == 2:
			if user[1] == "ADMIN":
				print('\n==========ADD QUESTIONS==========\n')
				ques = input("Enter the question that you want to add:\n")
				opt = []
				print("Enter the 4 options with character initials (A, B, C, D)")
				for _ in range(4):
					opt.append(input())
				ans = input("Enter the answer:\n")
				str=""
				ip=True
				while ip:
					print("\n 1. G & K \n 2. Lists \n 3. Dictionaries \n 4. Tuples and Sets")
					choice=int(input(" From above topics whiich topic do u want add the question ? : "))
					if choice == 1:
						str="questions.json"
						ip=False
					elif choice == 2:
						str="lists.json"
						ip=False
					elif choice == 3:
						str="dictionaries.json"
						ip=False
					elif choice == 4:
						str="tuples&sets.json"
						ip=False
					else:
						print('WRONG INPUT GIVEN')
						ip=True
				with open(str, 'r+',encoding="utf8") as f:
					questions = json.load(f)
					dic = {"question": ques, "options": opt, "answer": ans}
					questions.append(dic)
					f.seek(0)
					json.dump(questions, f)
					f.truncate()
					print("Question successfully added.")		
			else:
				print("You don't have access to adding questions. Only admins are allowed to add questions.")
class Details():
	def __init__(self):
		global user
		if len(user)==0:
			print("Login first")
		elif len(user) == 2:
			if user[1] == "ADMIN":
				name=input("Enter user name : ")
				with open("user_accounts.json", 'r',encoding="utf8") as user_accounts:
					users = json.load(user_accounts)
					if name not in users.keys():
						print("An account of that name doesn't exist.")
					elif name in users.keys():
						print(" User Name is : {} \n User Password is : {} \n User is role is : {}".format(name,users[name][0],users[name][1]))
			else:
				print("You don't have access to see the details of users. Only admins are allowed to see the details of users.")
