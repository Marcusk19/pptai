import yaml


class Config:
    def __init__(self, config_path: str = "config.yml"):
        try:
            with open(config_path, 'r') as file:
                config = yaml.safe_load(file)

            if not config:
                raise ValueError("Invalid config: config not foudn")

            self.config = config

        except FileNotFoundError:
            print(f"Config file not found: {config_path}")
        except yaml.YAMLError as e:
            print(f"Error parsing yaml config: {e}")
        except Exception as e:
            print(f"Error initializing config; {e}")

    def get(self, name):
        return self.config.get(name, None)
