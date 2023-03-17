def Enqueue(QueueArray, DataToAdd):
    global tail, numOfItems
    if numOfItems >= 10:
        return False
    QueueArray[tail] = DataToAdd
    if tail >= 9:
        tail = 0
    else:
        tail = tail + 1
    numOfItems = numOfItems + 1
    return True

def Dequeue(QueueArray, numOfItems):
    global head
    if numOfItems == 0:
        return False
    else:
        ReturnVal = QueueArray[head]
        head = head + 1
        if head >= 9:
            head = 0
        numOfItems = numOfItems - 1
        return ReturnVal

QueueArray = ["" for i in range(10)]
head = 0
tail = 0
numOfItems = 0

for i in range(11):
    DataToAdd = input("Input string: ")
    result = Enqueue(QueueArray, DataToAdd)

    if result == True:
        print("Success!")
    else:
        print("Unsuccessful")


result = Dequeue(QueueArray, numOfItems)
print("{} is dequeued".format(result))
result = Dequeue(QueueArray, numOfItems)
print("{} is dequeued".format(result))