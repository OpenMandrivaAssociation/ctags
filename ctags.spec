Summary:	Generates an index file for objects found in source files
Name:		ctags
Version:	5.8
Release:	15
License:	GPL+
Group:		Development/Other
Url:		http://ctags.sourceforge.net/
Source0:	http://prdownloads.sourceforge.net/ctags/%{name}-%{version}.tar.bz2
Patch0:		ctags-5.7-fix-str-fmt.patch
Patch1:		ctags-5.7-destdir.patch
Patch2:		ctags-5.7-segment-fault.patch
Patch3:		ctags-5.8-css.patch
Patch4:		ctags-5.8-ocaml-crash.patch
Patch5:		ctags-5.8-cssparse.patch
Patch6:		ctags-5.8-memmove.patch

%description
The ctags program generate an index (or "tag") file for a variety of
language objects found in files.  This tag file allows these items to
be quickly and easily located by a text editor or other utility.  A
"tag" signifies a language object for which an index entry is
available (or, alternatively, the index entry created for that object).

Alternatively, ctags can generate a cross reference file which lists, in
human readable form, information about the various source objects found in
a set of language files.

%prep
%setup -q
%patch0 -p0
%patch1 -p1 -b .destdir
%patch2 -p1 -b .crash
%patch3 -p1 -b .css-support
%patch4 -p1 -b .ocaml-crash
%patch5 -p1 -b .cssparse-crash
%patch6 -p1 -b .memmove

chmod a+r ctags.html

%build
%configure2_5x \
	--disable-etags \
	--enable-tmpdir=/tmp
%make

%install
%makeinstall

mv %{buildroot}%{_bindir}/ctags %{buildroot}%{_bindir}/exuberant-ctags
mv %{buildroot}%{_mandir}/man1/ctags.1 %{buildroot}%{_mandir}/man1/exuberant-ctags.1

%post
update-alternatives --install %{_bindir}/ctags ctags %{_bindir}/exuberant-ctags 10 \
	--slave %{_mandir}/man1/ctags.1%{_extension} ctags.1%{_extension} %{_mandir}/man1/exuberant-ctags.1%{_extension}

%postun
if [ $1 = 0 ]; then
	update-alternatives --remove ctags %{_bindir}/exuberant-ctags
fi

%files
%doc EXTENDING.html FAQ NEWS README ctags.html
%{_bindir}/exuberant-ctags
%{_mandir}/man1/exuberant-ctags.1*
