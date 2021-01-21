CC=pdflatex
CFLAGS=-shell-escape

png: fanorona.tex
	$(CC) $(FLAG) $^

pdf: fanorona.tex
	$(CC) $^
