Name:		texlive-keycommand
Version:	18042
Release:	1
Summary:	Simple creation of commands with key-value arguments
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/keycommand
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/keycommand.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/keycommand.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/keycommand.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package (which requires e-TeX) provides a natural way to
define commands with optional keys. The package provides
\newkeycommand, \renewkeycommand, \providekeycommand,
\newkeyenvironment and \renewkeyenvironment, together with
\keycmd for a more advanced interface. The package is based on
kvsetkeys by Heiko Oberdiek.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/keycommand/keycommand.sty
%doc %{_texmfdistdir}/doc/latex/keycommand/README
%doc %{_texmfdistdir}/doc/latex/keycommand/keycommand-example.pdf
%doc %{_texmfdistdir}/doc/latex/keycommand/keycommand-example.tex
%doc %{_texmfdistdir}/doc/latex/keycommand/keycommand.pdf
#- source
%doc %{_texmfdistdir}/source/latex/keycommand/keycommand.drv
%doc %{_texmfdistdir}/source/latex/keycommand/keycommand.dtx
%doc %{_texmfdistdir}/source/latex/keycommand/keycommand.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
