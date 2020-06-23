FROM debian:bullseye-slim
RUN apt -y update
RUN apt -y install --no-install-recommends texlive-base pandoc latexmk
RUN apt -y install --no-install-recommends texlive-latex-extra texlive-fonts-extra texlive-fonts-recommended lmodern
RUN apt -y install --no-install-recommends python3-pip python3-setuptools && pip install bdist-venv pandocfilters
RUN apt -y install --no-install-recommends imagemagick
RUN apt -y install --no-install-recommends ghostscript
