Summary: GNOME default icons
Name: gnome-icon-theme
Version: 3.4.0
Release: 1
License: GPLv2+
Group: Graphical desktop/GNOME
URL: http://www.gnome.org/
Source0: ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.xz
BuildArch: noarch

BuildRequires: gtk+2.0
BuildRequires: hicolor-icon-theme
BuildRequires: icon-naming-utils >= 0.8.7
BuildRequires: intltool

Requires: hicolor-icon-theme
Requires(post,postun):	gtk+2.0

%description
GNOME default icons

%package devel
Summary:	The pkgconfig for %{name}
Group:		Development/GNOME and GTK+
Requires:	%{name} = %{version}

%description devel
The pkgconfig for %{name}.

%prep
%setup -q

%build
%configure2_5x --enable-icon-mapping
%make

%install
rm -rf %{buildroot}

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

%post
%update_icon_cache gnome

%postun
%clean_icon_cache gnome

%files
%doc README TODO
%dir %{_datadir}/icons/gnome
%{_datadir}/icons/gnome/*x*
%ghost %{_datadir}/icons/gnome/icon-theme.cache
%{_var}/lib/rpm/filetriggers/gtk-icon-cache-gnome.*

%files devel
%_datadir/pkgconfig/%name.pc
