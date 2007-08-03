Summary: GNOME default icons
Name: gnome-icon-theme
Version: 2.19.6
Release: %mkrel 1
License: GPL
Group: Graphical desktop/GNOME
URL: http://www.gnome.org/
Source0: ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.bz2
Source1: mdk-icons.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot
BuildRequires: perl-XML-Parser
BuildRequires: hicolor-icon-theme
BuildRequires: icon-naming-utils >= 0.8.1
BuildArch: noarch
Requires: hicolor-icon-theme
Requires(post):	gtk+2.0 >= 2.6.0
Requires(postun):gtk+2.0 >= 2.6.0

%description
GNOME default icons

%prep
%setup -q
mkdir hicolor
cd hicolor
tar xjf %SOURCE1

%build

./configure --prefix=%_prefix

%make

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall_std
cp -r hicolor $RPM_BUILD_ROOT%{_iconsdir}

tar -C $RPM_BUILD_ROOT%{_iconsdir}/hicolor -xjf %{SOURCE1}

touch %buildroot%{_datadir}/icons/gnome/icon-theme.cache

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache gnome
%update_icon_cache hicolor

%postun
%clean_icon_cache hicolor
%clean_icon_cache gnome

%files
%defattr(-,root,root,-)
%doc NEWS TODO
%dir %{_datadir}/icons/gnome
%{_datadir}/icons/gnome/*x*
%{_datadir}/icons/gnome/scalable
%{_datadir}/icons/hicolor/*
%{_datadir}/pkgconfig/%{name}.pc
%ghost %{_datadir}/icons/gnome/icon-theme.cache


