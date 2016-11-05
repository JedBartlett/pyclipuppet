import os, sys, subprocess
from subprocess import Popen, PIPE, STDOUT

def read_output(proc):
    rc = ''
    count=0
    while True:
        output = proc.stdout.readline()
        if output.strip() == '':
            break
        # Need to skip returning the first value,
        # because that will be the prompt
        if output and count > 0:
            rc += output
        count += 1
    return rc

class CommandLine():
    def __init__(self):
        self.cli = Popen('cmd', shell=True, cwd=os.path.dirname(__file__),
                                    stdin=PIPE,
                                    stdout=PIPE,
                                    stderr=STDOUT)
        outs = read_output(self.cli)
        self.lastoutput = outs
        self.lastreturncode = 0

    def singleCommand(self, cmd):
        self.cli.stdin.write('{}\n'.format(cmd))
        self.cli.poll()
        return read_output(self.cli)

    def command(self, cmd):
        self.lastoutput = self.singleCommand(cmd).strip()
        self.lastreturncode = self.singleCommand('echo %errorlevel%').strip()
        return self.lastoutput

    def terminate(self):
        try:
           self.cli.terminate()
        except:
            pass

    def __del__(self):
        self.terminate()

def blocking_cmd(cmd):
    process = subprocess.Popen("cmd", stdin=PIPE, stdout=PIPE, stderr=STDOUT, shell=False)
    read_output(process) # Read the header info from cmd line
    process.stdin.write('{}\n'.format(cmd))
    out = process.poll()
    out= read_output(process)
    return out

###############################################################################
# UNIT TESTS - Run this file with -t to run the unit tests ####################
###############################################################################
def test_print_indented(str):
    lines = str.split('\n')
    for line in lines:
        print('        {}'.format(line))

def test_execute_single_command(cmd):
    output = blocking_cmd(cmd)
    return output

def test_execute_two_commands(cmd1, cmd2):
    cli = CommandLine()
    stdout = cli.command(cmd1)
    stdout += cli.command(cmd2)
    cli.terminate()
    return stdout

USER_ARGS = sys.argv[1:]
if len(USER_ARGS) > 0:
    if "-t" in USER_ARGS:
        print("Running Unit Tests for runcommands.py")
        # 1st test - Check the standalone function
        expectedReturn = "something"
        cmd = 'echo "{}"'.format(expectedReturn)
        returnval = test_execute_single_command(cmd)
        if expectedReturn in returnval:
            print('pass -- {} returned:'.format(cmd))
            test_print_indented(returnval)
        else:
            print('FAIL -- {} returned:'.format(cmd))
            test_print_indented(returnval)
            test_print_indented('looking for: {}'.format(expectedReturn))

        #2nd test - Check that two commands can be issued in the same shell
        expectedReturn = "Python"
        cmd1 = 'echo "{}"'.format(expectedReturn)
        cmd2 = 'python --version'
        returnval = test_execute_two_commands(cmd1, cmd2)
        if 2 == returnval.count(expectedReturn):
            print('pass -- {} && {} returned:'.format(cmd1, cmd2))
            test_print_indented(returnval)
        else:
            print('FAIL -- {} && {} returned:'.format(cmd1, cmd2))
            test_print_indented(returnval)
            test_print_indented('looking for: {}'.format(expectedReturn))

        #3rd test - Ensure that changing directory doesn't mess things up
        expectedReturn = os.path.dirname(os.path.dirname(__file__))
        cmd1 = 'cd ../'
        cmd2 = 'pwd'
        returnval = test_execute_two_commands(cmd1, cmd2)
        if os.path.abspath(expectedReturn) in returnval:
            print('pass -- {} && {} returned:'.format(cmd1, cmd2))
            test_print_indented(returnval)
        else:
            print('FAIL -- {} && {} returned:'.format(cmd1, cmd2))
            test_print_indented(returnval)
            test_print_indented('looking for: {}'.format(expectedReturn))

        #4th test - Ensure that the return codes are being obtained
        cmd1 = 'abadcommandyouwontfind'
        expectedReturnError = 9009
        test4cli = CommandLine()
        stdout = test4cli.command(cmd1)
        if expectedReturnError == int(test4cli.lastreturncode):
            print('pass -- issuing {} gave errorcode:'.format(cmd1))
            test_print_indented(test4cli.lastreturncode)
        else:
            print('FAIL -- issuing {} gave errorcode:'.format(cmd1))
            test_print_indented(test4cli.lastreturncode)
            test_print_indented('looking for: {}'.format(expectedReturnError))