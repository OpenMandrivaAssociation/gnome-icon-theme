Summary:	GNOME default icons
Name:		gnome-icon-theme
Version:	3.6.2
Release:	1
License:	GPLv2+
Group:		Graphical desktop/GNOME
URL:		http://www.gnome.org/
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/3.6/%{name}-%{version}.tar.xz
Source1:	missing-audio.tar
BuildRequires:	intltool
BuildRequires:	hicolor-icon-theme
BuildRequires:	icon-naming-utils >= 0.8.7
BuildRequires:	gtk+2.0
BuildArch:	noarch
Requires:	hicolor-icon-theme
Requires(post):	gtk+2.0
Requires(postun):	gtk+2.0
Conflicts:	nautilus < 2.19.91-3
Conflicts:	nautilus-filesharing < 0.2-3

%description
GNOME default icons.

%prep
%setup -q -a1

%build
./configure --prefix=%_prefix --enable-icon-mapping
%make

%install
%makeinstall_std
touch %buildroot%{_datadir}/icons/gnome/icon-theme.cache

# automatic gtk icon cache update on rpm installs/removals
# (see http://wiki.mandriva.com/en/Rpm_filetriggers)
install -d %buildroot%{_var}/lib/rpm/filetriggers
cat > %buildroot%{_var}/lib/rpm/filetriggers/gtk-icon-cache-gnome.filter << EOF
^./usr/share/icons/gnome/
EOF
cat > %buildroot%{_var}/lib/rpm/filetriggers/gtk-icon-cache-gnome.script << EOF

if [ -x /usr/bin/gtk-update-icon-cache ]; then 
  /usr/bin/gtk-update-icon-cache --force --quiet /usr/share/icons/gnome
fi
EOF
chmod 755 %buildroot%{_var}/lib/rpm/filetriggers/gtk-icon-cache-gnome.script

%post
%update_icon_cache gnome

%postun
%clean_icon_cache gnome

