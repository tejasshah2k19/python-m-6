user = {
    "name":"ram",
    "email":"ram@gmail.com",
    "password":"12345" 
}

print(len(user))
print(user["email"])
# print(user["emaiil2"])

print(user.keys())

# user.clear()


print(user.get("email"))
print(user.get("email2"))

user.update({"gender":"male"})
print(user)

user.pop("gender")
print(user)

print(user.values())
