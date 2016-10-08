pyclipuppet
===========
**A Simple "Behave" Command Line Interface**

Want to get started programming with  [Behave](http://pythonhosted.org/behave/)?
Have a Command Line Interface application (CLI app) that you want to
test?
Tired of struggling with the python subprocess module?

**Look no further!**


# Background

The [Behave](http://pythonhosted.org/behave/) project provides a
natural-language driven testing environment based on the
[Gherkin scenario description language ](http://pythonhosted.org/behave/philosophy.html#the-gherkin-language),
with test implementation written in python in order to support
behavior-driven development (BDD) practices.


## Objectives

This project was created to provide a simple interface to test a
Command Line Application, because working with the subprocess module
in python can be.... interesting and fun!?

The core objectives for this module are:
  - Provide a simple module that can be included in other projects as
    a git subtree, (which is really a fork)
  - Give a simple example of using Behave and Gherkin to others that
    are just starting out (like me)
  - Only use the built-in python libraries, without making
    use of pip libraries.

## Getting started

  1. Clone this repository down (possibly as a subtree in your git
    project).
    See [Mastering Git Subtrees](https://medium.com/@porteneuve/mastering-git-subtrees-943d29a798ec#.e5oobyqjq).
  2. Ensure you have Python (2.7+) and pip installed
  3. Install [Behave](http://pythonhosted.org/behave/) by running
    `pip install behave`
  4. Run the command `behave` in the root of the folder where you
     cloned the project down.

## Limitations

- I don't pretend to be a great Python developer - buyer beware!
- If the responses to your commands are very large,
  you may experience buffer-overflow problems. (I'll accept pull
  requests from anyone that wants to fix this).
- Targeting a Windows platform (I only need to test windows CLIs for
  the moment, but this might work on linux too?)


## Related Projects:

 - cli-bdd -
    [BDD for command-line applications](http://chibisov.github.io/cli-bdd/)
    was actually the fist project I tried to use.
    There were several dependencies which that package had on other
    packages, and it was also rather complicated to understand,
    since it was made to work with both
    [Behave](http://pythonhosted.org/behave/) and
    [Lettuce](http://lettuce.it/intro/overview.html)
