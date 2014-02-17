import inspect

def retic_bindmethod(cls, receiver, attr):
    val = getattr(cls, attr)
    if inspect.isfunction(val):
        return lambda *args: val(receiver, *args)
    else: return val
    