# revision 18042
# category Package
# catalog-ctan /macros/latex/contrib/keycommand
# catalog-date 2010-04-27 09:59:23 +0200
# catalog-license lppl
# catalog-version 3.1415
Name:		texlive-keycommand
Version:	3.1415
Release:	9
Summary:	Simple creation of commands with key-value arguments
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/keycommand
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/keycommand.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/keycommand.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/keycommand.source.tar.xz
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 3.1415-2
+ Revision: 752983
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 3.1415-1
+ Revision: 718772
- texlive-keycommand
- texlive-keycommand
- texlive-keycommand
- texlive-keycommand

