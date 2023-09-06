
import pickle


cricket_players = [
    {"name": "virat kohli", "score": 750},
    {"name": "Yashasvi", "score": 650}
]

# dump the data using pickle
with open('lists_of_dicts.pkl', 'wb') as f:
    pickle.dump(cricket_players, f)

# load the data using pickle
with open('lists_of_dicts.pkl', 'rb') as f:
    obj = pickle.load(f)
print(obj)