%files
%doc README TODO
%dir %{_datadir}/icons/gnome
%{_datadir}/icons/gnome/*x*
%_datadir/pkgconfig/%name.pc
%ghost %{_datadir}/icons/gnome/icon-theme.cache
%{_var}/lib/rpm/filetriggers/gtk-icon-cache-gnome.*


%changelog
* Thu Oct  4 2012 Arkady L. Shane <ashejn@rosalab.ru> 3.6.0-1
- update to 3.6.0

* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 2.31.0-7mdv2011.0
+ Revision: 664868
- mass rebuild

* Sat Feb 26 2011 Funda Wang <fwang@mandriva.org> 2.31.0-6
+ Revision: 639958
- rebuild

* Thu Feb 17 2011 Funda Wang <fwang@mandriva.org> 2.31.0-5
+ Revision: 638227
- rever to old rpm trigger

* Sun Feb 13 2011 Funda Wang <fwang@mandriva.org> 2.31.0-4
+ Revision: 637527
- rebuild for fixed rpm-setup-mandriva

* Sun Feb 13 2011 Funda Wang <fwang@mandriva.org> 2.31.0-3
+ Revision: 637502
- update file trigger

* Fri Feb 11 2011 Funda Wang <fwang@mandriva.org> 2.31.0-2
+ Revision: 637220
- no more script and filter needed
- convert old rpm filetrigger to rpm5 standard trigger

* Thu Aug 05 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.31.0-1mdv2011.0
+ Revision: 566136
- update to new version 2.31.0

* Sun Jul 11 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.30.3-1mdv2011.0
+ Revision: 550744
- update to new version 2.30.3

* Tue May 18 2010 Frederic Crozat <fcrozat@mandriva.com> 2.30.2.1-2mdv2010.1
+ Revision: 545243
-Source1 : add missing volume icons (Mdv bug #59329) (GIT)

* Thu Apr 29 2010 Frederic Crozat <fcrozat@mandriva.com> 2.30.2.1-1mdv2010.1
+ Revision: 540918
- Release 2.30.2.1

* Tue Apr 27 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.30.2-1mdv2010.1
+ Revision: 539772
- update to new version 2.30.2

* Sat Apr 17 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.30.1-1mdv2010.1
+ Revision: 535747
- update to new version 2.30.1

* Tue Mar 30 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.30.0-1mdv2010.1
+ Revision: 528950
- update to new version 2.30.0

* Thu Mar 25 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.29.3-1mdv2010.1
+ Revision: 527510
- update to new version 2.29.3

* Thu Mar 04 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.29.2-1mdv2010.1
+ Revision: 514168
- update to new version 2.29.2

* Thu Mar 04 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.29.1-1mdv2010.1
+ Revision: 514073
- new version
- readd pkgconfig file

* Thu Feb 25 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.29.0-1mdv2010.1
+ Revision: 511312
- new version
- update file list

* Tue Sep 22 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.28.0-1mdv2010.0
+ Revision: 447182
- update to new version 2.28.0

* Thu Aug 13 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.27.90-1mdv2010.0
+ Revision: 415949
- update to new version 2.27.90

* Tue Mar 17 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.26.0-1mdv2009.1
+ Revision: 356487
- update to new version 2.26.0

* Wed Mar 11 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.25.92-1mdv2009.1
+ Revision: 353611
- update to new version 2.25.92

* Tue Feb 17 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.25.91-1mdv2009.1
+ Revision: 341225
- update to new version 2.25.91

* Wed Feb 11 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.25.90-1mdv2009.1
+ Revision: 339526
- update to new version 2.25.90

* Tue Sep 23 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.24.0-1mdv2009.0
+ Revision: 287366
- new version

* Tue Sep 09 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.23.92-1mdv2009.0
+ Revision: 282919
- new version

* Sun Aug 31 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.23.91-1mdv2009.0
+ Revision: 277783
- new version

* Tue Aug 19 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.23.90-1mdv2009.0
+ Revision: 273588
- new version

* Tue Jul 22 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.23.3-1mdv2009.0
+ Revision: 239990
- new version

* Fri Jul 04 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.23.2-2mdv2009.0
+ Revision: 231754
- readd icon mappings

* Thu Jul 03 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.23.2-1mdv2009.0
+ Revision: 230994
- new version
- update license
- update buildrequires

* Tue Jun 10 2008 Pixel <pixel@mandriva.com> 2.22.0-1mdv2009.0
+ Revision: 217432
- add rpm filetrigger running gtk-update-icon-cache when rpm install/remove gnome icons

* Tue Mar 11 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.22.0-1mdv2008.1
+ Revision: 186586
- new version

* Mon Feb 25 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.21.92-1mdv2008.1
+ Revision: 174585
- new version

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Tue Dec 18 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.21.4-1mdv2008.1
+ Revision: 132681
- new version

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Nov 24 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.21.0-1mdv2008.1
+ Revision: 111752
- new version

* Tue Sep 18 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.20.0-1mdv2008.0
+ Revision: 89459
- new version

* Fri Sep 07 2007 Frederic Crozat <fcrozat@mandriva.com> 2.19.91-3mdv2008.0
+ Revision: 81812
- Fix conflicts with nautilus-filesharing for upgrade (Mdv bug #33107)

* Tue Aug 28 2007 Frederic Crozat <fcrozat@mandriva.com> 2.19.91-2mdv2008.0
+ Revision: 72675
- Remove source1, no longer provide mdk folders icons
- don't update hicolor icon cache, package no longer provides stuff there

* Tue Aug 28 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.19.91-1mdv2008.0
+ Revision: 72491
- new version

* Tue Aug 14 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.19.90-1mdv2008.0
+ Revision: 63193
- new version

* Fri Aug 03 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.19.6-1mdv2008.0
+ Revision: 58584
- new version
- fix build

* Fri Jun 29 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.19.1-1mdv2008.0
+ Revision: 45777
- new version


* Fri Mar 30 2007 Frederic Crozat <fcrozat@mandriva.com> 2.18.0-2mdv2007.1
+ Revision: 149870
- Update mdk icons

* Mon Mar 12 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.18.0-1mdv2007.1
+ Revision: 142092
- new version

  + Thierry Vignaud <tvignaud@mandriva.com>
    - no need to package big ChangeLog when NEWS is already there

* Mon Feb 12 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.17.91-1mdv2007.1
+ Revision: 120205
- new version

* Mon Jan 22 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.17.90-1mdv2007.1
+ Revision: 112121
- new version

* Tue Jan 09 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.17.5-1mdv2007.1
+ Revision: 106547
- new version

* Wed Dec 20 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.17.4.1-1mdv2007.1
+ Revision: 100612
- new version

* Wed Dec 20 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.17.4-1mdv2007.1
+ Revision: 100373
- new version

* Wed Dec 06 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.17.3-1mdv2007.1
+ Revision: 91595
- new version

* Mon Nov 27 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.17.2.1-1mdv2007.1
+ Revision: 87670
- new version

* Tue Nov 21 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.16.1-1mdv2007.1
+ Revision: 85863
- Import gnome-icon-theme

* Tue Nov 21 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.16.1-1mdv2007.1
- New version 2.16.1

* Wed Sep 06 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.16.0.1-1mdv2007.0
- New release 2.16.0.1

* Tue Sep 05 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.16.0-1mdv2007.0
- New release 2.16.0

* Sat Sep 02 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.15.92-1mdv2007.0
- rebuild for new clean_icon_cache macro

* Thu Aug 31 2006 Götz Waschk <waschk@mandriva.org> 2.15.92-2mdv2007.0
- fix uninstallation

* Wed Aug 23 2006 Götz Waschk <waschk@mandriva.org> 2.15.92-1mdv2007.0
- bump deps
- New release 2.15.92

* Wed Aug 09 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.15.91-1mdv2007.0
- New release 2.15.91

* Thu Jul 27 2006 Götz Waschk <waschk@mandriva.org> 2.15.90-2mdv2007.0
- fix uninstallation

* Wed Jul 26 2006 Götz Waschk <waschk@mandriva.org> 2.15.90-1mdv2007.0
- bump deps
- New release 2.15.90

* Fri Jul 14 2006 Frederic Crozat <fcrozat@mandriva.com> 2.15.3-2mdv2007.0
- use icon cache macro

* Tue Jul 11 2006 Götz Waschk <waschk@mandriva.org> 2.15.3-1mdv2007.0
- bump deps
- New release 2.15.3

* Thu Apr 13 2006 Frederic Crozat <fcrozat@mandriva.com> 2.14.2-1mdk
- Release 2.14.2

* Mon Feb 27 2006 Frederic Crozat <fcrozat@mandriva.com> 2.12.1-3mdk
- Fortify uninstall script

* Thu Feb 23 2006 Frederic Crozat <fcrozat@mandriva.com> 2.12.1-2mdk
- Use mkrel

* Thu Oct 06 2005 Frederic Crozat <fcrozat@mandriva.com> 2.12.1-1mdk
- Release 2.12.1

* Thu Sep 08 2005 Frederic Crozat <fcrozat@mandriva.com> 2.10.1-5mdk 
- Add source1 : icons for default directories

* Fri Sep 02 2005 Frederic Crozat <fcrozat@mandriva.com> 2.10.1-4mdk 
- Fix prereq (Mdk bug #17494)

* Thu Apr 28 2005 Frederic Crozat <fcrozat@mandriva.com> 2.10.1-3mdk 
- Move .pc file to /usr/share/pkgconfig, remove biarch stuff (no longer
  needed) and we're back as noarch package

* Sat Apr 23 2005 Frederic Crozat <fcrozat@mandriva.com> 2.10.1-2mdk 
- Run gtk-update-icon-cache when uninstalling package too

* Thu Apr 21 2005 Frederic Crozat <fcrozat@mandriva.com> 2.10.1-1mdk 
- Release 2.10.1 (based on Götz Waschk package)

* Tue Mar 01 2005 Frederic Crozat <fcrozat@mandrakesoft.com> 2.8.0-3mdk 
- run gtk-update-icon-cache at install time

* Mon Feb 28 2005 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 2.8.0-2mdk
- this package has noarch contents but some locations are not noarch,
  i.e. make it arch-dependent
- provide 32-bit pkgconfig file on biarch platforms, don't bother
  with creating an extra package especially since only evoluton checks
  for its existence

* Tue Oct 19 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 2.8.0-1mdk
- New release 2.8.0

* Fri Sep 03 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 1.2.3-2mdk
- Add symlink for mimetype alias

* Tue Jun 08 2004 Goetz Waschk <waschk@linux-mandrake.com> 1.2.3-1mdk
- New release 1.2.3

* Fri Apr 23 2004 Götz Waschk <waschk@linux-mandrake.com> 1.2.1-3mdk
- fix buildrequires

* Thu Apr 22 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 1.2.1-2mdk
- Fix BuildRequires

* Tue Apr 20 2004 Goetz Waschk <goetz@mandrakesoft.com> 1.2.1-1mdk
- New release 1.2.1

* Tue Apr 06 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 1.2.0-2mdk
- Requires hicolor theme package

* Sat Apr 03 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 1.2.0-1mdk
- Release 1.2.0 (with Götz Waschk help)
- update doc list
- drop patch
- don't remove hicolor icons

