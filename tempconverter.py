
def tempconverter():
    print(f'{"T-C":<6}{"T-F"}')
    for i in range (101):
        tf=(9.0/5.0*(i)) + 32.0
        print()
        print(f'\n{i:<6}{round(tf,1)}')
tempconverter()

user_list=[]
user_state=True
while user_state==True:
    user_input=int(input('\nInput number:'))
    if user_input!=0:
        user_list.append(user_input)
    else:
        print(sorted(user_list))
        user_state=False
