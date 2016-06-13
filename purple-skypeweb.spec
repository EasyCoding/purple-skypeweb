%global plugin_name skypeweb

%global commit0 eb0b5000c56c9c264375ab2334c926c9715ee3d0
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global date 20160510

Name: purple-%{plugin_name}
Version: 1.1
Release: 7.%{date}git%{shortcommit0}%{?dist}
Summary: Adds support for Skype to Pidgin

License: GPLv3
URL: https://github.com/EionRobb/skype4pidgin
Source0: https://github.com/EionRobb/skype4pidgin/archive/%{commit0}.tar.gz#/skype4pidgin-%{shortcommit0}.tar.gz

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
%autosetup -n skype4pidgin-%{commit0}
cd %{plugin_name}

# fix W: wrong-file-end-of-line-encoding
perl -i -pe 's/\r\n/\n/gs' README.md

%build
cd %{plugin_name}
export CFLAGS="%{optflags}"
%make_build

%install
cd %{plugin_name}
%make_install
chmod 755 %{buildroot}%{_libdir}/purple-2/lib%{plugin_name}.so

%files
%{_libdir}/purple-2/lib%{plugin_name}.so
%doc %{plugin_name}/README.md CHANGELOG.txt
%license COPYING.txt

%files -n pidgin-%{plugin_name}
%{_datadir}/pixmaps/pidgin/protocols/*/skype*.png
%{_datadir}/pixmaps/pidgin/emotes/skype

%changelog
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
