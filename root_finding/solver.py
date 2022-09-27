# importing config and derivative calculator
import config as cfg
from derivative_calculator import calculate_derivative


# defining the functions used for solving the equation
def update_interval_parameters(interval_start, interval_end, equation_function):
    interval_middle = (interval_start + interval_end) / 2

    value_at_start = equation_function(interval_start)
    value_at_middle = equation_function(interval_middle)
    value_at_end = equation_function(interval_end)

    return interval_middle, value_at_start, value_at_middle, value_at_end


def calculate_error(guessed_root, equation_function):
    return abs(equation_function(guessed_root))


def calculate_next_potential_root(previous_potential_root, equation_function):
    return previous_potential_root - equation_function(previous_potential_root) / \
           calculate_derivative(previous_potential_root, equation_function)


def solve(initial_guess, root_error, equation_function):
    potential_root = initial_guess
    current_error = calculate_error(potential_root, equation_function)
    number_of_iterations = 0

    while root_error < current_error:
        potential_root = calculate_next_potential_root(potential_root, equation_function)
        current_error = calculate_error(potential_root, equation_function)

        number_of_iterations += 1
        if number_of_iterations > cfg.max_number_of_iterations:
            break

    return potential_root


# solving the given equation
found_root = solve(cfg.initial_guess, cfg.root_error, cfg.eqn_function)
root_value = cfg.eqn_function(found_root)

# printing the results
print("x = " + str(found_root))
print("f(x) = " + str(root_value))
