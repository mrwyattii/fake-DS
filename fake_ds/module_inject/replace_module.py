import fake_ds
import fake_mii

from fake_ds import logger
from fake_mii.policies import GPTInjectionPolicy

def generic_injection(model):
    if model == "gpt":
        policy = GPTInjectionPolicy()
    else:
        raise NotImplementedError(f"model {model} not supported")
    return model, policy

def replace_transformer_layer():
    return 0
