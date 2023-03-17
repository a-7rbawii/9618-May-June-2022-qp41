global arrayData
arrayData = [[]*2 for i in range(11)] #as STRING

def ReadHighScores():
    global arrayData
    filename = r"C:\Users\Abood\Desktop\School\Final Revision Files\Computer Science\Past paper python\P4 Papers\May June 2022 - 41\HighScore.txt"
    file = open(filename, 'r')
    for j in range(10):
        arrayData[i][0] = file.readline()[:3]
        arrayData[i][1] = file.readline()
    file.close()

def newarrange(username, score):
    global arrayData
    for i in range(10):
        if score > arrayData[i][1]:
            temp1 = arrayData[i][0]
            temp2 = arrayData[i][1]
            arrayData[i][0] = username
            arrayData[i][1] = score
            count = i + 1
            while count <10:
                newtemp1 = arrayData[count][0]
                newtemp2 = arrayData[count][1]
                arrayData[count][0] = temp1
                arrayData[count][1] = temp2

                temp1 = newtemp1
                temp2 = newtemp2
                count = count+1
                break;

def OutputHighScores():
    global arrayData
    for x in range(0, 11): 
        Output = arrayData[x][0] + " " + arrayData[x][1] 
        print(Output)

ReadHighScores() 
OutputHighScores() 
Username = input("Enter your Username") 
Score = -1 
while Score < 0 or Score > 100000: 
    Score = int(input("Enter score")) 
newarrange(Username, Score) 
OutputHighScores() 

