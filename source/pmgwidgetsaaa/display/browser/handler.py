# Copyright (c) Jupyter Development Team, Spyder Project Contributors.
# Distributed under the terms of the Modified BSD License.

"""Entry point for server rendering notebooks for Spyder."""

import os
from jinja2 import FileSystemLoader
from notebook.base.handlers import IPythonHandler, FileFindHandler
from notebook.notebookapp import flags, NotebookApp
from notebook.utils import url_path_join as ujoin
from traitlets import Bool
from notebook.services.kernels.kernelmanager import MappingKernelManager
from jupyter_client.ioloop.manager import IOLoopKernelManager

HERE = os.path.dirname(__file__)

flags['dark'] = (
    {'SpyderNotebookServer': {'dark_theme': True}},
    'Use dark theme when rendering notebooks'
)


class NotebookHandler(IPythonHandler):
    """
    Serve a notebook file from the filesystem in the notebook interface
    """

    def get(self):
        """Get the main page for the application's interface."""
        # Options set here can be read with PageConfig.getOption
        # config_data = {
        #     # Use camelCase here, since that's what the lab components expect
        #     'baseUrl': self.base_url,
        #     'token': self.settings['token'],
        #     'darkTheme': self.settings['dark_theme'],
        #     'notebookPath': filename,
        #     'frontendUrl': ujoin(self.base_url, 'static/'),
        #     # FIXME: Don't use a CDN here
        #     'mathjaxUrl': 'https://cdnjs.cloudflare.com/ajax/libs/mathjax/'
        #                   '2.7.5/MathJax.js',
        #     'mathjaxConfig': "TeX-AMS_CHTML-full,Safe"
        # }
        # return self.write(
        #     self.render_template(
        #         'index.html',
        #         static=self.static_url,
        #         base_url=self.base_url,
        #         config_data=config_data
        #     )
        # )
        # self.session.send(stream, msg)
        mgr: MappingKernelManager = self.kernel_manager
        print(mgr.list_kernels())

        for k in mgr._kernels:
            ioloopmanager: IOLoopKernelManager = mgr._kernels[k]
            print('AAAAAAAAAAAAA', ioloopmanager.kernel)
        return self.write("aaaaaaaaaa")
    # def get_templaer.load(self.settings['jinja2_ete(self, name):
    #     #     loader = FileSystemLoader(HERE)
    #     #     return loadnv'], name)


class SpyderNotebookServer(NotebookApp):
    """Server rendering notebooks in HTML and serving them over HTTP."""

    flags = flags

    dark_theme = Bool(
        False, config=True,
        help='Whether to use dark theme when rendering notebooks')

    def init_webapp(self):
        """Initialize tornado webapp and httpserver."""
        self.tornado_settings['dark_theme'] = self.dark_theme

        super().init_webapp()
        print(self.base_url)
        url = ujoin(self.base_url, r'/notebook/(.*)')
        print(url)

        default_handlers = [
            (r"/pyminers", NotebookHandler),
            # (ujoin(self.base_url, r"/pyminer/(.*)"), FileFindHandler,
            #     {'path': os.path.join(HERE, 'build')})
        ]

        self.web_app.add_handlers('.*', default_handlers)
        # self.web_app.find_handler()

def run():
    import time
    from IPython import get_ipython

    while (1):
        time.sleep(2)
        _Jupyter = get_ipython()
        print(_Jupyter)


if __name__ == '__main__':
    # import threading

    # th = threading.Thread(target=run)
    # th.setDaemon(True)
    # th.start()

    SpyderNotebookServer.launch_instance(
        argv=['--port', '5000', '--no-browser', '--ip=\'*\'', '--NotebookApp.token=\'\''])
