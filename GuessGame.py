print(':Welcome to the Guess :) game:')
print('You have 10 choices left')
print('The first world is: ' + '*' * 10)


def option1():
    print('Hint is : I am a favourite food for a Lion or leopard, also I remain over the top of your letter')
    print('Your options are: \t 1.A \t 2.B \t 3.D')
    x = input('enter ur ans: ')
    if x == 3 or x == 'D':
        print('Yippee that\'s correct')
        print('Word is : D' + '*' * 9)
        return 1
    else:
        print('Alas wrong answer, you are left with ' + str(num - 1) + ' choices')
        return 0


def option2():
    print('Hint is : Four legged animal used for Big Data management software')
    print('Your options are: \t 1.B \t 2.Z \t 3.E')
    x = input('enter ur ans: ')
    if x == 3 or x == 'E':
        print('Yippee that\'s correct')
        print('DE' + '*' * 8)
        return 1
    else:
        print('Alas wrong answer, you are left with ' + str(num - 1) + ' choices')
        return 0


def option3():
    print('Hint is : King of the jungle')
    print('Your options are: \t 1.L \t 2.M \t 3.O')
    x = input('enter ur ans: ')
    if x == 1 or x == 'L':
        print('Yippee that\'s correct')
        print('DEL' + '*' * 7)
        return 1
    else:
        print('Alas wrong answer, you are left with ' + str(num - 1) + ' choices')
        return 0


def option4():
    print('Hint is : ZINDAGI me 3 chiz kabhi underestimate mat karna ___, me and myself: Bhoi :0')
    print('Your options are: \t 1.G \t 2.I \t 3.M')
    x = input('enter ur ans: ')
    if x == 2 or x == 'I':
        print('Yippee that\'s correct')
        print('DELI' + '*' * 6)
        return 1
    else:
        print('Alas wrong answer, you are left with ' + str(num - 1) + ' choices')
        return 0


def option5():
    print('Hint is : Humans are said to evolve from these guys, Mark out the planet of Apes movies ')
    print('Your options are: \t 1.C \t 2.A \t 3.G')
    x = input('enter ur ans: ')
    if x == 3 or x == 'G':
        print('Yipee that\'s correct')
        print('DELIG' + '*' * 5)
        return 1
    else:
        print('Alas wrong answer, you are left with ' + str(num - 1) + ' choices')
        return 0


def option6():
    print('Hint is : Most usual starting word for a human conversation starts with this')
    print('Your options are: \t 1.H \t 2.B \t 3.V')
    x = input('enter ur ans: ')
    if x == 1 or x == 'H':
        print('Yippee that\'s correct')
        print('DELIGH' + '*' * 4)
        return 1
    else:
        print('Alas wrong answer, you are left with ' + str(num - 1) + ' choices')
        return 0


def option7():
    print('Hint is : Many ships have lost their ways in this region, even today it\'s a big mystery')
    print('Your options are: \t 1.X \t 2.T \t 3.R')
    x = input('enter ur ans: ')
    if x == 2 or x == 'T':
        print('Yippee that\'s correct')
        print('DELIGHT' + '*' * 3)
        return 1
    else:
        print('Alas wrong answer, you are left with ' + str(num - 1) + ' choices')
        return 0


def option8():
    print('Hint is : Mostly you have used the word- when u\'ve messed up something')
    print('Your options are: \t 1.F \t 2.P \t 3.M')
    x = input('enter ur ans: ')
    if x == 1 or x == 'F':
        print('Yippee that\'s correct')
        print('DELIGHTF' + '*' * 2)
        return 1
    else:
        print('Alas wrong answer, you are left with ' + str(num - 1) + ' choices')
        return 0


def option9():
    print('Hint is : You can\'t enjoy the rain without these')
    print('Your options are: \t 1.S \t 2.U \t 3.V')
    x = input('enter ur ans: ')
    if x == 2 or x == 'U':
        print('Yippee that\'s correct')
        print('DELIGHTFUL' + '*' * 1)
        return 1
    else:
        print('Alas wrong answer, you are left with ' + str(num - 1) + ' choices')
        return 0


def option10():
    print('Hint is : It is said to be in the air when you are first time in a relationship')
    print('Your options are: \t 1.L \t 2.Z \t 3.X')
    x = input('enter ur ans: ')
    if x == 1 or x == 'L':
        print('Yippee that\'s correct')
        print('DELIGHTFUL')
        print('YOU\'VE WON THE GAME : CONTRACTS')
        return 1
    else:
        print('Alas wrong answer, you are left with ' + str(num - 1) + ' choices')
        return 0


if __name__ == '__main__':
    answer = 'Delightful'
    num = int(10)
    ch = ''
    result = int(1)
    # for first letter of answer
    for option in range(len(answer)):
        if num <= 0:
            print('Alas, you\'ve lost: reload last save')
            break
        if option == 0:
            ch = input('Hit enter').strip()
            result = option1()
            if result == 1:
                continue
            elif result == 0:
                num = num - 1
                option1()
        elif option == 1:
            ch = input('Hit enter').strip()
            result = option2()
            if result == 1:
                continue
            elif result == 0:
                num = num - 1
                option2()
        elif option == 2:
            ch = input('Hit enter').strip()
            result = option3()
            if result == 1:
                continue
            elif result == 0:
                num = num - 1
                option3()
            result = option3()
        elif option == 3:
            ch = input('Hit enter').strip()
            result = option4()
            if result == 1:
                continue
            elif result == 0:
                num = num - 1
                option4()
        elif option == 4:
            ch = input('Hit enter').strip()
            result = option5()
            if result == 1:
                continue
            elif result == 0:
                num = num - 1
                option5()
        elif option == 5:
            ch = input('Hit enter').strip()
            result = option6()
            if result == 1:
                continue
            elif result == 0:
                num = num - 1
                option6()
        elif option == 6:
            ch = input('Hit enter').strip()
            result = option7()
            if result == 1:
                continue
            elif result == 0:
                num = num - 1
                option7()
        elif option == 7:
            ch = input('Hit enter').strip()
            result = option8()
            if result == 1:
                continue
            elif result == 0:
                num = num - 1
                option8()
        elif option == 8:
            ch = input('Hit enter').strip()
            result = option9()
            if result == 1:
                continue
            elif result == 0:
                num = num - 1
                option9()
        elif option == 9:
            ch = input('Hit enter').strip()
            result = option10()
            if result == 1:
                continue
            elif result == 0:
                num = num - 1
                option10()


