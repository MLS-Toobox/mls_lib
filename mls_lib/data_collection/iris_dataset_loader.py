""" IRIS DATASET LOADER """
from mls_lib.orchestration.task import Task
from mls_lib.objects.data_frame import DataFrame
from sklearn import datasets

class IrisDatasetLoader(Task):
    """ Iris Dataset Loader """

    def __init__(self) -> None:
        super().__init__()
    
    def execute(self):
        iris = datasets.load_iris()
        iris_data = iris.data
        iris_target = iris.target
        
        iris_data_df = DataFrame()
        iris_data_df.set_data(iris_data)
        
        iris_target_df = DataFrame()
        iris_target_df.set_data(iris_target)
        
        self._set_output("data", iris_data_df)
        self._set_output("target", iris_target_df)
