def typing_speed_test():
    #TYPING SPEED TEST:
    import random
    import time
    word_random=['is','are','apple','book','practical','car','girl','water','down','through','keyboard','self','application','form','speaker','grass','cat','dog','me','you','file','get','head','now','read','write','yours','mind','future','sentence','alphabet','river','mountain','house','play','game','kite','hello','bye','pendrive','monitor','cherry','banana','grape','objector','member','february','antiquary','march','may','spring','food','vegetable','boy','page','chemistry','folder','their','why','done','eyes','nose','ears','beautiful','time','day','year','hundred','heart','mouse','road','cloud','friends','drop','window','bottle','mutual','today','rabbit','listen','song','work','eat','ate','sleep','short','life','being','human','limit','maths','clothes','bike','car','scooter','motor','boat','claim','chair','carrot','handle','peace','positive','reflect','walk','calendar','goods','notes','crossing','unique','appreciable','memories','competition','crossword','definition','lotion','optical','elements','unicorn','popcorn','capsicum','integration','difference','unstoppable','India','summer','world','supplementary','development','committee','acknowledgment','fundamental','morning','nightmare','camera','impatient','attention','anybody','California','still','amazing','amazon','consequently','seemed','stolen','family','stricken']
    wrong_word=0
    correct_word=0
    keystrokes=0

    print("You have 20 sec to read the rule")
    print("="*32)
    rules="This games is to test and improve your typing speed.Some rules below:\n1.Focus on accuracy\n2.Sit staight\n3.Be patient\n4.Know your finger position"
    print(rules)
    print("If you have read the rules kindly wait and be prepared")
    time.sleep(20)
    print("Your typing starts now:")
    print("="*23)


    for i in range (25):#printing of words
        selected=(random.choice(word_random))
        print(selected)
        entered=input()
        keystrokes+=len(entered)#keystrokes
        if entered!=selected:
            wrong_word+=1#wrong word
        elif entered==selected:
            correct_word+=1#correct word

            
    print("Accuracy Rate:",correct_word*100/25,"%")#accuracy rate
    print("Keystrokes:",keystrokes)
    print("Wrong word:",wrong_word)
    print("Correct word:",correct_word)
    print("Speed:",(correct_word)*100%(keystrokes),"WPM(words per minute)")
typing_speed_test()

#change3
