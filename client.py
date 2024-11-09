import yaml
from openai import OpenAI
from typing import Optional
from config import Config

def setup_client(config_path: str = "config.yml") -> Optional[object]:
    """
    Sets up a client based on the configuration in config.yml.
    Currently supports OpenAI client setup.
    Args:
        config_path (str): Path to the config file. Defaults to "config.yml"
    Returns:
        Optional[object]: Configured client object or None if setup fails
    """

    config = Config()
    try:
        client_config = config.get('client')
        if not client_config:
            raise ValueError("Invalid config: 'client' field not found")

        if 'openai' in client_config.keys():
            api_key = client_config['openai'].get('api_key', None)
            if api_key is None:
                raise ValueError("Invalid config: OpenAI API key not found")

            return OpenAI(api_key=str(api_key))

        else:
            raise ValueError(f"Unsupported client type: {client_config}")

    except FileNotFoundError:
        print(f"Config file not found: {config_path}")
        return None
    except yaml.YAMLError as e:
        print(f"Error parsing YAML config: {e}")
        return None
    except Exception as e:
        print(f"Error setting up client: {e}")
        return None

