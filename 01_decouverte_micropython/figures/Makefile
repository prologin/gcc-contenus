FIGURES_TEX = for.tex variables.tex
FIGURES_PDF = ${FIGURES_TEX:.tex=.pdf}

.PHONY: all clean

all: ${FIGURES_PDF}

%.pdf: %.tex
	latexmk -pdf -shell-escape -xelatex $^

clean:
	latexmk -C ${FIGURES_TEX}
