import numpy as np
import pandas as pd


class lr:
    def __init__(self, x, y):
        """
        :param x: array-like object with x coordinates (list, array, numpy array,etc.))
        :param y: array-like object with y coordinates corresponding to x coordinates in 'x' (list, array, numpy array,etc.)

        INSTANCE ATTRIBUTES

        x - np array of x coordinates created from x parameter
        y - np array of y coordinates crated from y parameter

        INSTANCE ATTRIBUTES/PROPERTIES THAT ARE SOLELY DEPENDENT ON x and y
        (i.e. can't be changed without you changing the values of the x and y attributes)

        slope -  slope of best fit line(bfl)
        slope00 - slope of bfl through origin
        intercept - intercept of bfl
        slope_std_error - standard error of slope of bfl
        slope_std_error00 - standard error of bfl through origin
        intercept_std_error - standard error of bfl
        r - correlation coefficient for bfl
        r00 - correlation coefficient for bfl through origin
        r2 - correlation coefficient squared for bfl
        r2_00 - correlation coefficient squared for bfl through origin

        METHODS

        results(self, zero_intercept=False, both=False):
        :param zero_intercept: if True, results are returned for best fit line through origin. Default False
        :param both: if True, results are returned for both the best fit line through the origin and regular best fit line.
        Default False. If True, overrides zero_intercept argument.
        :return: DataFrame containing slope, intercept, std. error slope, std. error intercept, r, and r-squared for the chosen best fit line(s).

        print_results(self,zero_intercept = False, both = False):
            prints the DataFrame made by passing the same parameter value to the results function.


        Printing Instance Object:
        Example:
        data = lr(x,y)   <--- creation of lr instance object name data
        print(data)   <-- (printing data object).
        Using print function on instance object will print the
        - slope
        - intercept
        - std. error of slope
        - standard error of intercept
        - correlation coefficient
        - correlation coefficient squared
        for both the bfl and the bfl through the origin
        """
        self.__x = np.array(x)
        self.__y = np.array(y)

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = np.array(x)

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.__y = np.array(y)

    @property
    def n(self):
        '''
        :return: number of data points
        '''
        return len(self.__x)

    @property
    def slope(self):
        '''

        :return: slope of best fit line through origin
        '''
        return ((self.__x - self.__x.mean()) * self.__y).sum() / ((self.__x - self.__x.mean()) ** 2).sum()

    @property
    def slope00(self):
        '''

        :return: slope of best-fit line through origin
        '''
        return ((self.__x * self.__y).sum()) / (self.__x ** 2).sum()

    @property
    def intercept(self):
        '''

        :return: y-intercept of the best fit line
        '''
        return self.__y.mean() - self.slope * self.__x.mean()

    @property
    def intercept00(self):
        '''

        :return: 0.0 (y intercept of best line through origin)
        '''
        return 0.0

    @property
    def slope_std_error(self):
        '''

        :return: standard error of the slope of the best fit line
        '''
        return np.sqrt((1 / (self.n - 2)) * (((self.__y - self.slope * self.__x - self.intercept) ** 2).sum()) / (
            ((self.__x - self.__x.mean()) ** 2).sum()))

    @property
    def slope_std_error00(self):
        '''
        :return: standard error of the slope of the best fit line through the origin
        '''
        return np.sqrt((((self.__y - self.slope00 * self.__x) ** 2).sum()) / ((self.n - 1) * (self.__x ** 2).sum()))

    @property
    def intercept_std_error(self):
        '''
        :return: standard error of the intercept of the best fit line
        '''
        return np.sqrt(((1 / self.n) + (self.__x.mean() ** 2) / (((self.__x - self.__x.mean()) ** 2).sum())) * (
            ((self.__y - self.slope * self.__x - self.intercept) ** 2).sum()) / (self.n - 2))

    @property
    def r(self):
        '''

        :return: correlation coefficient for the best fit line
        '''
        return (self.n * ((self.__x * self.__y).sum()) - (self.__x.sum()) * (self.__y.sum())) / (
            (((self.n * (self.__x ** 2).sum()) - (self.__x.sum()) ** 2) ** .5) * (
                (self.n * ((self.__y ** 2).sum()) - (self.__y.sum()) ** 2) ** .5))

    @property
    def r00(self):
        '''

        :return: correlation coefficient for the best fit line through the origin
        '''
        return np.sqrt(1.0 - ((((self.__y - self.slope00 * self.__x) ** 2).sum()) / ((self.__y ** 2).sum())))

    @property
    def r2(self):
        '''

        :return: r-squared (coefficient coefficient squared) for best fit line
        '''
        return self.r ** 2

    @property
    def r2_00(self):
        '''

        :return: r-squared (coefficient coefficient squared) for best fit line through origin
        '''
        return self.r00 ** 2

    def results(self, zero_intercept=False, both=False):
        '''

        :param zero_intercept: if True, results are returned for best fit line through origin. Default False
        :param both: if True, results are returned for both the best fit line through the origin and regular best fit line.
        Default False. If True, overrides zero_intercept argument.
        :return: DataFrame containing slope, intercept, std. error slope, std. error intercept, r, and r-squared for the chosen best fit line(s).
        '''
        if (zero_intercept == False) and (both == False):
            data = {'Slope': [self.slope], 'Intercept': [self.intercept], 'Std. Error, Slope': [self.slope_std_error],
                    'Std. Error, Intercept': [self.intercept_std_error], 'r': [self.r], 'r-squared': [self.r2]}
            cols = ['Slope', 'Intercept', 'Std. Error, Slope', 'Std. Error, Intercept', 'r', 'r-squared']
            ind = ['BFL']
            return pd.DataFrame(data, index=ind, columns=cols)
        elif (zero_intercept == True) and (both == False):
            data = {'Slope': [self.slope00], 'Intercept': [self.intercept00],
                    'Std. Error, Slope': [self.slope_std_error00],
                    'r': [self.r00], 'r-squared': [self.r2_00]}
            cols = ['Slope', 'Intercept', 'Std. Error, Slope', 'r', 'r-squared']
            ind = ['BFL Through (0,0)']
            return pd.DataFrame(data, index=ind, columns=cols)
        else:
            data = {'Slope': [self.slope, self.slope00], 'Intercept': [self.intercept, 0.0],
                    'Std. Error, Slope': [self.slope_std_error, self.slope_std_error00],
                    'Std. Error, Intercept': [self.intercept_std_error, np.nan], 'r': [self.r, self.r00],
                    'r-squared': [self.r2, self.r2_00]}
            col = ['Slope', 'Intercept', 'Std. Error, Slope', 'Std. Error, Intercept', 'r', 'r-squared']
            ind = ['BFL', 'BFL Through (0,0)']
            return pd.DataFrame(data, index=ind, columns=col)

    def print_results(self, zero_intercept=False, both=False):
        '''
        :param
        zero_intercept: if True, results are returned for best fit line through origin.Default False
        :param
        both:
        if True, results are returned for both the best fit line through the origin and regular best fit line.
        Default False.If True, overrides zero_intercept argument.
        :prints: DataFrame containing slope, intercept, std.error slope, std.error intercept, r, and r - squared for the chosen best fit line(s).
        '''
        print(self.results(zero_intercept, both))

    def __str__(self):
        bfl_string = 'LINEAR LEAST-SQUARES REGRESSION ANALYSIS\n\nBEST FIT LINE:\n'
        slope_string = 'slope = ' + str(self.slope) + '\n'
        intercept_string = 'intercept = ' + str(self.intercept) + '\n'
        slope_error_string = 'std. error, slope = ' + str(self.slope_std_error) + '\n'
        intercept_error_string = 'std. error, intercept = ' + str(self.intercept_std_error) + '\n'
        r_string = 'r = ' + str(self.r) + '\n'
        r2_string = 'r-squared = ' + str(self.r2) + '\n'
        number_of_data_points = 'number of data points = ' + str(self.n)
        bfl_data = bfl_string + slope_string + intercept_string + slope_error_string + intercept_error_string + r_string + r2_string + number_of_data_points + '\n\n'
        bfl_string00 = 'BEST FIT LINE THROUGH THE ORIGIN, (0,0):\n'
        slope_string00 = 'slope = ' + str(self.slope00) + '\n'
        intercept_string00 = 'intercept = ' + str(self.intercept00) + '\n'
        slope_error_string00 = 'std. error, slope = ' + str(self.slope_std_error00) + '\n'
        r_string00 = 'r = ' + str(self.r00) + '\n'
        r2_string00 = 'r-squared = ' + str(self.r2_00) + '\n'
        bfl_data00 = (bfl_string00 + slope_string00 + intercept_string00
                      + slope_error_string00 + r_string00 + r2_string00
                      + number_of_data_points)
        return (bfl_data + bfl_data00)
