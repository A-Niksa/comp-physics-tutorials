# importing config
from config import derivative_increment


# defining the derivative calculation function
def calculate_derivative(x, function):
    value_at_back = function(x - derivative_increment)
    value_at_front = function(x + derivative_increment)
    return (value_at_front - value_at_back) / (2 * derivative_increment)