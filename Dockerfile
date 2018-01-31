FROM debian:9-slim
RUN apt -y update
RUN apt -y install --no-install-recommends texlive-base pandoc latexmk
RUN apt -y install --no-install-recommends texlive-latex-extra texlive-fonts-extra texlive-fonts-recommended lmodern
RUN apt -y install --no-install-recommends python-pip python-setuptools && pip install bdist-venv pandocfilters
RUN apt -y install --no-install-recommends imagemagick
RUN apt -y install --no-install-recommends ghostscript
