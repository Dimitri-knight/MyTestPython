#my second test thing from Atom

import json, random

filename='users.json'
try:
    jsonfile = json.load(open(filename))
except:
    jsonfile = [{"login": "admin", "password": "32145", "premission": 2}]
    with open(filename, 'w') as file:
        json.dump(jsonfile, file, indent=2, ensure_ascii=0)

print(jsonfile)

def write_json():
    tmp=0
    while tmp!=1:
        tmplog=input("Enter login to add:")
        for i in range(0, len(jsonfile)):
            if tmplog in jsonfile[i].values():
                print("Login is taken")
                tmp=1
                break
        if tmp==1: break
        tmppas=input("Enter password to add:")
        tmpprem=int(input("Enter premission 1-2 to add:"))
        tmp=1
    try:
        tmpuser={"login":tmplog, "password":tmppas, "premission":tmpprem}
    except:
        return

    try:
        data = json.load(open(filename))
    except:
        data=[]
    data.append(tmpuser)

    with open(filename, 'w') as file:
        json.dump(data, file, indent=2, ensure_ascii=0)

def delete_json():
    print(jsonfile)
    tmp=input("Select user login to delete: ")
    try:
        for i in range(len(jsonfile)):
            if jsonfile[i]["login"] == tmp:
                del jsonfile[i]
                break
        with open(filename, 'w') as file:
            json.dump(jsonfile, file, indent=2, ensure_ascii=0)
        print("User deleted successfully")
    except:
        print("Unexpected error")

tmp=1
while tmp!=0:
    login=input("Enter login:")
    for i in range(0, len(jsonfile)):
        accn=i
        if login in jsonfile[i].values():
            password = input("Enter password:")
            if jsonfile[i]['password'] == password:
                print("You joind server")
                tmp=0
                break
    if tmp!=0: print("Login or password is incorrect")

tmp=1

while tmp!=0:
    try:
        jsonfile = json.load(open(filename))
    except:
        jsonfile = []
    if jsonfile[accn]['premission']==2:
        tmp=int(input("1 - Read users\n2 - Add user\n3 - Delete user\n0 - Exit\n"))
        if tmp==1: print(jsonfile)
        elif tmp==2: write_json()
        elif tmp==3: delete_json()
    elif jsonfile[accn]['premission']==1:
        print("You are a regular user")
        tmp=0
    else:
        print("You are unspecialized user, your premission status is "+str(jsonfile[accn]['premission']))
        tmp=0
