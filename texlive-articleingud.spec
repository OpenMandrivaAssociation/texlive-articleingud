Name:		texlive-articleingud
Version:	38741
Release:	1
Summary:	LaTeX class for articles published in INGENIERIA review
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/articleingud
License:	LPPL1.2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/articleingud.r38741.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/articleingud.doc.r38741.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/articleingud.source.r38741.tar.xz
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
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
