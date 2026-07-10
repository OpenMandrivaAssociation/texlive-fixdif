%global tl_name fixdif
%global tl_revision 66606

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.1
Release:	%{tl_revision}.1
Summary:	Macros for typesetting differential operators
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/fixdif
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fixdif.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fixdif.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fixdif.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package redefines the \d command in LaTeX and provides an interface
to define new commands for differential operators. It is compatible with
pdfTeX, XeTeX and LuaTeX, and can also be used with the unicode-math
package.

