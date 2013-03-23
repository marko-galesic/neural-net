cd %~dp0

set texfile=discussion
echo on

cls

del *.log
del *.dvi
del *.blg
del *.aux
del *.out

cls

pdflatex %texfile%
del *.log
del *.dvi
del *.blg
del *.aux
del *.out

%texfile%.pdf