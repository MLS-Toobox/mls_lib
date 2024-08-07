""" Replace Null : Replace Null Data Cleaning Step """
from mls_lib.data_cleaning import DataCleaningStep
from mls_lib.objects import Object

class ReplaceNull(DataCleaningStep):
    """ Replace Null : Replace Null Data Cleaning Step """
    def __init__(self, strategy : str, column : str, data_in : Object):
        super().__init__(
            data_in = data_in
        )
        self.strategy = strategy
        self.column = column

    def execute(self):
        data = self._get_input("data_in").copy()

        df = data.getData()
        if self.strategy == 'average':
            self.__use_avg(df)
        elif self.strategy == 'zero':
            self.__use_zero(df)
        elif self.strategy == 'mode':
            self.__use_mode(df)

        data.setData(df)

        self._set_output("out", data)

        self.finish_execution()

    def __use_avg(self, df):
        df[self.column] = df[self.column].fillna(df[self.column].mean())

    def __use_mode(self, df):
        df[self.column] = df[self.column].fillna(df[self.column].mode()[0])

    def __use_zero(self, df):
        df[self.column] = df[self.column].fillna(0)
