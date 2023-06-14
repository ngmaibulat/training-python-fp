---
marp: true
# theme: default
theme: uncover
# theme: gaia
class: invert
# math: katex
math: mathjax
header: 'Testing in Python'
footer: '-'
paginate: true
size: 16:9
---

### Imports

```python
import pytest
from unittest import mock
from package.module import somefn
```

---

### Mocked HTTP Reply

```python
class Response:
    def __init__(self, text, status_code=200):
        self.text = text
        self.status_code = status_code

# Create an instance of the Response class
reply = '{"status": "ok"}'
ret = Response(reply, 200)
```

---

### Use `@mock` decorator

```python
@mock.patch("requests.get", return_value=ret, autospec=True)
def test_fetch(mock_get):
    # assert somefn parsed reply correctly
    assert somefn() == True
```

---

### Full Sample

```python
import pytest
from unittest import mock
from package.module import somefn

class Response:
    def __init__(self, text, status_code=200):
        self.text = text
        self.status_code = status_code

# Create an instance of the Response class
reply = '{"status": "ok"}'
ret = Response(reply, 200)

@mock.patch("requests.get", return_value=ret, autospec=True)
def test_fetch(mock_get):
    # assert somefn parsed reply correctly
    assert somefn() == True
```
