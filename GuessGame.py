
print(':Welcome to the Guess :) game:')
print('You have 10 choices left')
print('The first world is: '+'*'*10) 
num = 10

def Option1(ans):
    print('Hint is : I am a favourite food for a Lion or leopard, also I remain over the top of your letter') 
    print('Your options are: \t 1.A \t 2.B \t 3.D')
    x = input('enter ur ans: ')
    if x == 3 or x == 'D':
        print('Yipee that\'s corect')
        print('Word is : D' + '*'*9)
        return True
    else:
        print('Alas wrong answer, you are left with '+str(num-1)+' choices')
        return False
        
def Option2(ans):
    print('Hint is : Four legged animal used for Big Data management software') 
    print('Your options are: \t 1.B \t 2.Z \t 3.E')
    x = input('enter ur ans: ')
    if x == 3 or x == 'E':
        print('Yipee that\'s corect')
        print('DE' + '*'*8)
        return True
    else:
        print('Alas wrong answer, you are left with '+str(num-1)+' choices')
        Option2(x)
        return False
def Option3(ans):
    print('Hint is : King of the jungle') 
    print('Your options are: \t 1.L \t 2.M \t 3.O')
    x = input('enter ur ans: ')
    if x == 1 or x == 'L':
        print('Yipee that\'s corect')
        print('DEL' + '*'*7)
        return True
    else:
        print('Alas wrong answer, you are left with '+str(num-1)+' choices')
        return False

def Option4(ans):
    print('Hint is : zindagi me 3 chiz kabhi underestimate mat karna ___, me and myself: Bhoi :0') 
    print('Your options are: \t 1.G \t 2.I \t 3.M')
    x = input('enter ur ans: ')
    if x == 2 or x == 'I':
        print('Yipee that\'s corect')
        print('DELI' + '*'*6)
        return True
    else:
        print('Alas wrong answer, you are left with '+str(num-1)+' choices')
        return False

def Option5(ans):
    print('Hint is : Humans are saif to evolve from these guys, Mark out the panet of Apes movies ') 
    print('Your options are: \t 1.C \t 2.A \t 3.G')
    x = input('enter ur ans: ')
    if x == 3 or x == 'G':
        print('Yipee that\'s corect')
        print('DELIG' + '*'*5)
        return True
    else:
        print('Alas wrong answer, you are left with '+str(num-1)+' choices')
        return False

def Option6(ans):
    print('Hint is : Most usual starting word for a human coversation starts with this') 
    print('Your options are: \t 1.H \t 2.B \t 3.V')
    x = input('enter ur ans: ')
    if x == 1 or x == 'H':
        print('Yipee that\'s corect')
        print('DELIGH' + '*'*4)
        return True
    else:
        print('Alas wrong answer, you are left with '+str(num-1)+' choices')
        return False

def Option7(ans):
    print('Hint is : Many ships have lost their ways in this region, even today it\'s a big mystry') 
    print('Your options are: \t 1.X \t 2.T \t 3.R')
    x = input('enter ur ans: ')
    if x == 2 or x == 'T':
        print('Yipee that\'s corect')
        print('DELIGHT' + '*'*3)
        return True
    else:
        print('Alas wrong answer, you are left with '+str(num-1)+' choices')
        return False

def Option8(ans):
    print('Hint is : Mostly you have used the word- when u\'ve messed up something') 
    print('Your options are: \t 1.F \t 2.P \t 3.M')
    x = input('enter ur ans: ')
    if x == 1 or x == 'F':
        print('Yipee that\'s corect')
        print('DELIGHTF' + '*'*2)
        return True
    else:
        print('Alas wrong answer, you are left with '+str(num-1)+' choices')
        return False

def Option9(ans):
    print('Hint is : Chinese have always suppressed these muslims and world remains silent') 
    print('Your options are: \t 1.S \t 2.U \t 3.V')
    x = input('enter ur ans: ')
    if x == 2 or x == 'U':
        print('Yipee that\'s corect')
        print('DELIGHTFU' + '*'*1)
        return True
    else:
        print('Alas wrong answer, you are left with '+str(num-1)+' choices')
        return False

def Option10(ans):
    print('Hint is : It is said to be in the air when you are first time in a relationship') 
    print('Your options are: \t 1.L \t 2.Z \t 3.X')
    x = input('enter ur ans: ')
    if x == 1 or x == 'L':
        print('Yipee that\'s corect')
        print('DELIGHTFUL')
        print('YOU\'VE WON THE GAME : CONGRACTS')
        return True
    else:
        print('Alas wrong answer, you are left with '+str(num-1)+' choices')
        return False

if __name__ == '__main__':
    answer = 'Delightful'
    num = int(10)
    ch = ''
    result = True
    #for first letter of answer
    for option in range(len(answer)):
        #for options to guess the letter
        for i in range(3):
            if option == 1:
                ch = input('Hit enter').strip()
                result = Option1(ch)
            if option == 2:
                ch = input('Hit enter').strip()
                result = Option2(ch)
            if option == 3:
                ch = input('Hit enter').strip()
                result = Option3(ch)
            if option == 4:
                ch = input('Hit enter').strip()
                result = Option4(ch)
            if option == 5:
                ch = input('Hit enter').strip()
                result = Option5(ch)
            if option == 6:
                ch = input('Hit enter').strip()
                result = Option6(ch)
            if option == 7:
                ch = input('Hit enter').strip()
                result = Option7(ch)
            if option == 8:
                ch = input('Hit enter').strip()
                result = Option8(ch)
            if option == 9:
                ch = input('Hit enter').strip()
                result = Option9(ch)
            if option == 10:
                ch = input('Hit enter').strip()
                result = Option10(ch)
            if result:
                num= num-1
            else:
                break
        if num <= 0:
            print('Alas, you\'ve lost: reload last save')
            break

