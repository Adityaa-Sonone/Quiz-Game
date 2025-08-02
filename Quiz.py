head = " Welcome to Quiz Game "
x = head.center(40, "-")
print("\n", x)
print("\n Please click 'Enter' to start the Game \n")

Questions = [
    ["1. What is the capital of India ?", "Mumbai", "Kolkata", "Nagpur", "Delhi", 4],
    ["2. How many state are there in India ?", "28", "29", "30", "31", 2],
    ["3. Who is the 1st President of India ?", "Dr Rajendra Prasad", "Jawaharlal Nehru", "Dr B. R. Ambedkar", "Sardar Vallabhbhai Patel", 1],
    ["4. Facebook is developed using ?", "PHP", "Java", "C++", "Python", 1],
    ["5. How many countries are there in the world ?", "194", "195", "196", "199", 2],
    ["6. What is capital of Japan ?", "Osaka", "Burlin", "Tokyo", "Kyoto", 3],
    ["7. Which year did the world war 2 end ?", "1930", "1935", "1940", "1945", 4],
    ["8. Which is Biggest continent in the world ?", "Africa", "Asia", "Europe", "Antartica", 2],
    ["9. What is the Name of India's 1st satellite ?", "Chandrayan", "Aryabhata", "Mangalyaan", "Aditya L1", 2],
    ["10. Python Language was developed by ?", "Guido Van Rossum", "James Gosling", "Bjarne Stroustrup", "Dennis Ritchie", 1]]

score = 0
add = input("")

if add == "":
    for i in range(0, len(Questions)):
        Question = Questions[i]
        print(f"\n{Question[0]}")
        print(f"\n 1. {Question[1]}        2. {Question[2]} \n 3. {Question[3]}        4. {Question[4]}")
        reply = int(input("\nPlease Enter your Answer : "))
        if reply == Question[5]:
            print(("\nCorrect Answer \n-----------------------------------"))
            level += 10
        else:
            print(f"Wrong Answer,   Correct Answer is {Question[5]} \n-----------------------------------")
    
    print("\nYour Final Score is ", score, "/ 100 \n")

else: 
    print("\n       Your Enter Wrong Key")
    print("\n         Restart The Game")