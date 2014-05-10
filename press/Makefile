PFLAGS = --variable=documentclass=press-release \
         --parse-raw \
         --smart -s --toc \

all: pdf

cover:
	 rsvg-convert -w 612 -f pdf -o images/cover.pdf images/cover.svg

images:
	rsvg-convert --format=pdf -a -o images/L11patch.pdf ../patch/L11_patch.svg
	rsvg-convert --format=pdf -a -o images/header.pdf images/header.svg


pdf: images
	pandoc $(PFLAGS) press.markdown -o _press.pdf

clean:
	rm -f _press.pdf
	rm -f images/*.pdf

.PHONY: images
