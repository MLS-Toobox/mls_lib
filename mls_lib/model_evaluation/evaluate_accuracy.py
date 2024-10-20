""" Accuracy evaluation step. """

from mls_lib.orchestration.task import Task
from mls_lib.objects.data_frame import DataFrame
from mls_lib.objects.models.model import Model
class EvaluateAccuracy(Task):
    """ Accuracy evaluation step. """
    def __init__(self) -> None:
        super().__init__()

        self.features = DataFrame()
        self.truth = DataFrame()
        self.model = Model()
    
    def set_data(self, features : DataFrame, truth : DataFrame, model : Model) -> None:
        self.features = features
        self.truth = truth
        self.model = model

    def execute(self) -> None:

        result = self.model.score(self.features.get_data(), self.truth.get_data())

        self._set_output("result", result)
        