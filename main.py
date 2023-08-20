print('''
#############################################################################
#(@@@@)                    (#########)                   (@@@@@@@@(@@@@@@@@@#
#@@@@@@)___                 (####)~~~   /\                ~~(@@@@@@@(@@@@@@@#
#@@@@@@@@@@)                 ~~~~      /::~-__               ~~~(@@@@@@@@)~~#
#@@@)~~~~~~                           /::::::/\                  ~~(@@@@)   #
#~~~                              O  /::::::/::~--,                 ~~~~    #
#                                 | /:::::/::::::/{                         #
#                 |\              |/::::/::::::/:::|                        #
#                |:/~\           ||:::/:::::/::::::|                        #
#               |,/:::\          ||/'::: /::::::::::|                       #
#              |#__--~~\        |'#::,,/::::::::: __|   ,,'`,               #
#             |__# :::::\       |-#"":::::::__--~~::| ,'     ',     ,,      #
#,    ,,     |____#~~~--\,'',.  |_#____---~~:::::::::|         ',','  ',    #
# '.,'  '.,,'|::::##~~~--\    `,||#|::::::_____----~~~|         ,,,     '.''#
#____________'----###__:::\_____||#|--~~~~::::: ____--~______,,''___________#
#^^^  ^^^^^   |#######\~~~^^O, | ### __-----~~~~_____########'  ^^^^  ^^^   #
#,^^^^^','^^^^,|#########\_||\__O###~_######___###########;' ^^^^  ^^^   ^^ #
#^^/\/^^^^/\/\^^|#######################################;'/\/\/^^^/\/^^^/\/^#
#   /\/\/\/\/\  /\|####################################'      /\/\/\/\/\    #
#\/\/\     /\/\/\  /\/\/\/\    /\/\/\/\/\   /\/\/\    /\/\/\/\      /\/\/\/\#
#spb\/\/\    /\/\/\/\    /\/\/\/\    /\/\/\/\   /\/\/\/\    /\/\/\/\/\      #
#############################################################################
''')
print("Welcome to the Pirate's Hunt")
print("Your mission is to escape from the Pirate's Ship\nAll the Hunters in the ships looking for you!\nYou already escape from the Ship's cell\nBut escaping from the ship you have to find for a mini boat")
print('''Find the mini boat and escape\nGood Luck\n
       _ _      __   __       
      (_|_)    [  ) (  ]      
      (_|_)    / /   \ \      
        |      \ \___/ /      
        |       `.___,'       
   __________________________ 
  /--===---  _____ --==--   /|
 /_________________________// 
 |________________________|/  
''')
Choice = input('You\'r at the third floor of the ship, there are two doors, which door you want to go? "Red" or "Yellow"\n(REMEMBER HUNTER\'S ARE REALLY ANGRY)\n').lower()
if Choice == "red":
    Choice2=input('Mini Congrats! Now You\'r at the second floor of the ship, there are two doors, which door you want to go? "Green" or "Blue"\n(DID YOU KNOW WATER COLOR IS BLUE)\n').lower()
    if Choice2 == "green":
        Choice3=input('Congrats!! Now You\'r at the first floor, two mini boats are here, which one do you want to chose? "Pink" or "White"\n (WHITE RESMBLANCE THE SIGN OF PEACE)\n' ).lower()
        if Choice3 == "white":
         print("Congratulations! You Win, You are free now")
        else:
            print("Game Over. Ship is broken, You Died")
    else:
        print("Game Over. You fell into the middle of the sea, and DEAD")

else:
    print("Game Over. One of the Hunter kills You.")
