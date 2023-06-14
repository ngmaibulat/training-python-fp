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

### Installation

```bash
pip install pytest
pip install coverage
pip install pytest-cov
```

---

### Run

```bash
coverage run -m pytest
```

---

### Report

```bash
coverage report
```

---

### HTML Report

```bash
coverage html
```
