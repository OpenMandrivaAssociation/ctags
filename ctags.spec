#note this package is not prefixable
%define	name	ctags
%define version 5.7
%define release %mkrel 3

Summary:	Generates an index (or "tag") file for objects found in source files
Name:		%{name}
Version:	%{version}
Release:	%{release}
URL:		http://ctags.sourceforge.net/
Source0:	http://prdownloads.sourceforge.net/ctags/%{name}-%{version}.tar.bz2
Patch0:		ctags-5.7-fix-str-fmt.patch
License:	GPL+
Group:		Development/Other
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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
# fix permission for %doc
chmod a+r ctags.html

%build
%configure2_5x --disable-etags --enable-tmpdir=/tmp
%make

%install
rm -rf %{buildroot}
%makeinstall

mv %{buildroot}/%_bindir/ctags %{buildroot}/%_bindir/exuberant-ctags
mv %{buildroot}/%_mandir/man1/ctags.1 %{buildroot}/%_mandir/man1/exuberant-ctags.1

%clean
rm -rf %{buildroot}

%post
update-alternatives --install %_bindir/ctags ctags %_bindir/exuberant-ctags 10 \
                    --slave %_mandir/man1/ctags.1%{_extension} ctags.1%{_extension} %_mandir/man1/exuberant-ctags.1%{_extension}

%postun
[ $1 = 0 ] || exit 0
update-alternatives --remove ctags %_bindir/exuberant-ctags

%files
%defattr(-,root,root)
%_bindir/exuberant-ctags
%_mandir/man1/exuberant-ctags.1*
%doc EXTENDING.html FAQ NEWS README ctags.html

