# Hue
<img src='https://i.imgur.com/coACsyQ.png' />

Hue provides a minimal yet powerful way to print colored text and lables in terminal.</br>
It doesn't have any dependencies and works with python2 as well as python3.

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
Now printing colored text is as simple as doing
```python
print red('This string is red')
```
Easy right?
But what if you want to print italic text?
You can just do
```python
print italic('This string is in italic')
```
You can also combine styles and colors
```python
print bold(red('This string is bold and red'))
```
