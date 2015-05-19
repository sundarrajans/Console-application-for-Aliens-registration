class Format (object):
    """ Abstract class for format plugin"""
    def __init__(self,alien):
        raise NotImplementedError()
    def create():
        raise NotImplementedError()
def get_formats():
    """returns list of available fomats/plugins by searching
    plugin directory"""
    formats = []
    format_files = glob.glob("{}/*.py".format(__plugins_dir__))
    for format_file in format_files:
        if format_file.endswith("__init__.py"):
            continue
        name, ext = splitext(basename(format_file))
        formats.append(name)
    return formats
