input_str='four 52 along 96 25 gym root 15 hat 73 bank success 38 46'
alph='abcdefghijklmnopqrstuvwxyz'
counter =0
parts=input_str.split()
for i in range(len(parts)):
    simv=parts[i]
    if simv[0].isalpha()==True:
            for j in range(len(alph)):
                if simv[0]==alph[j]:
                    input_str=input_str.replace(simv,"")
                    input_str=" ".join([simv,input_str])
                    input_str = " ".join(input_str.split(" "))
    else:
        for i in range(0, len(parts) - 1):
            for j in range(len(parts) - 1):
                if (parts[j] > parts[j + 1]):
                    temp = parts[j]
                    parts[j] = parts[j + 1]
                    parts[j + 1] = temp
                    input_str = input_str.replace(parts[j + 1], "")
                    input_str = " ".join([input_str, parts[j + 1]])
                    input_str = " ".join(input_str.split(" "))
    input_str = " ".join(word for word in input_str.split())
    print(input_str)

