from behave import *

def before_step(context):
    context.config.setup_logging()

def after_step(context):
    try:
        context.cli.terminate()
    except:
        pass
