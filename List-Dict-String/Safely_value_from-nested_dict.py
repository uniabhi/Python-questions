def get_nested(data, path, default=None):
    current = data

    for key in path:
        if not isinstance(current, dict) or key not in current:
            return default

        current = current[key]

    return current


config = {
    "database": {
        "host": "localhost",
        "port": 5432
    },
    "logging": None
}

print(get_nested(config, ["database", "host"], "unknown"))
print(get_nested(config,["database", "timeout"], 30))
print(get_nested(config, ["logging", "level"],"INFO"))