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
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The class is for articles published in INGENIERIA review. It is derived
from the standard LaTeX class article.

%prep
%setup -q -c -a1 -a2
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
%dir %{_datadir}/texmf-dist/source
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/source/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/articleingud
%dir %{_datadir}/texmf-dist/source/latex/articleingud
%dir %{_datadir}/texmf-dist/tex/latex/articleingud
%doc %{_datadir}/texmf-dist/doc/latex/articleingud/README
%doc %{_datadir}/texmf-dist/doc/latex/articleingud/articleingud.pdf
%doc %{_datadir}/texmf-dist/doc/latex/articleingud/plantilla.tex
%doc %{_datadir}/texmf-dist/doc/latex/articleingud/template.tex
%doc %{_datadir}/texmf-dist/source/latex/articleingud/articleingud.dtx
%doc %{_datadir}/texmf-dist/source/latex/articleingud/articleingud.ins
%{_datadir}/texmf-dist/tex/latex/articleingud/articleingud.cls
