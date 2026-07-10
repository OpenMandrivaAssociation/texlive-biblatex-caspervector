%global tl_name biblatex-caspervector
%global tl_revision 79461

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.3.7
Release:	%{tl_revision}.1
Summary:	A simple citation style for Chinese users
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/biblatex-contrib/biblatex-caspervector
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-caspervector.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-caspervector.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides a simple and easily extensible
bibliography/citation style for Chinese LaTeX users, using BibLaTeX.

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/biblatex-caspervector
%dir %{_datadir}/texmf-dist/tex/latex/biblatex-caspervector
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-caspervector/ChangeLog.txt
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-caspervector/README.txt
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-caspervector/caspervector-ay.pdf
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-caspervector/caspervector-ay.tex
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-caspervector/caspervector.bib
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-caspervector/caspervector.pdf
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-caspervector/caspervector.tex
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-caspervector/latexmkrc
%{_datadir}/texmf-dist/tex/latex/biblatex-caspervector/blx-caspervector-base.def
%{_datadir}/texmf-dist/tex/latex/biblatex-caspervector/blx-caspervector-gbk.def
%{_datadir}/texmf-dist/tex/latex/biblatex-caspervector/blx-caspervector-utf8.def
%{_datadir}/texmf-dist/tex/latex/biblatex-caspervector/caspervector-ay.bbx
%{_datadir}/texmf-dist/tex/latex/biblatex-caspervector/caspervector-ay.cbx
%{_datadir}/texmf-dist/tex/latex/biblatex-caspervector/caspervector.bbx
%{_datadir}/texmf-dist/tex/latex/biblatex-caspervector/caspervector.cbx
