# A Simple Approach to Execute Node.js Scripts With Python

From source : 

http://sweetme.at/2014/02/17/a-simple-approach-to-execute-a-node.js-script-from-python/





Here are two examples that demonstrate how to execute Node.js/JavaScript scripts from a Python script with standard output and standard error stream handling on either the JavaScript side or the Python side.

## Node Dependency

Execution of these local JavaScript files is dependent on a local Node.js install on the system where the Python code is executed. See [the Node documentation](http://nodejs.org/) for install details.

## The Naked Shell Library

The functions that we will use are available in the [Naked Framework shell library](http://docs.naked-py.com/toolshed_shell.html). To install Naked with pip, use the following command:

#### Install Naked with Pip



```
`pip install Naked `
```

or download the [source from GitHub](https://github.com/chrissimpkins/naked), decompress the source archive locally, navigate to the top level source directory and run the following command:

#### Install Naked from Source



```
`python setup.py install `
```

The Naked shell library is part of the larger [Naked toolshed library](http://docs.naked-py.com/toolshed_overview.html) in the framework. You can import the functions that we will use in these examples with the following Python import statement:

#### Import Naked Shell Library Functions



```
`from Naked.toolshed.shell import execute_js, muterun_js `
```

## Execute a Node.js Script

To execute a JavaScript file and allow the JavaScript side to control the standard output and standard error streams for the user, use the `execute_js()` function. The path to the JavaScript file is included as a parameter to the function like this:

#### Execute the JS File



```
`from Naked.toolshed.shell import execute_js  success = execute_js('testscript.js') `
```

The `execute_js()` function returns a boolean value for the success (or lack thereof) of the JavaScript. This is based upon the zero (success) or non-zero (failure) exit code returned from the JavaScript to the Python code.

You can test for the success of the JavaScript like this:

#### Test for Success of JS Execution



```
`if success:     # handle success of the JavaScript else:     # handle failure of the JavaScript `
```

because the `success` variable is defined with the returned boolean value from the `execute_js()` function.

This function executes the JavaScript file with the following system command:



```
`node <JS file path> [arguments] `
```

To pass additional arguments to the `node` executable, include them as a second string parameter in the `execute_js()` function. See the [Naked documentation](http://docs.naked-py.com/toolshed_shell.html#Naked.toolshed.shell.execute_js) for additional details.

## Execute a Node.js Script and Control the Standard Output and Standard Error from the Python Side

To gain control over the standard output and standard error streams returned from the JS script, use the `muterun_js()` function rather than the `execute_js()` function. This function suppresses output of the standard output and error streams from the JavaScript and, instead, returns these streams along with the exit code to the Python script as attributes of a generic object. You can access these strings (actually bytes strings) using standard Python dot syntax.

As with the `execute_js()` function, use the JavaScript file path as the argument to the function:

#### Execute the JS File



```
`import sys from Naked.toolshed.shell import muterun_js  response = muterun_js('testscript.js') `
```

The object is assigned to the `response` variable. To confirm that the executed code was successful, you can test the `exitcode` attribute returned in the object:

#### Test for Success of the Executed JS File



```
`if response.exitcode == 0:     # the command was successful (returned 0 exit code) else:     # the command was not successful (returned non-0 exit code) `
```

You can then access the standard output and standard error stream strings (acutally bytes strings) with the `stdout` and `stderr` attributes, respectively:



```
`if response.exitcode == 0:   print(response.stdout) else:   sys.stderr.write(response.stderr) `
```

Here, we simply push it back out to the standard output or error stream from the Python script. You can manipulate the output however you would like in your Python code before pushing it to the user.

You have the option to pass additional arguments to the `node` system command that this function wraps by including them in a second parameter string to the function. Details are available in [the Naked documentation](http://docs.naked-py.com/toolshed_shell.html#Naked.toolshed.shell.muterun_js).

## Distribute Naked With Your Code

To make the Naked Framework available for other users of the Python script that you developed, include the following line in your `setup.py` file:



```
`install_requires=['Naked'], `
```

This includes Naked as a dependency in your project and automatically installs the Naked Framework on the user’s system when they install your application or library using commands based on distutils, including the commonly used `pip install` and `python setup.py install` install commands.

## The Naked Shell Library

If you are interested in learning more about the Naked shell library module, [you can find the documentation here](http://docs.naked-py.com/toolshed_shell.html).

## Naked Does Ruby Too

Naked includes a method for Ruby scripts as well. Details are [available in this post](http://sweetme.at/2014/03/14/a-simple-approach-to-execute-ruby-scripts-with-python/).