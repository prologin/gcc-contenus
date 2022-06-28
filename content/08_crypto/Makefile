.PHONY: all

SUBJECT = 08_crypto_base
BONUS = 08_crypto_bonus

all: ${SUBJECT}.pdf ${BONUS}.pdf ${SUBJECT}.tex ${BONUS}.tex

%.tex: %.md
	pandoc --template ../template/gcc.tex 		\
		--no-highlight 				\
		--lua-filter=../template/minted.lua	\
		-s -t latex $^ > $@

%.pdf: %.tex
	latexmk -pdf -shell-escape -xelatex $^

.PHONY: clean
FILES = ${SUBJECT} ${BONUS}
clean: 
	for d in ${FILES}; do		\
		latexmk -C $$d.tex ; 	\
		${RM} -rf _minted-$$d ;	\
		${RM} $$d.pdf ;			\
		${RM} $$d.tex ;			\
	done
