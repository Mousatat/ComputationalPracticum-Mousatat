import sys

from model.model import Model


class ConsoleController:
    def __init__(self, model: Model, view):
        self.model = model
        self.view = view

        self.page1_config = {'show_y': True, 'show_euler': True, 'show_ie': True, 'show_rk': True}
        self.page2_config = {'method': 'lte', 'show_euler': True, 'show_ie': True, 'show_rk': True}
        self.page3_config = {'method': 'lte', 'show_euler': True, 'show_ie': True, 'show_rk': True}

    def update_page1(self):
        self.model.x0 = self.view.get_x0()
        self.model.y0 = self.view.get_y0()
        self.model.X = self.view.get_X()
        self.model.steps = self.view.get_count()
        self.page1_config['show_y'] = self.view.get_show_y()
        self.page1_config['show_euler'] = self.view.get_show_euler()
        self.page1_config['show_ie'] = self.view.get_show_ie()
        self.page1_config['show_rk'] = self.view.get_show_rk()

        self.show_page1()

    def update_page2(self):
        self.model.x0 = self.view.get_x0()
        self.model.y0 = self.view.get_y0()
        self.model.X = self.view.get_X()
        self.model.steps = self.view.get_count()
        self.page2_config['method'] = self.view.get_method()
        self.page2_config['show_euler'] = self.view.get_show_euler()
        self.page2_config['show_ie'] = self.view.get_show_ie()
        self.page2_config['show_rk'] = self.view.get_show_rk()

        self.show_page2()

    def update_page3(self):
        self.model.n0 = self.view.get_n0()
        self.model.N = self.view.get_N()
        self.page3_config['method'] = self.view.get_method()
        self.page3_config['show_euler'] = self.view.get_show_euler()
        self.page3_config['show_ie'] = self.view.get_show_ie()
        self.page3_config['show_rk'] = self.view.get_show_rk()

        self.show_page3()

    def show_page1(self):
        self.view.show_page1(**self.page1_config)

    def show_page2(self):
        self.view.show_page2(**self.page2_config)

    def show_page3(self):
        self.view.show_page3(**self.page3_config)

    def run(self):
        print('Please, choose the option:')
        print('(1): show page #1')
        print('(2): show page #2')
        print('(3): show page #3')
        print('(exit): close the program')
        inp = input()
        if inp == '1':
            self.show_page1()
            self._page1()
        elif inp == '2':
            self.show_page2()
            self._page2()
        elif inp == '3':
            self.show_page3()
            self._page3()
        elif inp == 'exit':
            sys.exit(0)
        else:
            self.run()

    def _page1(self):
        inp = ''
        while inp != 'exit':
            print('Please, choose the option:')
            print('(1): change x0')
            print('(2): change X')
            print('(3): change y0')
            print('(4): change a number of steps N')
            print('(6): update the current page')
            print('(7): UPDATE THE PAGE')
            print('(exit): close the program')
            inp = input()
            if inp == '1':
                self.model.x0 = self.view.get_x0()
            elif inp == '2':
                self.model.X = self.view.get_X()
            elif inp == '3':
                self.model.y0 = self.view.get_y0()
            elif inp == '4':
                self.model.steps = self.view.get_count()
            elif inp == '6':
                self.update_page1()
            elif inp == '7':
                self.show_page1()

    def _page2(self):
        inp = ''
        while inp != 'exit':
            print('Please, choose the option:')
            print('(1): change x0')
            print('(2): change X')
            print('(3): change y0')
            print('(4): change a number of steps N')
            print('(5): change turnaround method')
            print('(6): update the current page')
            print('(7): UPDATE THE PAGE')
            print('(exit): go to main menu')
            inp = input()
            if inp == '1':
                self.model.x0 = self.view.get_x0()
            elif inp == '2':
                self.model.X = self.view.get_X()
            elif inp == '3':
                self.model.y0 = self.view.get_y0()
            elif inp == '4':
                self.model.steps = self.view.get_count()
            elif inp == '5':
                self.page2_config['method'] = self.view.get_method()
            elif inp == '6':
                self.update_page2()
            elif inp == '7':
                self.show_page2()

    def _page3(self):
        inp = ''
        while inp != 'exit':
            print('Please, choose the option:')
            print('(1): change n0')
            print('(2): change N')
            print('(5): change turnaround method')
            print('(6): update the current page')
            print('(7): UPDATE THE PAGE')
            print('(exit): go to main menu')
            inp = input()
            if inp == '1':
                self.model.n0 = self.view.get_n0()
            elif inp == '2':
                self.model.N = self.view.get_N()
            elif inp == '5':
                self.page3_config['method'] = self.view.get_method()
            elif inp == '6':
                self.update_page3()
            elif inp == '7':
                self.show_page3()
