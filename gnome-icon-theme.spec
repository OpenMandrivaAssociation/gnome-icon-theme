Summary: GNOME default icons
Name: gnome-icon-theme
Version: 2.29.2
Release: %mkrel 1
License: GPLv2+
Group: Graphical desktop/GNOME
URL: http://www.gnome.org/
Source0: ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot
BuildRequires: intltool
BuildRequires: hicolor-icon-theme
BuildRequires: icon-naming-utils >= 0.8.1
BuildArch: noarch
Requires: hicolor-icon-theme
Requires(post):	gtk+2.0 >= 2.6.0
Requires(postun):gtk+2.0 >= 2.6.0
Conflicts: nautilus < 2.19.91-3mdv
Conflicts: nautilus-filesharing < 0.2-3mdv

%description
GNOME default icons

%prep
%setup -q

%build

./configure --prefix=%_prefix --enable-icon-mapping

%make

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall_std
touch %buildroot%{_datadir}/icons/gnome/icon-theme.cache

# automatic gtk icon cache update on rpm installs/removals
# (see http://wiki.mandriva.com/en/Rpm_filetriggers)
install -d %buildroot%{_var}/lib/rpm/filetriggers
cat > %buildroot%{_var}/lib/rpm/filetriggers/gtk-icon-cache-gnome.filter << EOF
^./usr/share/icons/gnome/
EOF
cat > %buildroot%{_var}/lib/rpm/filetriggers/gtk-icon-cache-gnome.script << EOF
#!/bin/sh
if [ -x /usr/bin/gtk-update-icon-cache ]; then 
  /usr/bin/gtk-update-icon-cache --force --quiet /usr/share/icons/gnome
fi
EOF
chmod 755 %buildroot%{_var}/lib/rpm/filetriggers/gtk-icon-cache-gnome.script


%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache gnome

%postun
%clean_icon_cache gnome

%files
%defattr(-,root,root,-)
%doc README TODO
%dir %{_datadir}/icons/gnome
%{_datadir}/icons/gnome/*x*
%_datadir/pkgconfig/%name.pc
%ghost %{_datadir}/icons/gnome/icon-theme.cache
%{_var}/lib/rpm/filetriggers/gtk-icon-cache-gnome.*
