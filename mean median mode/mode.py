from collections import Counter

def mode(x):
    a = Counter(x)
    o = {'75-85':0,'85-95':0,'95-105':0,'105-115':0,'115-125':0,'125-135':0,'135-145':0,'145-155':0,'155-165':0,'165-175':0,}
    nums = []
    for key in o:
        nums.append(list(map(lambda x:float(x),key.split('-'))))
    #print(nums)
    for b in a.items():
        for r in nums:
            #print(b)
            if b[0] > r[0] and b[0] < r[1]:
                o['{0}-{1}'.format(int(r[0]),int(r[1]))]+=1

    most_occured = max(zip(o.values(),o.keys()))[1]
    avg = (int(most_occured.split('-')[0])+int(most_occured.split('-')[1]))/2
    return avg




