%define url_ver %(echo %{version}|cut -d. -f1,2)

Summary:	GNOME default icons
Name:		gnome-icon-theme
Version:	3.12.0
Release:	1
License:	GPLv2+
Group:		Graphical desktop/GNOME
Url:		http://www.gnome.org/
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/gnome-icon-theme/%{url_ver}/%{name}-%{version}.tar.xz
BuildArch:	noarch

BuildRequires:	intltool
BuildRequires:	hicolor-icon-theme
BuildRequires:	icon-naming-utils >= 0.8.7
BuildRequires:	gtk+2.0
Requires:	hicolor-icon-theme
Requires(post,postun):	gtk+2.0

%description
GNOME default icons.

%package	devel
Summary:	Development files for gnome-icon-theme
Group:		Development/C
Requires:	%{name} = %{version}-%{release}

%description devel
Development files for gnome-icon-theme

%prep
%setup -q

%build
%configure --enable-icon-mapping
%make

%install
%makeinstall_std
touch %{buildroot}%{_datadir}/icons/gnome/icon-theme.cache

# automatic gtk icon cache update on rpm installs/removals
# (see http://wiki.mandriva.com/en/Rpm_filetriggers)
install -d %{buildroot}%{_var}/lib/rpm/filetriggers
cat > %{buildroot}%{_var}/lib/rpm/filetriggers/gtk-icon-cache-gnome.filter << EOF
^./usr/share/icons/gnome/
EOF
cat > %{buildroot}%{_var}/lib/rpm/filetriggers/gtk-icon-cache-gnome.script << EOF

if [ -x /usr/bin/gtk-update-icon-cache ]; then 
	/usr/bin/gtk-update-icon-cache --force --quiet /usr/share/icons/gnome
fi
EOF
chmod 755 %{buildroot}%{_var}/lib/rpm/filetriggers/gtk-icon-cache-gnome.script

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
%{_datadir}/pkgconfig/%{name}.pc
