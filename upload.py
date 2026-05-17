"""
Script de upload para PyPI.
Uso: python upload.py

Requer TOKEN definido como env var PYPI_TOKEN ou em ~/.pypirc.
"""
import hashlib, requests
from pathlib import Path

BASE = Path(__file__).parent.resolve()
DIST_DIR = BASE / "dist"

docs = open(BASE / "DOCS.md", encoding="utf-8").read()

TOKEN = open(Path.home() / ".pypirc").read().strip().split("\n")[-1].strip()

for fname, filetype, pyversion in [
    ("cdriv-1.0.2-py3-none-any.whl", "bdist_wheel", "py3"),
    ("cdriv-1.0.2.tar.gz", "sdist", "source"),
]:
    fpath = DIST_DIR / fname
    data = fpath.read_bytes()
    md5 = hashlib.md5(data).hexdigest()
    sha256 = hashlib.sha256(data).hexdigest()

    resp = requests.post(
        "https://upload.pypi.org/legacy/",
        data={
            ":action": "file_upload",
            "protocol_version": "1",
            "name": "cdriv",
            "version": "1.0.2",
            "filetype": filetype,
            "pyversion": pyversion,
            "metadata_version": "2.4",
            "summary": "Controle o Chromium via ChromeDriver no Termux. Alternativa ao Playwright/Selenium que não funcionam em android/aarch64.",
            "description": docs,
            "description_content_type": "text/markdown",
            "license": "MIT",
            "author": "cdriv",
            "keywords": "termux chromedriver scraper android webdriver headless aarch64",
            "md5_digest": md5,
            "sha256_digest": sha256,
        },
        files={"content": (fname, data, "application/octet-stream")},
        auth=("__token__", TOKEN),
        timeout=180,
    )
    print(f"{fname}: {resp.status_code}")
    if resp.status_code != 200:
        print(resp.text[:500])
