logpas = dict([('murblen','32145'),('senti','15234')])
print(logpas)
login=input("Enter login:")
if login in logpas:
    password=input("Enter password:")
    if logpas[login]==password:
        print("You joind server")
    else: print("Password incorrect")
else: print("Login not found")