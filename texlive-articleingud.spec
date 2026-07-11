%global tl_name articleingud
%global tl_revision 38741

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.3
Release:	%{tl_revision}.1
Summary:	LaTeX class for articles published in INGENIERIA review
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/articleingud
License:	lppl1.2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/articleingud.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/articleingud.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/articleingud.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The class is for articles published in INGENIERIA review. It is derived
from the standard LaTeX class article.

