# import matplotlib.pyplot as plt
# import numpy as np
# fig, ax = plt.subplots()             # Create a figure containing a single Axes.
# ax.plot([1, 2, 3, 4], [1, 4, 2, 3])  # Plot some data on the Axes.
# plt.show()

#%%
import matplotlib
# matplotlib.use('tkAgg')
import PyQt5
matplotlib.use('Qt5Agg')

import matplotlib.pyplot as plt
# from matplotlib.backends.backend_tkagg import FigureCanvasAgg
import numpy as np
plt.close('all')




#%%
x = np.linspace(0, 2, 100)  # Sample data.

plt.figure()
plt.plot(x, x, label='linear')  # Plot some data on the (implicit) Axes.
plt.plot(x, x**2, label='quadratic')  # etc.
plt.plot(x, x**3, label='cubic')
plt.xlabel('x label')
plt.ylabel('y label')
plt.title("Simple Plot")
plt.legend()
plt.show()


#%%
plt.figure()
# plt.suptitle('pcf - neff - (epochs-{}) - pyTorch'.format(epochs), fontsize=25, color='r', fontweight='bold')     ## giving title on top of all subplots


plt.subplot(231)
plt.show()  # This line is needed to display the plot.

plt.plot(x, x, 'r-', linewidth=3, label='mse_loss_train')
plt.plot(x, x**2, 'b-', linewidth=3, label='mse_loss_validation')
plt.legend(loc='best', fontsize=10)
plt.xlabel('epochs#', fontsize=15)
plt.show()  # This line is needed to display the plot.
