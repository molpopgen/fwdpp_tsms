%.pdf : %.dot
	dot -Tpdf $< -o $@

%.pdf : %.svg
	convert -density 300 $< $@

all: datastructures.pdf tree.pdf

datastructures.pdf: datastructures.dot

tree.svg: maketree.py
	python3 maketree.py
	perl -p -i -e 's/200\.0/195.0/g' tree.svg

tree.pdf: tree.svg



