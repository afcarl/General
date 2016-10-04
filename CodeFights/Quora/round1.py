def mostViewedWriters(topicIds, answerIds, views):
    from operator import itemgetter
    from itertools import groupby
    
    flat_topicIds = [item for sublist in topicIds for item in sublist]
    flat_topicIds = sorted(set(flat_topicIds))
    results = []
    
    for ti in flat_topicIds:
        per_t = []
        mapping = map(lambda x:1 if (ti in x) else 0, topicIds)
        map_index = map(lambda x: x[0] if (x[1]==1) else None,enumerate(mapping))
        map_index = filter(lambda x: x!=None,map_index)
        answerIds_topic = [answerIds[i] for i in map_index]
        answerIds_topic = [item for sublist in answerIds_topic for item in sublist]
        #print answerIds_topic
        for i in answerIds_topic:
            views_perTopic = filter(lambda x: i == x[0], views)
            users_topic = map(lambda x: x[1:],views_perTopic)
            per_t.append(users_topic[0])
        
        #print per_t,'no sort, no group'
        new_pert = []
        per_t.sort(key=itemgetter(0))
        for user_id,views_count in groupby(per_t,key=itemgetter(0)):
            
            s = 0
            
            for i in views_count:
                s += i[1]
            new_pert.append([user_id,s])
            
            
            
        
        new_pert.sort(key=itemgetter(1),reverse=True)
        #print new_pert
        results.append(new_pert[:10])
        #break
    return results
            
        
            
            
        

