# Description

This is the task for Computational Practicum.

The program allows user to see the graph of the solution of the equation y=(x/3+1/6+(e^(2(x-1))(2^(2/3)-1/2)))^(3/2) with opportunity to change initial conditions, range and number of grid steps.

The user can change parameters of the equation and visibility of the corresponding solutions.
After changing any value, user should push the button `Update`.

Also, user can change any of the parameters without filling all of them.
If you want to change only 1 parameter, just fill only this form and push `Update` button.
The application will update only this parameter and display the new graph.

## Page 1

On the first page user can see the graph on which the following solutions are presented:

- Exact solution;
- Approximate solution using Euler's method;
- Approximate solution using Improved Euler's method;
- Approximate solution using Runge Kutta method.

Parameters:
- `x0` - starting point for x;
- `y0` - solution for starting point;
- `X` - endpoint for x;
- `steps` - the number of steps between `x0` and `X`.

## Page 2

There are local truncation errors (LTE) of each method.

## Page 3

There are changing LTE of each approximation method depending on the given step.

It calculates the maximum local error on the range [x0, X] for each number of steps on the range [n0, N] with step 1.

- `n0` - starting number of steps
- `N` - end number of steps

## Tests

The program has tests of functionality.

They are located in the **tests** directory.

## Libraries

Required **Python** version: `3.8` or above.

# Installation

1. Clone repo: `git clone https://github.com/Mousatat/ComputationalPracticum-Mousatat.git`
2. Open the directory: `cd ComputationalPracticum/`
3. Install requirements: `pip install -r requirements.txt`
4. Open the application directory: `cd app/`
5. Launch the application on the current directory: `python3 .`

# Tests

You can check correctness of the installation and functionality of the program by launching the tests.

Unfortunately, you can run tests only from Pycharm by adding new configuration:

1. Open `Edit Configurations...` (push the button at the left of `Run` button)
2. Add new `Python tests` > `Unittests`
3. Call it as you want (optional)
4. Choose **Script path** and choose folder `{PATH-TO-PROJECT}/tests/model`
5. Press `OK` button
6. Launch the configuration
