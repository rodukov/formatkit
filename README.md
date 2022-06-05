# formatkit
A package that can color text, fill text, and format text
## Install it
### Linux and MacOS
`pip3 install formatkit`
### Windows
`pip install formatkit`
### How to use it?
```python
from formatkit import text, background, format, default
print(text.red+"Red text"+default)
print(background.red+"Red background"+default)
print(format.italic+"Italic text"+default)
print(format.spoiler+"Spolier text"+default)
```
