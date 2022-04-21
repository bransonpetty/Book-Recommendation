import operator

topFriends = {}


def friends(userInput):
    people = []
    rating = []
    peopleDict = {}
    with open("ratings.txt", "r") as friends:
        ratingSort = friends.readlines()
        for i in range(len(ratingSort)):
            if i % 2 == 0:
                people.append(ratingSort[i].strip("\n"))
            else:
                rating.append(ratingSort[i].split())

    friends.close()

    for j in range(len(people)):
        peopleDict.setdefault(people[j], rating[j])

    resultsDict = {}

    for trial in range(len(people)):
        mainSubject = people[trial]
        tempList = []

        for subTrial in range(len(people)):
            total = 0
            if trial == subTrial:
                tempList.append(-5)
            else:
                for compare in range(55):
                    one = int(peopleDict[people[trial]][compare])
                    two = int(peopleDict[people[subTrial]][compare])
                    total += one * two
                total = total / 55
                tempList.append(total)

        resultsDict.setdefault(mainSubject, tempList)

    pos1 = 0
    pos2 = 0
    topFriends = {}
    for q in range(len(people)):
        friendOne = -9
        friendTwo = -10
        for w in range(len(people)):
            if resultsDict[people[q]][w] > friendOne:
                friendTwo = friendOne
                friendOne = resultsDict[people[q]][w]
            elif resultsDict[people[q]][w] > friendTwo:
                friendTwo = resultsDict[people[q]][w]
            else:
                continue

        for e in range(len(people)):
            if resultsDict[people[q]][e] == friendOne:
                pos1 = e
            elif resultsDict[people[q]][e] == friendTwo:
                pos2 = e
        amigos = [people[pos1], people[pos2]]
        topFriends.setdefault(people[q], amigos)

    for check in range(len(people)):
        if userInput == people[check]:
            break
        else:
            userInput = userInput.title()
            if userInput == people[check]:
                break
            else:
                userInput = userInput.lower()
                if userInput == people[check]:
                    break
                else:
                    if check == len(people) - 1:
                        print("Reader not found.")
                        quit()
                    else:
                        continue

    thing1 = topFriends.get(userInput)[0]
    thing2 = topFriends.get(userInput)[1]

    with open("booklist.txt", "r") as books:
        bookList = books.readlines()
        library = []
        for test in range(55):
            rate = int(peopleDict.get(userInput)[test])
            rate1 = int(peopleDict.get(thing1)[test])
            rate2 = int(peopleDict.get(thing2)[test])
            if rate == 0:
                if rate1 == 3:
                    library.append(bookList[test])
                elif rate1 == 5:
                    library.append(bookList[test])
                elif rate2 == 3:
                    library.append(bookList[test])
                elif rate2 == 5:
                    library.append(bookList[test])
                else:
                    continue
            else:
                continue

    thing1 = topFriends.get(userInput)[0].title()
    thing2 = topFriends.get(userInput)[1].title()
    alphaFriends = [thing1, thing2]
    alphaFriends.sort()
    library.sort()
    line = []
    patchedLibrary = []
    # patchedBook = []

    print("Recommendations for", userInput.title(), "from", thing1, "and", thing2)
    for b in range(len(library)):
        patchedBook = []
        library[b] = library[b].strip("\n")
        library[b] = library[b].split(",")
        title = library[b][1]
        element = 0
        library[b][0] = library[b][0].split()

        authorFirst = library[b][:-1]
        authorSecond = library[b][-2]
        patchedBook.append(authorFirst)
        patchedBook.append(authorSecond)
        patchedBook.append(title)
        patchedLibrary.append(patchedBook)
        # patchedBook.clear()
    patchedLibrary.sort(key = operator.itemgetter(-1))
    print(patchedLibrary)
    # print(patchedLibrary)
    for b in range(len(library)):
        # print(patchedLibrary)
        print(patchedLibrary[b][0], patchedLibrary[b][1] + ",", "\t", patchedLibrary[b][1])


def recommend():
    while True:
        userInput = input("Enter a reader's name: ")
        if userInput == "":
            quit()
        else:
            friends(userInput)
            recommend()


recommend()
