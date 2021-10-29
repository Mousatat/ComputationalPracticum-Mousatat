import eel
import matplotlib.pyplot as plt

from model.exceptions.incorrect_params_error import IncorrectParamsError
from model.model import Model


class WebView:
    """
    Represents the View in MVC pattern.
    It displays the application to the user.
    """
    def __init__(self, model: Model):
        """ View initialization. """
        self.model = model

    def run(self) -> None:
        """
        Start to display the system.
        """
        self._change_image({}, 1, callback_needed=False)
        eel.init('view/static')
        eel.start('index.html', size=(1000, 600))

    def show_page1(self, show_y=True, show_euler=True, show_ie=True, show_rk=True) -> None:
        """
        Display page 1 to user.
        :param show_y: flag to display on the graph of the exact solution.
        :param show_euler: flag to display on the graph of the approximate solution using Euler's algorithm.
        :param show_ie: flag to display on the graph of the approximate solution using Improved Euler's algorithm.
        :param show_rk: flag to display on the graph of the approximate solution using Runge Kutta algorithm.
        """
        data = {'X': self.model.x_plane()}
        if show_y:
            data['Y exact'] = self.model.exact()
        if show_euler:
            data['Y Euler'] = self.model.euler_method()
        if show_ie:
            data['Y Improved Euler'] = self.model.improved_euler_method()
        if show_rk:
            data['Y Runge Kutta'] = self.model.runge_kutta_method()
        self._change_image(data, 1)

    def show_page2(self, method: ['lte', 'gte'] = None, show_euler=True, show_ie=True, show_rk=True) -> None:
        """
        Display page 2 to user.
        :param method: method of calculation of error between approximation method and exact solution.
         Can be one of ['lte', 'gte']
        :param show_euler: flag to display on the graph of the approximate solution using Euler's algorithm.
        :param show_ie: flag to display on the graph of the approximate solution using Improved Euler's algorithm.
        :param show_rk: flag to display on the graph of the approximate solution using Runge Kutta algorithm.
        """
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
        self._change_image(data, 2)

    def show_page3(self, method: ['lte', 'gte'] = None, show_euler=True, show_ie=True, show_rk=True) -> None:
        """
        Display page 3 to user.
        :param method: method of calculation of error between approximation method and exact solution.
         Can be one of ['lte', 'gte']
        :param show_euler: flag to display on the graph of the approximate solution using Euler's algorithm.
        :param show_ie: flag to display on the graph of the approximate solution using Improved Euler's algorithm.
        :param show_rk: flag to display on the graph of the approximate solution using Runge Kutta algorithm.
        """
        if method is not None and method not in ['lte', 'gte']:
            raise IncorrectParamsError('"method" with values "lte" or "gte"')

        data = {'X': self.model.n_plane()}
        if method == 'gte':
            if show_euler:
                data['Euler GTE Error'] = self.model.euler_gte_errors()
            if show_ie:
                data['Improved Euler GTE Error'] = self.model.improved_euler_gte_errors()
            if show_rk:
                data['Runge Kutta GTE Error'] = self.model.runge_kutta_gte_errors()
        else:
            if show_euler:
                data['Euler LTE Error'] = self.model.euler_lte_errors()
            if show_ie:
                data['Improved Euler LTE Error'] = self.model.improved_euler_lte_errors()
            if show_rk:
                data['Runge Kutta LTE Error'] = self.model.runge_kutta_lte_errors()
        self._change_image(data, 3)

    def _change_image(self, table: dict, page_number: int, callback_needed=True) -> None:
        """
        Creates a graph with given parameters and saves it to 'view/static/img' directory.
        :param table: a dictionary with all data needed to represent the graph.
         Each value should be an array with common size.
        :param page_number: a page number for axes' name.
        :param callback_needed: special flag for sending callback to the application (graphical part).
        """
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
        if len(table) > 1:
            plt.legend()
        plt.savefig('view/static/img/graph.png', bbox_inches='tight', transparent=True)
        if callback_needed:
            eel.updateImage()()
        plt.close()
