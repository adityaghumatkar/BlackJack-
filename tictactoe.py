

l=[' ']*9

from IPython.display import clear_output
def board():
    clear_output()
    print(""+l[6]+"   | "+l[7]+"    |"+l[8]+"     ")
    print("----|------|-----")
    print(""+l[3]+"   | "+l[4]+"    |"+l[5]+"     ")
    print("----|------|-----")
    print(""+l[0]+"   | "+l[1]+"    |"+l[2]+"     ")


def marker_position(str):
    marker=input(str+' enter the location')
    return int(marker)

def check_space(l,m):
    if l[m]=='X' or l[m]=='O':
        return 0
    else:
        return 1

def win(l,p):
    if ((l[0]==p and l[1]==p and l[2]==p) or (l[3]==p and l[4]==p and l[5]==p) or (l[6]==p and l[7]==p and l[8]==p) or (l[0]==p and l[3]==p and l[6]==p) or 
    (l[1]==p and l[4]==p and l[7]==p) or (l[2]==p and l[5]==p and l[8]==p) or (l[0]==p and l[4]==p and l[8]==p) or (l[2]==p and l[4]==p and l[6]==p)) :
        return 1
    else :
        return 0

v1='X'
v2='O' 
flag = 0
board()
for i in range(9):
    if flag == 0 :
        str1 = 'PLAYER 1'
        m2=marker_position(str1)
        k=check_space(l,m2)
        while k==0 :
            print('use another location')
            m2=marker_position(str1)
            k=check_space(l,m2)
        l[m2]=v1
        board()
        e1=win(l,v1)
        if e1==1:
            print('player 1 won the game')
            break
        flag =1
        i=i+1
    else :
        str2 = 'PLAYER 2'
        m1=marker_position(str2)
        k=check_space(l,m1)
        while k==0 :
            print('use another location')
            m1=marker_position(str2)
            k=check_space(l,m1)
        l[m1]=v2
        board()
        e2=win(l,v2)
        if e2==1:
            print('player 2 won the game')
            break
        flag =0
        i=i+1

if i > 8 :
    print('match draw')
    

