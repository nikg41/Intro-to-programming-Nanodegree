list_level = ["easy","medium","hard"]#list of levels
ques_list = [["HTML stands for _1_.HTML is used to make web pages.to design the web pages we us CSS which stands for _2_.To know the user that we are using 5th version so, which tag we us _3_.meta tag in which tag of HTML _4_",["hyper text markup language","cascading style sheet","!DOCTYPE html","head"]],
             ["In HTML language WHich tag is used to give break _1_.How the CSS can be include in HTML Page by 3 ways what are they  _2_ .Which tag is used to do grouping of tags _3_. to give color to the background in html tag where we give it _4_.",["br","internal,external,inline","div","body"]],
            ["Which team has won 11 UEFA Champion League _1_._1_ Has won _2_ league titles from which countary they are. recently to win last UEFA Champion league which team they have Defeated _3_.Thir derby with Barcelona is known as _4_",["Real Madrid","32","Atletico Madrid","El Clasico"]]]#list of ques and answer    
que_range=range(1,5)#it is the range of no. of questions in each quiz
ques_index=0#it is the place where ques is place in ques list
que=0#place of ques in ques_index
answer_index=1#where is the answer list is there in the ques_index
'''select_level function is used to select the ques and answer list of it that person has entered whichh level.integer input as ques_index and returns the value inques in string and ans in list form'''
def select_level(ques_index):
    ques=ques_list[ques_index][que]
    ans= ques_list[ques_index][answer_index]
    return ques,ans
'''wrong function is used for wrong answer and to print try again message.it take the integer input and return integer output'''
def wrong(loop_control):
    loop_control += 1
    print "please try again."
    return loop_control         
def correct(loop_control):#if answer is correct then to print the correct
    print "correct!!"
    print "Now the paragraph look like:"
    loop_control=0
    return loop_control# it take the integer input and return integer output
'''ques_answer is used to see the answer is right or wrong in this all the main work is done of selecting a ques and ans list of program and do all the work we need'''
def ques_answer(ques_index,level):
    ques,ans=select_level(ques_index)
    for blank_control in que_range:
        print ques
        user_input = raw_input("Enter the answer in blank _" +str(blank_control)+"_ ?" + "")
        loop_control=1
        while loop_control != 0:
            if user_input == ans[blank_control-1]:
                loop_control=correct(loop_control)
                ques=ques.replace("_"+str(blank_control)+"_",user_input)
                break
            else:
                loop_control=wrong(loop_control)
                print ques
                user_input = raw_input("Enter the answer in _"+str(blank_control)+"_?" + "")
    print ques            
    print "congrats!!! you have completed "+ level + " level.if you want to play more"
'''function que_level is used to print the which level player has selected and to begin the quiz it take level as string input .ques_index is used in to call a function Quiz answer where the main work is to be done'''
def ques_level(level,ques_index):
    print "You Have choosen "+level+" Level!"
    print "Now lets Start the quiz!!"
    print "Here the paragraph for you:-"
    ques_answer(ques_index,level)
'''start function is used is to sart a quiz and is used to ask a person which level he want to play or want to quit it takes the input the person enter which level he want to play and output the level in function ques_level'''
def start():
    print "Welome! to the quiz"
    while True:
        print "Enter a level easy, medium and you want to play,else type quit to quit"
        level = raw_input("")
        if level in list_level:
            ques_index = list_level.index(level)
            ques_level(level,ques_index)   
        else:
            if level == "quit":
                break
    print "Thanks for Playing!!"
start()
    
