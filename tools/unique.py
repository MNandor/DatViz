#removes duplicate stations
ifs = open("result.txt", "rt")
lines = ifs.readlines()
ifs.close()

unique = list(dict.fromkeys(lines))
ofs = open("unique.txt", "wt")
ofs.writelines(unique)
ofs.close()

print(len(unique))

check = list(dict.fromkeys([x.split()[0] for x in lines]))
print(len(check))
