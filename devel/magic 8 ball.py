
import random
question=input("Ask the magic 8 ball a question")



def yourAnswer(answers):

                
    if answers == 1:
        return ("It is certain")
    
    elif answers == 2:
        return ("It is decidedly so")
    
    elif answers == 3:
        return ("My sources say no")
    
    elif answers == 4:
        return ("Outlook not so good")
    
    elif answers == 5:
        return ("You may rely on it")
    
    elif answers == 6:
        return ("Ask me again later")
    
    elif answers == 7:
        return ("Concentrate and ask again")
    
    elif answers == 8:
        return ("Outlook good")

    
    
   
r= random.randint(1, 8)
result = yourAnswer(r)
print(result)
