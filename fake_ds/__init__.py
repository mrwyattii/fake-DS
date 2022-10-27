__version__ = "1.0"
from .logger import logger
from .module_inject import replace_transformer_layer
from .inference.engine import InferenceEngine

def init_inference(model, policy="auto"):
    engine = InferenceEngine(model, policy)
    return engine
