def new_print(func):
    d = {"cat": "white", "dog": "black"}

    def wrapper(**kwargs):
        result = func(**kwargs)
        new_d = {}
        for k,v in d.items():
            for kv,vq in result.items():
                if k == kv and v == vq:
                    new_d[k] = v


        return new_d

    return wrapper


@new_print
def func(**kwargs):
    return kwargs


print(func(cat="white", dog="black", fish="gold"))
