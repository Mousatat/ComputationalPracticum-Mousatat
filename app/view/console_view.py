from tabulate import tabulate
import matplotlib.pyplot as plt

from model.model import Model
from model.exceptions.incorrect_params_error import IncorrectParamsError


class ConsoleView:
    def __init__(self, model: Model):
        self.model = model

    def show_page1(self, show_y=True, show_euler=True, show_ie=True, show_rk=True) -> None:
        data = {'X': self.model.x_plane()}
        if show_y:
            data['Y exact'] = self.model.exact()
        if show_euler:
            data['Y Euler'] = self.model.euler_method()
        if show_ie:
            data['Y Improved Euler'] = self.model.improved_euler_method()
        if show_rk:
            data['Y Runge Kutta'] = self.model.runge_kutta_method()
        ConsoleView.print_table(data, 1)

    def show_page2(self, method: ['lte', 'gte'] = None, show_euler=True, show_ie=True, show_rk=True) -> None:
        if method is not None and method not in ['lte', 'gte']:
            raise IncorrectParamsError('"method" with values "lte" or "gte"')

        data = {'X': self.model.x_plane()}
        if method == 'gte':
            if show_euler:
                data['Euler GTE Error'] = self.model.euler_gte()
            if show_ie:
                data['Improved Euler GTE Error'] = self.model.improved_euler_gte()
            if show_rk:
                data['Runge Kutta GTE Error'] = self.model.runge_kutta_gte()
        else:
            if show_euler:
                data['Euler LTE Error'] = self.model.euler_lte()
            if show_ie:
                data['Improved Euler LTE Error'] = self.model.improved_euler_lte()
            if show_rk:
                data['Runge Kutta LTE Error'] = self.model.runge_kutta_lte()
        ConsoleView.print_table(data, 2)

    def show_page3(self, method: ['lte', 'gte'] = None, show_euler=True, show_ie=True, show_rk=True) -> None:
        if method is not None and method not in ['lte', 'gte']:
            raise IncorrectParamsError('"method" with values "lte" or "gte"')

        data = {'X': self.model.n_plane()}
        if method == 'gte':
            if show_euler:
                data['Euler GTE Error'] = self.model.euler_lte_errors()
            if show_ie:
                data['Improved Euler GTE Error'] = self.model.improved_euler_lte_errors()
            if show_rk:
                data['Runge Kutta GTE Error'] = self.model.runge_kutta_lte_errors()
        else:
            if show_euler:
                data['Euler LTE Error'] = self.model.euler_gte_errors()
            if show_ie:
                data['Improved Euler LTE Error'] = self.model.improved_euler_gte_errors()
            if show_rk:
                data['Runge Kutta LTE Error'] = self.model.runge_kutta_gte_errors()
        ConsoleView.print_table(data, 3)

    def get_x0(self) -> float:
        try:
            a = float(input('Enter x0: '))
            return a
        except ValueError:
            return 1.

    def get_X(self) -> float:
        try:
            a = float(input('Enter X: '))
            return a
        except ValueError:
            return 1.5

    def get_y0(self) -> float:
        try:
            a = float(input('Enter y0: '))
            return a
        except ValueError:
            return 2.

    def get_count(self) -> int:
        try:
            a = int(input('Enter a number of steps (N): '))
            if a < 0:
                raise ValueError('Number has to be positive')
            return a
        except Exception:
            return 6

    def get_n0(self) -> int:
        try:
            a = int(input('Enter n0: '))
            if a < 0:
                raise ValueError('Number has to be positive')
            return a
        except Exception:
            return 1

    def get_N(self) -> int:
        try:
            a = int(input('Enter N: '))
            if a < 0:
                raise ValueError('Number has to be positive')
            return a
        except Exception:
            return 100

    def get_method(self) -> str:
        method = input('Enter truncation method: (1): LTE (2): GTE\n')
        if method == '1':
            return 'lte'
        elif method == '2':
            return 'gte'
        else:
            print('Sorry, but there is no that option')
            return 'lte'

    def get_show_y(self) -> bool:
        res = input('Is Y-exact needed: (y/n): ')
        if res == 'y':
            return True
        else:
            return False

    def get_show_euler(self) -> bool:
        res = input('Is Euler approximation needed: (y/n): ')
        if res == 'y':
            return True
        else:
            return False

    def get_show_ie(self) -> bool:
        res = input('Is Improved Euler approximation needed: (y/n): ')
        if res == 'y':
            return True
        else:
            return False

    def get_show_rk(self) -> bool:
        res = input('Is Runge Kutta approximation needed: (y/n): ')
        if res == 'y':
            return True
        else:
            return False

    @staticmethod
    def print_table(table: dict, page_number: int):
        print(tabulate(table, headers='keys', tablefmt='fancy_grid'))
        plt.title(f'Page #{page_number}')
        for key in table.keys():
            if key == 'X':
                continue
            plt.plot(table['X'], table[key], label=key)
        if page_number == 1:
            plt.xlabel('x')
            plt.ylabel('y')
        elif page_number == 2:
            plt.xlabel('x')
            plt.ylabel('Error')
        elif page_number == 3:
            plt.xlabel('n')
            plt.ylabel('Error')
        plt.legend()
        plt.savefig('view/static/img/graph.png', bbox_inches='tight', transparent=True)
        plt.show()
