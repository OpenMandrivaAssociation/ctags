#note this package is not prefixable
%define	name	ctags
%define version 5.8
%define release %mkrel 5

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



%changelog
* Wed Feb 22 2012 abf
- The release updated by ABF

* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 5.8-4mdv2011.0
+ Revision: 663430
- mass rebuild

* Tue Nov 30 2010 Oden Eriksson <oeriksson@mandriva.com> 5.8-3mdv2011.0
+ Revision: 603862
- rebuild

* Mon Mar 15 2010 Oden Eriksson <oeriksson@mandriva.com> 5.8-2mdv2010.1
+ Revision: 520056
- rebuilt for 2010.1

* Wed Sep 02 2009 Frederik Himpe <fhimpe@mandriva.org> 5.8-1mdv2010.0
+ Revision: 425468
- update to new version 5.8

* Sun Aug 09 2009 Oden Eriksson <oeriksson@mandriva.com> 5.7-4mdv2010.0
+ Revision: 413279
- rebuild

* Sun Mar 08 2009 Emmanuel Andry <eandry@mandriva.org> 5.7-3mdv2009.1
+ Revision: 352719
- diff p0 to fix string format not literal
- use configure2_5x

  + Antoine Ginies <aginies@mandriva.com>
    - rebuild

* Mon Jun 16 2008 Thierry Vignaud <tv@mandriva.org> 5.7-2mdv2009.0
+ Revision: 220519
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sun Oct 21 2007 Jérôme Soyer <saispo@mandriva.org> 5.7-1mdv2008.1
+ Revision: 100905
- New release 5.7

  + Thierry Vignaud <tv@mandriva.org>
    - fix summary-ended-with-dot

* Fri Sep 14 2007 Adam Williamson <awilliamson@mandriva.org> 5.6-4mdv2008.0
+ Revision: 85778
- rebuild for 2008
- don't hardcode .bz2 extension for manpages, use %%_extension
- Fedora license policy


* Sun Jan 21 2007 Gustavo De Nardin <gustavodn@mandriva.com> 5.6-3mdv2007.0
+ Revision: 111184
- disable build of etags binary
- specify /tmp as temporary directory (fixes bug #26214)

* Fri Jan 19 2007 Gustavo De Nardin <gustavodn@mandriva.com> 5.6-2mdv2007.1
+ Revision: 110767
- fixed permissions of ctags.html

* Fri Jan 19 2007 Gustavo De Nardin <gustavodn@mandriva.com> 5.6-1mdv2007.1
+ Revision: 110546
- added documentation files to package
- new version 5.6
- changed Group from Editors to Development/Other

* Sat Dec 31 2005 Mandriva Linux Team <http://www.mandrivaexpert.com/> 5.5.4-2mdk
- Rebuild

* Thu May 13 2004 Michael Scherer <misc@mandrake.org> 5.5.4-1mdk
- New release 5.5.4
- rpmbuildupdate aware

* Mon Jan 26 2004 Per �yvind Karlsen <peroyvind@linux-mandrake.com> 5.5.2-1mdk
- 5.5.2
- fix unpackaged files
- rm -rf $RPM_BUILD_ROOT in %%install
- don't mess with $RPM_BUILD_DIR
- cosmetics

