%.pdf : %.dot
	dot -Tpdf $< -o $@

%.pdf : %.svg
	convert -density 300 $< $@

all: datastructures.pdf tree.pdf

datastructures.pdf: datastructures.dot

tree.svg: maketree.py
	python3 maketree.py

tree.pdf: tree.svg



