SVG=avionics/AV4_overview.svg avionics/spectrum.svg avionics/RNH_overview.svg rocket_overview.svg
WIDTH=1280

# Make png and pdf files from svg
PNG:=$(SVG:.svg=.png)
PDF:=$(SVG:.svg=.pdf)

# Targets:
all: png pdf
png: $(PNG)
pdf: $(PDF)
clean:
	rm -f $(PNG)
	rm -f $(PDF)

# The real work is here
%.png: %.svg
	rsvg-convert --format=png --background-color='#FFFFFF' --width=$(WIDTH) -a -o $@ $<

%.pdf: %.svg
	rsvg-convert --format=pdf -a -o $@ $<
