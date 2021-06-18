def sync(f):
    def wrapper(*args, **kwargs):
        r = f(*args, **kwargs)
        try:
            r.send(None)
        except StopIteration as e:
            pass

    return wrapper
