# Import libraries
import torch 
import numpy as np

# data
data = [[1, 2], [3, 4]]
data_tensor = torch.tensor(data)
print(data_tensor, "\n", type(data_tensor))

# some more data
data = [[1,2], [3,4], [5,6]]
np_data = np.array(data)
print(np_data, type(np_data))
np_data_tensor = torch.from_numpy(np_data)
print(np_data_tensor, "\n", type(np_data_tensor))

print(torch.zeros(5))