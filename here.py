from Stack import Stack
fg = open("extract_seqs4_sbv2.1_all.c", "r")
s = stack()
f = stack()

while True:
    line = fg.readline()
    if line == "":
        break
    for i in xrange(0, len(line)):
        if line[i] == "{":
            if s.isEmpty == True
            s.push (line[i])
        elif line[i] ==
        else:
            
            print "there is an error"

        if line[i] == "(":
            if f.isEmpty == True
            print "missing parenthesis"
        else:
            f.push(line[i])
if s.isEmpty == True:
    print mistake
    
