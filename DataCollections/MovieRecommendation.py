db = {
    "action" : ['baahubali','kgf','hulk','ironman','batman','superman','thor',
                'avengers','antman','captain america','aquaman','bang bang'],
    "comedy" : ['zero','dhamaal','hera pheri'],
    "drama" : ['zero'],
    "biopic" : ['ms dhoni','sanju'],
    "horror" : ['the ring','the nun']
    }

user_1 = {'baahubali','kgf','the ring','zero','the nun','hulk','ironman',
          'batman','superman','thor','ms dhoni','dhamaal'}

# jaccard distance
'''
sim_action = user_1.intersection(db['action'])
union_action = user_1.union(db['action'])
d = len(sim_action) / len(union_action)
print(d*100)
'''

distances = {}
for category in db:
    sim_action = user_1.intersection(db[category])
    union_action = user_1.union(db[category])
    d = len(sim_action) / len(union_action)
    distances[category] = round(d * 100,2)

print(distances)

items = distances.items()
category = max(items, key = lambda x : x[1])[0]
recommendedMovies = set(db[category]) - user_1
print("Recommended Movies are",recommendedMovies)







