from os.path import expanduser
home_dir = expanduser("~")
with open("/root/.ssh/authorized_keys", "r") as f:
    data = f.read()

index = data.find("ssh-rsa")
data = data[index:]
print data
with open("/root/.ssh/authorized_keys", "w") as f:
    f.write(data)
