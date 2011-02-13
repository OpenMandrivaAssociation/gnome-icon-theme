Summary: GNOME default icons
Name: gnome-icon-theme
Version: 2.31.0
Release: %mkrel 3
License: GPLv2+
Group: Graphical desktop/GNOME
URL: http://www.gnome.org/
Source0: ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.bz2
# (fc) 2.30.2.1-2mdv add missing volume icons (Mdv bug #59329) (GIT)
Source1: missing-audio.tar
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot
BuildRequires: intltool
BuildRequires: hicolor-icon-theme
BuildRequires: icon-naming-utils >= 0.8.7
BuildArch: noarch
Requires: hicolor-icon-theme
Requires(post):	gtk+2.0 >= 2.6.0
Requires(postun):gtk+2.0 >= 2.6.0
Conflicts: nautilus < 2.19.91-3mdv
Conflicts: nautilus-filesharing < 0.2-3mdv

%description
GNOME default icons

%prep
%setup -q -a1

%build
./configure --prefix=%_prefix --enable-icon-mapping
%make

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall_std
touch %buildroot%{_datadir}/icons/gnome/icon-theme.cache

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache gnome

%postun
%clean_icon_cache gnome

%triggerin -- %{_iconsdir}/gnome/*/*/*
%update_icon_cache gnome

%triggerpostun -- %{_iconsdir}/gnome/*/*/*
%update_icon_cache gnome

%files
%defattr(-,root,root,-)
%doc README TODO
%dir %{_datadir}/icons/gnome
%{_datadir}/icons/gnome/*x*
%_datadir/pkgconfig/%name.pc
%ghost %{_datadir}/icons/gnome/icon-theme.cache
