if __name__ == '__main__':
    nest=[]
    num=int(input("please give me a number "))
    scorelist=[]
    for i in range(num):
        name = input("give me a string")
        score = float(input("give me a score"))
        insider=[name,score]
        nest.append(insider)
        scorelist.append(score)
        scorelist.sort()
    scorelist2=[score for score in scorelist if score != min(scorelist)]
    result=[]
    for i in range(num):
        if nest[i][1]==min(scorelist2):
            result.append(nest[i][0])
    result.sort(reverse=False)
    for r in result:
        print(r)




