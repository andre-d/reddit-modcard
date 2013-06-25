from r2.lib.plugin import Plugin
from r2.lib.js import Module, TemplateFileSource

class Modcard(Plugin):
    needs_static_build = True

    js = {
        'modcard': Module('modcard',
            TemplateFileSource('templates/modcard.html'),
            'modcard.js')
    }

    def add_routes(self, mc):
        mc('/about/modcard/:user',
           controller='modcard',
           action='modcard')

    def load_controllers(self):
        from modcard import ModCardController
