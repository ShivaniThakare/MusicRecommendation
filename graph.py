import matplotlib.pyplot as plt
import matplotlib.ticker as plticker
import numpy as np

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [-1680.4841862022877, -1309.740696579218 , -291.53875797986984, 303.52625727653503 , 77.2940861582756, 500.63980570435524, 864.5055113434792, 962.1560164093971, 1023.2745914459229, 1071.6613954305649]
plt.plot(x, y)
plt.xticks(np.arange(min(x), max(x)+1, 1.0))
plt.xlabel('Episode (Single Recommendation of 10 Songs)')
plt.ylabel('Cumulative Reward')
plt.title('Cumulative Reward for Q-Learning Model')
plt.show()


x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [0.3, 0.2 , 0.3, 0.3, 0.4, 0.5, 0.7, 0.5, 0.6, 0.6]
plt.plot(x, y)
plt.xticks(np.arange(min(x), max(x)+1, 1.0))
plt.xlabel('Episode (Single Recommendation of 10 Songs)')
plt.ylabel('Percentage Like Per Episode')
plt.title('Like Song Perentage for Recommended Playlist')
plt.show()

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [4378, 4399, 5082, 5540, 5973, 6313, 7097, 7596, 8831, 8763]
plt.plot(x, y)
plt.xticks(np.arange(min(x), max(x)+1, 1.0))
plt.xlabel('Episode (Single Recommendation of 10 Songs)')
plt.ylabel('Song Play Count (Time in Sec)')
plt.title('Song Play Count for Recommended Playlist')
plt.show()