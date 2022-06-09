arr = np.array([3, 5, 7, 2, 8, 10, 11, 65, 72, 81, 99, 100, 150])
df = np.convolve(arr,np.ones(3),'valid')/3
df
