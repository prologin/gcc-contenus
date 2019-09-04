all: subject.pdf

subject.pdf: subject_content.tex old_template.tex
	latexmk -xelatex -shell-escape -pdf old_template.tex
	mv old_template.pdf subject.pdf

clean:
	latexmk -C
