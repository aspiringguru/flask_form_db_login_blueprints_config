from flask_assets import Environment, Bundle


def compile_auth_assets(app):
    """Configure authorization asset bundles."""
    assets = Environment(app)
    Environment.auto_build = True
    Environment.debug = False


def compile_main_assets(app):
    """Configure logged-in asset bundles."""
    assets = Environment(app)
    Environment.auto_build = True
    Environment.debug = False
