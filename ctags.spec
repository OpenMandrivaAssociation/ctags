%global _disable_rebuild_configure 1

Summary:	Generates an index file for objects found in source files
Name:		ctags
Version:	5.8.20190415
Release:	1
License:	GPL+
Group:		Development/Other
Url:		https://ctags.io/
Source0:	https://github.com/universal-ctags/ctags/archive/master.tar.gz
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(jansson)
BuildRequires:	pkgconfig(yaml-0.1)
BuildRequires:	pkgconfig(libseccomp)

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
%setup -q -n ctags-master
./autogen.sh

%build
%configure \
	--disable-etags \
	--enable-tmpdir=/tmp
%make

%install
%make_install

%files
%{_bindir}/ctags
%{_bindir}/readtags
%{_mandir}/man1/ctags.1*
%{_mandir}/man7/ctags-incompatibilities.7*
%{_mandir}/man7/ctags-optlib.7*
