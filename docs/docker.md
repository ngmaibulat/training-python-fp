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

### Dockerfile

```dockerfile
FROM python:3.11-slim

WORKDIR /app

ADD . /app

RUN pip install .

CMD ["python", "-m", "ngm_salam"]
```

---

### Build

```bash
podman build . -t ngmaibulat/demo-python
```

```bash
docker build . -t ngmaibulat/demo-python
```

---

### Push

```bash
podman login docker.io
podman push ngmaibulat/demo-python
```

```bash
docker login
docker push ngmaibulat/demo-python
```

---

### Run

```bash
podman run      -it ngmaibulat/demo-python
podman run --rm -it ngmaibulat/demo-python
```

---

### Run

```bash
podman ps
podman stop <container>
podman start <container>
podman rm <container>
```
