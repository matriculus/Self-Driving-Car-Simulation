import pandas as pd
import numpy as np

data = pd.read_csv("data/driving_log.csv", names=['center', 'left', 'right', 'steering', 'throttle', 'reverse', 'speed'])
center = np.asarray(data['center'])
left = np.asarray(data['left'])
right = np.asarray(data['right'])
data1 = data.drop(columns=['center', 'left', 'right'])

adr = center[0].find("IMG")

center = pd.DataFrame({"center" : np.asarray([a[adr:] for a in center])})
left = pd.DataFrame({"left" : np.asarray([a[adr:] for a in left])})
right = pd.DataFrame({"right" : np.asarray([a[adr:] for a in right])})

data1 = pd.concat([center, left, right, data1], axis=1)

data1.to_csv("data/driving_log.csv", index=False, header=False)
