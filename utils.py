import yaml
from typing import Dict

def get_prompt(prompt_name: str, config_path: str = "prompts.yaml") -> Dict[str, str]:
    """
    Reads the prompt configuration from a YAML file and returns the system and user messages.
    """
    with open(config_path, "r") as f:
        config = yaml.safe_load(f)
    
    if prompt_name not in config:
        raise ValueError(f"Prompt '{prompt_name}' not found in {config_path}")
    
    return config[prompt_name]

def format_prompt(messages: Dict[str, str], **kwargs) -> Dict[str, str]:
    """
    Formats the user message with the provided keyword arguments.
    """
    return {
        "system": messages["system"],
        "user": messages["user"].format(**kwargs)
    }
