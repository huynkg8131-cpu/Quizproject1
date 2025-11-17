def new_game ():
    guessed= []
    correct_guess = 0
    question_num =1 
    for key in question : 
        print("--------------")
        print (key)
        for i in option[question_num-1] : 
            print(i)
        guess = input("Enter your answer: ").upper()
     
        guessed.append(guess)
        correct_guess += check_answer(question.get(key),guess)
        question_num +=1
    
    view_score(correct_guess, guessed)
   
        
        
        
def check_answer(answer , guess):
    if answer == guess :
        print ("Correct")
        return 1
    else :
        print ("Wrong")
        return 0
    
def view_score (correct_guess, guessed):
    print ("--------")
    print ("Result")
    for i in question : 
        print (question.get(i))
    print()
    
    print ("You choosen :")
    for i in guessed :
        print (i)
    
    print ("Cac dap an dung la ")
    print (correct_guess)
        
    
def play_again():
    responde = input ("Ban co muon choi lai :").upper()
    if responde == "YES" : 
        return True
    else :
        return False

question ={
    "Ai la nguoi xinh dep nhat" : "B",
    "Ai cuoi xinh nhat trong long hien tai" : "A",
    "Mong uoc cua tui hien tai" : "C",
    "Python do ai tao ra ": "D"
}

option = [["A. Cong chua", "B.Tran ","C. Be hay cuoi","D. Layla"],
["A.Be Duy","B. Bao Boi","C.Cong chua", "D. Bboy"],
["A.Kiem that nhiu tien  ", "B. Ngu trua", "C. Thanh cong tren con duong tui da chon","D. Nothing"],
["A. Cong chua", "B.Tran ","C. Be hay cuoi","D. Guido Van Rossom"]]

new_game()
if play_again() == True :
    new_game()
else :
    print ("Game Over")