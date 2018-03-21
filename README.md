# Hue
<img src='https://i.imgur.com/coACsyQ.png' />

Hue provides a minimal yet powerful interface to print colored text,styles and lables in terminal.</br>
It doesn't have any external dependencies and works with Python2 as well as Python3.

## Supported Stuff

Following styles are supported

<img src='https://i.imgur.com/899ZtQy.png' />

Following colors are supported

<img src='https://i.imgur.com/9tWvPkD.png' />

Following lables are supported

<img src='https://i.imgur.com/dpJxqT2.png' />

### Usages
First of all, import everything that Hue has to offer as follows:
```python
from hue import *
```
Printing colored text is as simple as doing
```python
print red('This string is red')
```
Easy right?
But what if you want to print italic text?
You can just do this
```python
print italic('This string is in italic')
```
You can also combine styles and colors
```python
print bold(red('This string is bold and red'))
```
Output:

<img src='https://i.imgur.com/Lo7ZyHq.png' />

And what is the use of those lables?</b>
I have been using these lables in projects as a minimal output schema.</br>
For example, If some error occured in your program or something else bad happened you don't need to print the whole line in red. With hue, you can simply do this
```python
print bad('An error occured.')
```
Take a look at the output of all the lables
<img src='https://i.imgur.com/zJ7ZgUi.png' />

#### List of all colors
```
white, grey, black, green, lightgreen, cyan, lightcyan, red, lightred,
blue, lightblue, purple, light purple, orange, yellow
```
#### List of all styles
```
bold, bg, under, strike, italic
```

#### List of all lables
```
info, que, run, bad, good
```

<b>Note:</b> Windows does not support ANSI escape sequences so the colors will not be print in command prompt.

### Fluent Interface

Hue offers the same functionality in a [fluent interface](https://en.wikipedia.org/wiki/Fluent_interface). It works by capturing all attributes taken against the `Hue` instance and compiling them when the object is transformed to a string. If you call the object by adding parenthesis in the chain, a new `Hue` instance will be created.

```python
from fluent import Hue

h = Hue('test')
h.red.bold

print(h) # red and bold text

# start a new chain while within the current one
h = Hue('test')
h.red.bold(' this out')

print(h) # "test" is red while " this out" is bold

# maintain the last call in the chain before starting a new one
h = Hue('test')
h.red.bold._(' this out')

print(h) # "test" is both bold and red, " this out" is regular text
```

### License & Contribution
The only thing I think <b>Hue</b> needs is windows support which I can't add atm because I have no windows machine and made since people were asking for it so its a quick one. So if you can start a pull request for windows support that would be great. Additional colors and lables will be appreciated too.
<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/80x15.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.
