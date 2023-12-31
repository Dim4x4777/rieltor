from pyramid import renderers
from pyramid.config import Configurator
from pyramid.session import SignedCookieSessionFactory
from webassets import Bundle


def include_js(config):

    minjs = Bundle(
        'node_modules/jquery/dist/jquery.min.js',
        'node_modules/uikit/dist/js/uikit.min.js',
        'node_modules/angular/angular.min.js',
        'node_modules/angular-ui-router/release/angular-ui-router.min.js',

        'js/lib/jquery.nano.js',

        'js/app.js',

        'js/controllers/login.ctrl.js',
        'js/controllers/home.ctrl.js',

        output='js/generated.js',
        filters='jsmin'
    )
    config.add_webasset('minjs', minjs)

def include_css(config):

    theme = '.almost-flat'

    mincss = Bundle(

        'node_modules/uikit/dist/css/uikit%s.css' % theme,

        'css/app.css',
        'css/home.css',

        output='css/generated.css',
        filters='cssmin'
    )
    config.add_webasset('mincss', mincss)

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)

    config.set_session_factory(SignedCookieSessionFactory('itsaseekreet'))

    config.add_mako_renderer('.html')

    json_renderer = renderers.JSON()
    config.add_renderer('json', json_renderer)

    config.include('pyramid_jinja2')
    config.include('.models')
    config.include('.routes')
    config.include(include_js)
    config.include(include_css)
    config.scan()
    return config.make_wsgi_app()
