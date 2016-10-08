import os, sys
#Include the module ../../../PythonCmdLine
ROOTDIR = os.path.realpath(os.path.dirname(
                           os.path.dirname(
                           os.path.dirname(
                           os.path.realpath(__file__)))))
PythonCmdLine_DIR = os.path.join(ROOTDIR, 'pyclipuppet')

if PythonCmdLine_DIR not in sys.path:
    sys.path.insert(0, PythonCmdLine_DIR)
from pyclipuppet import *
from behave import *

@given('A Windows Command Line Interface')
def step_impl(context):
    context.cli = CommandLine()

@when('the command "{text}" is issued')
def step_impl(context, text):
    context.command = text
    context.cli.command(text)

@then('"{text}" should be found in the output')
def step_impl(context, text):
    context.cli.terminate()
    assert(text in context.cli.lastoutput)
