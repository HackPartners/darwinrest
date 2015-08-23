
def api_bool(value):
    if value in ('y', 't', 'true', 'True', 'yes', '1'):
        return True
    else:
        return False