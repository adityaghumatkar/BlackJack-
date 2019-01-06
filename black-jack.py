import random
from IPython.display import clear_output
cards=('Heart','Diamond','Spade','Club')
ranks=('Ace','2','3','4','5','6','7','8','9','10','Joker','Queen','King')
cards_val={'Ace':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'Joker':10,'Queen':10,'King':10}
player1=[]
dealer=[]
deck=[]

global b1

def form_deck():
    for card in cards:
        for rank in ranks:
            deck.append((card , rank))

def shuffle():
    random.shuffle(deck)


def player():
    name=input('enter name ')
    bet=input('enter bet amount ')
    bet=int(bet)
    #print('Dealer bets with Rs',bet)
    return (name , bet )
    
def distribute_cards():
    print('Distributing Cards...')
    for i in range(2):
        player1.append(deck.pop(0))
        dealer.append(deck.pop(0))
    


def play(name,bet):
    b1=1
    if b1 == 1 :
        psum = calculate_value(player1)
        dsum = calculate_value(dealer)
        if psum == 21 and psum >dsum :
            print(name +' it is a perfect black-jack(21)')
            print('you won!!!')
        else :
            while True :
                #x=display(psum,dsum,b1)
                (psum,x1)=actions(name , player1,b1,psum,dsum)
                #print('card total dealer',dsum)
                #print('card total player',psum)
                x1=int(x1)
                if x1 == 1:
                    if psum < 22 :
                        continue
                    else :
                        b1=2
                        x=display(psum,dsum,b1)
                        #print('                                                  | money Won :',bet)
                        #print('                                                  | '+name +' BUSTED!!!Better luck next time.')
                        #print('                                                  | Dealer Won!!')
                        break
                else :
                    b1=0
                    #print('stay completes')
                    break
        
    if b1==0:
        #print("It's Dealers turn now")
        #print('Dealers cards:')
        #print(dealer)
        #print('Dealers card total is ',dsum)
                
        if dsum < 17 :
            if psum < dsum:
                #print('inside dsum 17/psum<dsum')
                b1=2
                x=display(psum,dsum,b1)
                b1=0
            else :
                while True :
                    #display(psum,dsum,b1)
                    (dsum,x1)=actions('dealer',dealer,b1,psum,dsum)
                    #print('card total dealer',dsum)
                    #print('card total player',psum)
                    x1=int(x1)
                    if x1 == 1 :
                        if dsum < 22:
                            if dsum < psum or dsum == psum :
                                continue
                            else :
                                #print('                                                  | Dealer has Won the Game')
                                #print('                                                  | Winning amount : Rs',(bet*2))
                                break
                        else :
                            break
                    else :
                        break
                            
                if dsum > 21 :
                    b1=3
                    x=display(psum,dsum,b1)
                    b1=0
                elif psum == 21 :
                    b1=3
                    if psum > dsum :
                        x=display(psum,dsum,b1)
                        
                    else:
                        b1=4
                        x=display(psum,dsum,b1)
                        
                                    
                elif psum < dsum :
                    b1=2
                    x=display(psum,dsum,b1)
                    #print('                                                  | dealer has won the game')
                    #print('                                                  | prize won :',bet *2)
                    #print('                                                  | dealers card total : ',dsum)
                    #print('                                                  | '+name + ' card total :',psum)
                    
                elif psum == dsum :
                    b1 = 4
                    x=display(psum,dsum,b1)
                    #print('                 Match draw.')
                    
                else :
                    b1=3
                    x=display(psum,dsum,b1)
                    #print(name +' has won the game')
                    #print('prize won :',(bet *2))
                    #print('dealers card total : ',dsum)
                    #print(name + ' card total :',psum)
        else :
            if dsum > psum :
                b1=2
                x=display(psum,dsum,b1)
                #print('                                                  | dealer won !!')
                #print('                                                  | card total dealer : ',dsum)
            elif dsum == psum :
                b1=4
                x=display(psum,dsum,b1)
                #print('                 Match draw.')
                
            else :
                b1=3
                x=display(psum,dsum,b1)
                #print(name +' won!!')
                #print('card total player : ',psum)            
            
                                                
def actions(name,d,b2,psum,dsum):
    
    x=display(psum,dsum,b2)
    #x=input(name + ' do you want to :\n1.HIT\n2.STAY\n')
    x=int(x)
    if x == 1 :
        add_card(b2)
        xsum = calculate_value(d)
        return (xsum,x)
        
    else :
        xsum=calculate_value(d)
        #print('Lets check what dealer has got.')
        return (xsum,x)
        
        
    
        
def add_card(v):
   # print('inside add card')
    if v == 1:
        player1.append(deck.pop(0))
        print('card added to player')
        #print(player1)
    else :
        dealer.append(deck.pop(0))
        print('                                                  | card added to dealer')
        #print(dealer)

def calculate_value(d):
    #print(type(d))
    sum = 0
    for i in range(len(d)):
        sum = sum + cards_val[d[i][1]]
    if check_ace(d):
        if sum <12 :
            return(sum+10)
        else :
            return(sum)
    else :
        return(sum)


def check_ace(d):
    for i in range(len(d)):
        if d[i][1] == 'Ace':
            return True
    return False

def display(psum,dsum,b3):
    clear_output()
    print('Cards Distributed..')
    print('player : '+name+'                                   |  dealer : Dealer')
    print('--------------------------------------------------|----------------------------------------')
    if b3 == 1 :
        print('Card Total : ',psum,'                                 |  Card Total : [X]')
        print('Cards :                                           |  Cards :')
        print(player1,'| ',dealer[0],'[hidden]')
    else :
        print('Card Total : ',psum,'                                 |  Card Total : ',dsum)
        print('Cards :                                           |  Cards :')
        print(player1,'| ',dealer)
        
    
    if b3 == 1:
        print('players turn                                      |')     
        x=input(name + ' do you want to :                           |\n1.HIT\n2.STAY\n')
        x=int(x)
        return x
    elif b3 == 0 :
        print('                                                  | Dealers turn')
        x=input('                                                  | Dealer do you want to :\n                                                  | 1.HIT                                                 \n                                                  | 2.STAY\n                                                  |')
        x=int(x)
        return(x)
    elif b3 == 2 :
        if dsum > psum:
            print('\n')
            print('\n')
            print('                                                  | Dealer has Won the Game')
            print('                                                  | Winning amount : Rs',(bet*2))
        else :
            print('\n')
            print('\n')
            print('                                                  | money Won :',bet)
            print('                                                  | '+name +' BUSTED!!!Better luck next time.')
            print('                                                  | Dealer Won!!')
   
    elif b3 == 3 :
        if dsum > 21 :
            print('\n')
            print('\n')
            print('Dealer BUSTED!!!. ' + name +' has won the game         |')
            #print('card total dealer',dsum,'       |')
            print('prize money won by :' + name,bet*2,'                   |')
        else :
            print('\n')
            print('\n')
            print(name + ' has won the game!!                             |')
            #print(name + ' cards total : ',psum,'| dealers cards total : ',dsum)
            print('prize money won by :' + name,bet *2,'                  |')
    else :
        print('\n')
        print('\n')
        print('                 Match draw.')
    

if __name__ == '__main__':
    print('*-*-*-*-*-*-lets play black-jack!!!!*-*-*-*-*-*-*')
    (name ,bet )=player()
    form_deck()
    shuffle()
    distribute_cards()
    #display_cards(name)
    play(name , bet)
    #print(deck)
    
