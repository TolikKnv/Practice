import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

df = pd.DataFrame({
    "X": [1, 2, 3, 4, 5],
    "Y": [2, 3, 5, 7, 11],
    "Z": [1, 4, 9, 16, 25]
})

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(df["X"], df["Y"], df["Z"])


ax.plot(df["X"], df["Y"], df["Z"])

ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

plt.show()
