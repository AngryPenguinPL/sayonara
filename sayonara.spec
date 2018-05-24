%define _disable_ld_no_undefined 1

%define tarball git5-20180115

Summary:	A lightweight Qt Audio player
Name:		sayonara
Version:	1.0.0
Release:	1
License:	GPLv3+
Group:		Sound
Url:		http://sayonara-player.com
Source0:	http://sayonara-player.com/sw/%{name}-player-%{version}-%{tarball}.tar.gz
BuildRequires:	cmake
BuildRequires:	qt5-linguist-tools
BuildRequires:	qt5-tools
BuildRequires:	pkgconfig(gstreamer-app-1.0)
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	pkgconfig(libmtp)
BuildRequires:	pkgconfig(libnotify)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5DBus)
BuildRequires:	pkgconfig(Qt5Help)
BuildRequires:	pkgconfig(Qt5Network)
BuildRequires:	pkgconfig(Qt5Sql)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5Xml)
BuildRequires:	pkgconfig(libnotify)
BuildRequires:	pkgconfig(taglib)
BuildRequires:	pkgconfig(zlib)
Requires:	qt5-database-plugin-sqlite

%description
Sayonara is a small, clear, not yet platform-independent music player.
Low CPU usage, low memory consumption and no long loading times are only
three benefits of this player. Sayonara should be easy and intuitive to
use and therefore it should be able to compete with the most popular
music players.

%files
%doc MANUAL README.txt
%{_bindir}/%{name}
%{_libdir}/%{name}/
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/pixmaps/%{name}.png
%{_iconsdir}/%{name}.png
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_iconsdir}/hicolor/*/apps/%{name}.xpm
%{_mandir}/man1/%{name}.1.*

#----------------------------------------------------------------------------

%prep
%setup -q -n %{name}-player

%build
%cmake_qt5
%make

%install
%makeinstall_std -C build

# remove menu dir, because it's not necessary
rm -rf %{buildroot}%{_datadir}/menu

