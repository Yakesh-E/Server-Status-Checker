import pickle

with open('server_status_history.pkl', 'rb') as f:
    history = pickle.load(f)

print(history)