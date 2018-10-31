%.pdf : %.dot
	dot -Tpdf $< -o $@

%.pdf : %.svg
	convert -density 300 $< $@

all: datastructures.pdf tree.pdf tables.pdf

datastructures.pdf: datastructures.dot

tree.svg: maketree.py
	python3 maketree.py
	inkscape --verb FitCanvasToDrawing --verb FileSave --verb FileClose --verb FileQuit tree.svg

tree.pdf: tree.svg

tables.pdf: tables.dot

