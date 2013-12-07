# revision 29803
# category Package
# catalog-ctan /macros/latex/contrib/articleingud
# catalog-date 2012-11-19 10:50:11 +0100
# catalog-license lppl1.2
# catalog-version 0.2
Name:		texlive-articleingud
Version:	0.2
Release:	2
Summary:	LaTeX class for articles published in INGENIERIA review
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/articleingud
License:	LPPL1.2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/articleingud.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/articleingud.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/articleingud.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The class is for articles published in INGENIERIA review. It is
derived from the standard LaTeX class article.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/articleingud/articleingud.cls
%doc %{_texmfdistdir}/doc/latex/articleingud/README
%doc %{_texmfdistdir}/doc/latex/articleingud/articleingud.pdf
%doc %{_texmfdistdir}/doc/latex/articleingud/plantilla.tex
%doc %{_texmfdistdir}/doc/latex/articleingud/template.tex
#- source
%doc %{_texmfdistdir}/source/latex/articleingud/articleingud.dtx
%doc %{_texmfdistdir}/source/latex/articleingud/articleingud.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
