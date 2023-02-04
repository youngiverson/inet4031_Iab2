with open("file.txt", "r") as file:
        lines = file.readlines()
lines_split = [line.strip().split(":") for line in lines]
lines_filtered = [line for line in lines_split if not line[0].startswith("#")]
print("Printing out User Data:")
for line in lines_filtered:
    user, password, userid, groupid = line
    print(f"The user {user} has a password of {password} and has userid {userid} and groupid {groupid}")
print("End of User Data")
