with open('file16,text','r') as file:
    text=file.read()
    text=text.split()
    print(text)
    count=0
    for i in range(len(text)-1):
        if text[i]!=text[i+1]:
            count+=1
    print(count+1)

