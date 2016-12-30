with open("tf_file", "r") as f:
    data = f.read()

data = data.replace(" ", "")
data = data.replace("=", ":")
data = data.replace("[", "").replace("]\n", "")
data = data.replace(":\n", ":").replace(":", ": ")
index = data.find("ipa_master_private_dns")
domain_name = data[index+24:]
domain_name = domain_name[domain_name.find(".")+1:domain_name.find("\n")]
realm_name = domain_name.upper()


data += "\nRealmName: " + realm_name + "\nDomainName: " + domain_name
with open("./files/tf_variables", "w+") as f:
    f.write(data)
