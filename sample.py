with open('data.txt',mode='w+') as f:
    f.write('hi iam siva this my project')
    f.seek(0)
    print(f.read())
