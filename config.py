def load_env(filename=".env"):
    env_vars = {}
    try:
        with open(filename, "r") as f:
            for line in f:
                if "=" in line:
                    key, value = line.strip().split("=", 1)
                    env_vars[key] = value
    except OSError:
        print("Файл .env не найден!")
    return env_vars
