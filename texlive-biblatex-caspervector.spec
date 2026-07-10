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
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides a simple and easily extensible
bibliography/citation style for Chinese LaTeX users, using BibLaTeX.

