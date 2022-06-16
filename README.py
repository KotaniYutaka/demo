t = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0] #「2」を正解とする

def sum_squared_error(y, t):
  return 0.5 * np.sum((y-t)**2)
