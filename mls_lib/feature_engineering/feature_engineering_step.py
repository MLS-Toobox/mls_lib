from mls_lib.orchestration import Step

class FeatureEngineeringStep(Step):
    def __init__(self, **inputs) -> None:
        super().__init__(**inputs)