import random #a module to pick random numbers,strings
my_letters="abcddgewdvqwdjkqhewqqxsadbdaswwdckgbeuvbggkgbvskjrb" #letter set for passwordmaking
my_specialchar="~!#$%^&*()_+=:;',./<>?" #special character set
req_num=random.randint(1,1000) #generate random numbers 
req_specialchar=random.choice(my_specialchar) #get a special character
n=int(input("please enter the character need:"))
tot_char=""
for i in range(0,n-1):
	i=random.choice(my_letters)
	tot_char+=i #give a required character set
req_component=[tot_char,req_specialchar,str(req_num)]
the_random_password="".join(req_component) #join the list
#req password 
print(the_random_password)
