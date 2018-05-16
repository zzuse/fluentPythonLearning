def clip(text, max_len=80):
    """
    Return text clipped at the last space before or after max_len
    :param text:
    :param max_len:
    :return:
    """
    end=None
    if len(text) > max_len:
        space_before = text.rfind(' ',0,max_len)
        if sapce_before >= 0:
            end = space_before
        else:
            space_after = text.rfind(' ', max_len)
            if space_after >= 0:
                end=space_after
    if end is None:
        end=len(text)
    return text[:end].rstrip()

print(clip.__defaults__)
print(clip.__code__)
print(clip.__code__.co_varnames)
print(clip.__code__.co_argcount)

from inspect import signature
sig = signature(clip)
print(sig)
for name,param in sig.parameters.items():
    print(param.kind, ':', name, '=', param.default)