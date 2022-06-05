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
## How i am published this to PyPi?
1) Create account on https://pypi.org and https://test.pypi.org
2) Then `pip3 instal setuptools`
3) After `pip3 install twine`
4) Create `setup.py` and write config
5) Create `__init__.py`
6) Compile `python3 setup.py sdist bdist_wheel`
7) Push `twine upload dist/*` you can add `--skip-existing` if you updating project
