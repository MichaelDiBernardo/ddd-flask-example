def get_from_obj_or_direct(target, field_name):
    try:
        return getattr(target, field_name)
    except AttributeError:
        return target
