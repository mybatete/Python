fg = open("Patient_info.dat","r")

while True:
    line = fg.readline()
    if line =="":
        break
    line=line.strip()
    print line, "/n"
