
class BaseInjectionPolicy(object):
    def __init__(self):
        import fake_ds
        self.ds_version = fake_ds.__version__

    def attention(self):
        return "attention"
