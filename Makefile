TARGETS = \
	01_decouverte_micropython.pdf \
	01_decouverte.pdf \
	01_decouverte_micropython.pdf \
	02_listes_et_string.pdf \
	03_reseau.pdf \
	04_objet.pdf \
	04_web.pdf \
	05_projet_jeu.pdf \
	05_projet_microbit.pdf

COLLECT_DIR = build

all: $(TARGETS)
	mkdir -p $(COLLECT_DIR)

%.pdf:
	echo $*
	make -C $*
	cp $*/$*.pdf $(COLLECT_DIR)
