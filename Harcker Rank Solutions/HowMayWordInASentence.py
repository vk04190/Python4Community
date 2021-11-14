
def howMany(sentence):
    # Write your code here
    word_list=sentence.replace("."," ").replace(","," ").replace("?"," ").replace("!"," ").replace("  "," ").strip().split(" ")
    total_world=0
    for i in word_list:
        if i.isnumeric():
            pass
        else:
            flag=True
            for a in i:
                print(i,a,flag)
                a="fff"
                if a.i:
                    
                    flag=False
                    break
                else:
                    flag=True
            if flag:
                    total_world+=1

            
            
    # new_sentence=
    return(total_world)

    

if __name__ == '__main__':
    pass

sentence="bf[l. dj."
print(howMany(sentence))