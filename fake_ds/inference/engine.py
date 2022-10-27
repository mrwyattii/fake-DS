import fake_ds

from ..module_inject.replace_module import generic_injection

class InferenceEngine(object):
    def __init__(self, model, policy="auto"):
        if policy == "auto":
            model, policy = generic_injection(model)
            self.model = model
            self.policy = policy
        else:
            raise NotImplementedError("no custom policies supported")
