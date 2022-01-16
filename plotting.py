import matplotlib

matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt  # noqa
import numpy as np  # noqa

x_intervall_left = -5
x_intervall_right = 5
step_size = 0.05
number_of_steps = int((x_intervall_right - x_intervall_left) / step_size)

# creates a list of x values in the intervall of left->right
x_values = np.linspace(x_intervall_left, x_intervall_right, number_of_steps)
# define your function
func_x = lambda x: np.exp(x)
# calculate the y values for each x in x_values
y_values = [func_x(x) for x in x_values]
# define the value for the courve
label = "y=e^x"

fig1 = plt.figure()
plt.plot(x_values, y_values, "r", label=label)
plt.legend(loc='upper left')
plt.show()
