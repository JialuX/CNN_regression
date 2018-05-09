import os
import json



#path_t = r"/Users/xujialu/Desktop/Term1/Data Ming/dataset/lamem/test" #path of dataset of pics
path_t = r"/Users/xujialu/Desktop/Term1/Data Ming/dataset/lamem/splits"

# store the sum of image scores
sum_score = {}
#store the count of every image memorability trial
count = {}
i = 0
for dirs in os.listdir(path_t):
    scorepath = os.path.join(os.path.join(path_t, dirs))
    print(scorepath)

    file_object = open(scorepath, 'rb')

    for line in file_object:
        a= bytes.decode(line)
        a = a.split(' ')
       # print(a)
        if len(a)==2:
            if sum_score. __contains__(a[0]) is False:
                sum_score[a[0]] = float(a[1][:8])
                count[a[0]]=1
            else:
                sum_score[a[0]] += float(a[1][:8])
                count[a[0]]+=1

#print(dict)
#print(count)
ave_score={}   #get the average of the memorability score of every image
'''
for item in sum_score:
    ave_score[item]=int(sum_score.get(item)/count.get(item)*100)
#print(ave_score)
'''
for item in sum_score:
    ave_score[item]=sum_score.get(item)/count.get(item)


#save to file
mydatafile="/Users/xujialu/Desktop/Term1/Data Ming/dataset/tt.txt"
with open(mydatafile, 'w') as f:
    json.dump(ave_score, f)
    #print("er")
f.close()

# show the distribution of the scores, imbalance
#count_0=0
#count_1=0
#count_2=0
#count_3=0
#for item in ave_score:
 #   if ave_score[item]>0.75:
  #      count_3+=1
   # elif ave_score[item]>0.5:
    #    count_2 += 1
    #elif ave_score[item] > 0.25:
     #   count_1 += 1
    #else:
     #   count_0 +=1

#print(count_3)
#print(count_2)
#print(count_1)
#print(count_0)