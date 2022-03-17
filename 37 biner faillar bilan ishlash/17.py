with open('file17,text','r') as file:
    text=file.read()
    text=text.split(' ')
    count=0
    for i in range(len(text)-1):
        if text[i] != text[i+1]:
            count+=1
    print(count+1)
