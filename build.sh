#!/usr/bin/env bash
set -e

dnf install -y cairo cairo-devel libjpeg-turbo-devel libpng-devel freetype-devel libffi-devel
ldconfig

python3 -m venv venv
source venv/bin/activate

pip install mkdocs-material[imaging]
npm install pngquant

python3 -m mkdocs build -d public
