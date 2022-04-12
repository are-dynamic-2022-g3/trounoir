import json

class DataType:
  NumberOfBlackHole = "nb_blackhole"
  NumberOfStars = "nb_stars"
  BiggestBlackHole = "biggest_bh"
 
current_data = {}

data = {}

def save_data():
  global data
  data_json = None
  with open("data.json", 'r') as f:
    data_json = json.load(f)

  if "times" not in data_json:
    data_json["times"] = 1
    data["data"] = {}
  else:
    data_json["times"] += 1

  t = str(data_json["times"])  

  data_json["data"][t] = data

  data = {}

  with open("data.json", 'w') as f:
    json.dump(data_json, f)

def clear_data():
  data_json = {
    "times" : 0,
    "data" : {}
  }
  with open("data.json", 'w') as f:
    json.dump(data_json, f)

    
     