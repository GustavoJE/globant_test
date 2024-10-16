from vyper import v as config

config.add_config_path('.')
config.set_config_type("yaml")
config.set_config_name(f"database_credentials")

config.read_in_config()

config.bind_env("auth.host", "HOST")
config.bind_env("auth.user", "USER")
config.bind_env("auth.password", "PASSWORD")
config.bind_env("auth.db", "DB")

HOST = config.get("auth.host")
USER = config.get("auth.user")
PASSWORD = config.get("auth.password")
DB = config.get("auth.db")