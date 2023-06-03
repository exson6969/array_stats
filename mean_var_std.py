import numpy as np

def calculate(list):
  if (len(list) != 9):
    raise ValueError("List must contain nine numbers.")

  array_2d = np.reshape(list, (3,3))

  calculations = {
  'mean': [np.mean(array_2d, axis=0).tolist(), np.mean(array_2d, axis=1).tolist(), np.mean(list)],
  'variance': [np.var(array_2d, axis=0).tolist(), np.var(array_2d, axis=1).tolist(), np.var(list)],
  'standard deviation': [np.std(array_2d, axis=0).tolist(), np.std(array_2d, axis=1).tolist(), np.std(list)],
  'max': [np.max(array_2d, axis=0).tolist(), np.max(array_2d, axis=1).tolist(), np.max(list)],
  'min': [np.min(array_2d, axis=0).tolist(), np.min(array_2d, axis=1).tolist(), np.min(list)],
  'sum': [np.sum(array_2d, axis=0).tolist(), np.sum(array_2d, axis=1).tolist(), np.sum(list)]
}

  return calculations
