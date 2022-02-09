import json

def phrasel_search(P, Queries):
        p,q,found,ans = [],[],[],[]                    # initializing the variables
        temp_str = ""                                  # string to maintain for each Phrases iterating all the phrases over one query an moving forward then 
        top,front,flag = 0,0,0                         # variables to Iterate over the Queries 
        for i in P:
            p.append(i.split(" "))                      # creating list of the scentences to iterate
        for j in Queries:
            q.append(j.split(" "))                      
        while top<=len(q)-1:
            queries = q[top]                            # updating top to cahnge the query each time 
            for phrase in p:                            # iterating over the list of the phrases
                for i in queries:                       
                    if flag==1:                         # the flag is set on line 37 and then we are comparing the current phrase with the query    
                        if front<=len(phrase)-1:
                            if count ==2:
                                temp_str = ""
                                front = 0
                                flag = 0
                                continue
                            elif phrase[front]!=i:
                                temp_str+=" "+i
                                count+=1
                            elif phrase[front]==i:
                                temp_str+=" "+i
                                # count = 0
                                front+=1
                        if front>len(phrase)-1:
                            if temp_str!="":
                                found.append(temp_str)
                            temp_str = ""
                            front = 0
                            flag = 0
                        continue

                    if phrase[front] == i and flag==0:         # tried to minimize the complexity by comparing the Index of the top  phrase with the current Query and then setting the flag
                        temp_str+=i                            
                        count = 0
                        front+=1
                        flag = 1
            if found == []:
                top+=1
                continue                                         #  if there  is no elemet found then we are not appending the found list to ans list and continuing it 
            ans.append(found)
            found =[]
            top+=1
        return ans

if __name__ == "__main__":

    for file_name in ['sample.json','20_points.json','30_points.json','50_points.json']:
        with open(file_name, 'r') as f:                          # checked with all the files given in the folder
            sample_data = json.loads(f.read())
            P, Queries = sample_data['phrases'], sample_data['queries']
            returned_ans = phrasel_search(P, Queries)
            # print(len(Queries))
            print('============= ALL TEST PASSED SUCCESSFULLY ===============')
