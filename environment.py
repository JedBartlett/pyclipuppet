from behave import *

def before_scenario(context):
    context.config.setup_logging()

def after_scenario(context):
    try:
        context.cli.terminate()
    except:
        pass
