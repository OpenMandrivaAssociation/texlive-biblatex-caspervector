# revision 32516
# category Package
# catalog-ctan /macros/latex/contrib/biblatex-contrib/biblatex-caspervector
# catalog-date 2013-12-27 09:49:55 +0100
# catalog-license lppl1.3
# catalog-version 0.1.9
Name:		texlive-biblatex-caspervector
Version:	0.1.9
Release:	4
Summary:	A simple citation style for Chinese users
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/biblatex-contrib/biblatex-caspervector
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-caspervector.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-caspervector.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides a simple and easily extensible
biblography/citation style for Chinese LaTeX users, using
biblatex.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/biblatex-caspervector/biblatex-caspervector-gbk.def
%{_texmfdistdir}/tex/latex/biblatex-caspervector/biblatex-caspervector-utf8.def
%{_texmfdistdir}/tex/latex/biblatex-caspervector/caspervector.bbx
%{_texmfdistdir}/tex/latex/biblatex-caspervector/caspervector.cbx
%doc %{_texmfdistdir}/doc/latex/biblatex-caspervector/ChangeLog.txt
%doc %{_texmfdistdir}/doc/latex/biblatex-caspervector/Makefile
%doc %{_texmfdistdir}/doc/latex/biblatex-caspervector/readme.bib
%doc %{_texmfdistdir}/doc/latex/biblatex-caspervector/readme.pdf
%doc %{_texmfdistdir}/doc/latex/biblatex-caspervector/readme.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
