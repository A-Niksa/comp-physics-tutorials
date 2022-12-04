# ----------------------------- importing config ----------------------------- #
import config as cfg

# ----------- defining the functions used for solving the equation ----------- #
def update_interval_parameters(interval_start, interval_end, equation_function):
    interval_middle = (interval_start + interval_end) / 2

    value_at_start = equation_function(interval_start)
    value_at_middle = equation_function(interval_middle)
    value_at_end = equation_function(interval_end)

    return interval_middle, value_at_start, value_at_middle, value_at_end


def solve(interval_start, interval_end, root_error, equation_function):
    current_error = root_error * 10  # initial value of current_error so that we can enter the while loop
    number_of_iterations = 0
    interval_middle = interval_start - 1  # default value; will let us know that no root has been found

    while root_error < current_error:
        interval_middle, value_at_start, value_at_middle, value_at_end = update_interval_parameters(interval_start,
                                                                                                    interval_end,
                                                                                                    equation_function)

        if value_at_start * value_at_middle < 0:
            interval_end = interval_middle
        else:
            interval_start = interval_middle

        current_error = abs(value_at_middle)

        number_of_iterations += 1
        if number_of_iterations > cfg.max_number_of_iterations:
            break

    return interval_middle


# ------------------------ solving the given equation ------------------------ #
stable_root = solve(cfg.interval_1_start, cfg.interval_1_end, cfg.root_error, cfg.eqn_function)
stable_value = cfg.eqn_function(stable_root)

unstable_root = solve(cfg.interval_2_start, cfg.interval_2_end, cfg.root_error, cfg.eqn_function)
unstable_value = cfg.eqn_function(unstable_root)

# --------------------------- printing the results --------------------------- #
print("The stable equilibrium is at approximately r = " + str(stable_root) + " where F(r) is " + str(stable_value) + ".")
print("The unstable equilibrium is at approximately r = " + str(unstable_root) + " where F(r) is " + str(unstable_value) + ".")