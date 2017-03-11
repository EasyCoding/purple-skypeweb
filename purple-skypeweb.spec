%global plugin_name skypeweb

%global commit0 19ba66e3f01075dc82b2c3a7617bd6836177ced8
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global date 20170226

Name: purple-%{plugin_name}
Version: 1.2.2
Release: 7.%{date}git%{shortcommit0}%{?dist}
Summary: Adds support for Skype to Pidgin

License: GPLv3
URL: https://github.com/EionRobb/skype4pidgin

# Run ./generate-tarball.sh script to build tarball from
# official Git repository without legacy sources.
Source0: %{name}-%{shortcommit0}.tar.xz
Source1: generate-tarball.sh

BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(purple)
BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: pkgconfig(zlib)
BuildRequires: gcc

Provides: skype4pidgin = %{version}-%{release}
Obsoletes: skype4pidgin < %{version}-%{release}

%description
Adds support for Skype to Pidgin, Adium, Finch and other libpurple 
based messengers.

%package -n pidgin-%{plugin_name}
Summary: Adds pixmaps, icons and smileys for Skype protocol
BuildArch: noarch
Requires: %{name} = %{version}-%{release}
Requires: pidgin

%description -n pidgin-%{plugin_name}
Adds pixmaps, icons and smileys for Skype protocol implemented by libskypeweb.

%prep
%autosetup -n %{name}-%{commit0}

# fix W: wrong-file-end-of-line-encoding
perl -i -pe 's/\r\n/\n/gs' README.md

%build
export CFLAGS="%{optflags}"
export LDFLAGS="%{__global_ldflags}"
%make_build

%install
%make_install
chmod 755 %{buildroot}%{_libdir}/purple-2/lib%{plugin_name}.so

%files
%{_libdir}/purple-2/lib%{plugin_name}.so
%doc README.md
%license gpl3.txt

%files -n pidgin-%{plugin_name}
%{_datadir}/pixmaps/pidgin/protocols/*/skype*.png
%{_datadir}/pixmaps/pidgin/emotes/skype

%changelog
* Sat Mar 11 2017 Vitaly Zaitsev <vitaly@easycoding.org> - 1.2.2-7.20170226git19ba66e
- Updated to latest snapshot.

* Thu Dec 22 2016 Vitaly Zaitsev <vitaly@easycoding.org> - 1.2.2-6.20161220gitfa888e0
- Updated to latest snapshot.

* Tue Nov 22 2016 Vitaly Zaitsev <vitaly@easycoding.org> - 1.2.2-5.20161122git92c376f
- Updated to latest snapshot.

* Thu Oct 27 2016 Vitaly Zaitsev <vitaly@easycoding.org> - 1.2.2-4.20161027git3208958
- Updated to latest snapshot.

* Sun Oct 16 2016 Vitaly Zaitsev <vitaly@easycoding.org> - 1.2.2-3.20161015gitd23eab9
- Fixed typo in changelog section. Fixed warning.

* Sun Oct 16 2016 Vitaly Zaitsev <vitaly@easycoding.org> - 1.2.2-2.20161015gitd23eab9
- Added patch to support correct build flags.

* Sun Oct 16 2016 Vitaly Zaitsev <vitaly@easycoding.org> - 1.2.2-1.20161015gitd23eab9
- Updated to version 1.2.2.

* Mon Aug 08 2016 Vitaly Zaitsev <vitaly@easycoding.org> - 1.2.1-1.20160808gitf477d9e
- Updated to version 1.2.1.

* Thu Jul 21 2016 Vitaly Zaitsev <vitaly@easycoding.org> - 1.2-2.20160720git2b42d11
- Updated to latest Git snapshot.

* Thu Jul 14 2016 Vitaly Zaitsev <vitaly@easycoding.org> - 1.2-1.20160714git41cd230
- Updated to version 1.2.

* Tue Jun 21 2016 Vitaly Zaitsev <vitaly@easycoding.org> - 1.1-11.20160620git72f0b00
- Added missing LDFLAGS to build.

* Mon Jun 20 2016 Vitaly Zaitsev <vitaly@easycoding.org> - 1.1-10.20160620git72f0b00
- Updated to latest Git snapshot.

* Wed Jun 15 2016 Vitaly Zaitsev <vitaly@easycoding.org> - 1.1-9.20160510giteb0b500
- Updated script generate-tarball.sh (written by Simone Caronni).

* Tue Jun 14 2016 Vitaly Zaitsev <vitaly@easycoding.org> - 1.1-8.20160510giteb0b500
- Added script generate-tarball.sh which can be used to remove legacy sources from tarball.

* Mon Jun 13 2016 Vitaly Zaitsev <vitaly@easycoding.org> - 1.1-7.20160510giteb0b500
- Fixed directory ownership. Removed patch.

* Sun Jun 12 2016 Vitaly Zaitsev <vitaly@easycoding.org> - 1.1-6.20160510giteb0b500
- Removed empty configure script. Now obsoletes skype4pidgin package.

* Sun Jun 12 2016 Vitaly Zaitsev <vitaly@easycoding.org> - 1.1-5.20160510giteb0b500
- Updated to latest Git version.

* Mon May 02 2016 Vitaly Zaitsev <vitaly@easycoding.org> - 1.1-4.20160420gitf23913d
- Updated to latest Git version.

* Fri Mar 04 2016 Vitaly Zaitsev <vitaly@easycoding.org> - 1.1-3.20160226git80368db
- Updated to latest Git version.

* Tue Feb 16 2016 Vitaly Zaitsev <vitaly@easycoding.org> - 1.1-2.20160214git04312d8
- Updated to latest Git version. Added EPEL7 support.

* Thu Jan 07 2016 Vitaly Zaitsev <vitaly@easycoding.org> - 1.1-1.20160107git9764e31
- Updated to version 1.1: added support of file transfers, fixed Live logins, fixed other crashes.

* Sat Jan 02 2016 Vitaly Zaitsev <vitaly@easycoding.org> - 1.0-4.20160101git68cb5f3
- Updated to latest version: added support for receiving server-backed files. Added patch.

* Fri Dec 25 2015 Vitaly Zaitsev <vitaly@easycoding.org> - 1.0-3.20151225gita173efa
- Updated to latest version: fixed plugin crash.

* Thu Nov 26 2015 Vitaly Zaitsev <vitaly@easycoding.org> - 1.0-2
- Applyed Maxim Orlov's fixes.

* Sun Nov 08 2015 Vitaly Zaitsev <vitaly@easycoding.org> - 1.0-1
- Updated to version 1.0.

* Mon Aug 24 2015 jparvela <jparvela@gmail.com> - 0.1-4
- Added missing files to spec file list.

* Mon Aug 03 2015 BOPOHA <vorona.tolik@gmail.com> - 0.1-3
- Fixed build with OBS. RPMS can be built from main tarball.

* Sat May 09 2015 Vitaly Zaitsev <vitaly@easycoding.org> - 0.1-2
- Separated packages. Now can be used with other libpurple-based clients without Pidgin being installed.

* Mon Mar 16 2015 Vitaly Zaitsev <vitaly@easycoding.org> - 0.1-1
- Created first RPM spec for Fedora/openSUSE.
