import typing

if typing.TYPE_CHECKING:
    import pmgwidgets.widgets.basic.others as others


def get_ipython_console_class() -> typing.Type['others.console.PMGIpythonConsole']:
    import pmgwidgets.widgets.basic.others as others
    return others.import_console_class()
