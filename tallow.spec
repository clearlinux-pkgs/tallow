#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : tallow
Version  : 21
Release  : 33
URL      : https://github.com/clearlinux/tallow/releases/download/v21/tallow-21.tar.xz
Source0  : https://github.com/clearlinux/tallow/releases/download/v21/tallow-21.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0
Requires: tallow-autostart = %{version}-%{release}
Requires: tallow-bin = %{version}-%{release}
Requires: tallow-data = %{version}-%{release}
Requires: tallow-license = %{version}-%{release}
Requires: tallow-man = %{version}-%{release}
Requires: tallow-services = %{version}-%{release}
Requires: ipset
Requires: iptables
Requires: tallow-doc
BuildRequires : ipset
BuildRequires : iptables
BuildRequires : pkgconfig(json-c)
BuildRequires : pkgconfig(libpcre)
BuildRequires : pkgconfig(libsystemd)

%description
tallow
======
Tallow is a fail2ban/lard replacement that uses systemd's native
journal API to scan for attempted ssh logins, and issues temporary
IP bans for clients that violate certain login patterns.

%package autostart
Summary: autostart components for the tallow package.
Group: Default

%description autostart
autostart components for the tallow package.


%package bin
Summary: bin components for the tallow package.
Group: Binaries
Requires: tallow-data = %{version}-%{release}
Requires: tallow-license = %{version}-%{release}
Requires: tallow-services = %{version}-%{release}

%description bin
bin components for the tallow package.


%package data
Summary: data components for the tallow package.
Group: Data

%description data
data components for the tallow package.


%package doc
Summary: doc components for the tallow package.
Group: Documentation
Requires: tallow-man = %{version}-%{release}

%description doc
doc components for the tallow package.


%package license
Summary: license components for the tallow package.
Group: Default

%description license
license components for the tallow package.


%package man
Summary: man components for the tallow package.
Group: Default

%description man
man components for the tallow package.


%package services
Summary: services components for the tallow package.
Group: Systemd services

%description services
services components for the tallow package.


%prep
%setup -q -n tallow-21
cd %{_builddir}/tallow-21

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1619061049
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1619061049
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/tallow
cp %{_builddir}/tallow-21/COPYING %{buildroot}/usr/share/package-licenses/tallow/8624bcdae55baeef00cd11d5dfcfa60f68710a02
%make_install
## service_restart content
mkdir -p %{buildroot}/usr/share/clr-service-restart
ln -s /usr/lib/systemd/system/tallow.service %{buildroot}/usr/share/clr-service-restart/tallow.service
## service_restart end
## install_append content
mkdir -p %{buildroot}/usr/lib/systemd/system/multi-user.target.wants/
ln -s ../tallow.service %{buildroot}/usr/lib/systemd/system/multi-user.target.wants/tallow.service
## install_append end

%files
%defattr(-,root,root,-)

%files autostart
%defattr(-,root,root,-)
/usr/lib/systemd/system/multi-user.target.wants/tallow.service

%files bin
%defattr(-,root,root,-)
/usr/bin/tallow

%files data
%defattr(-,root,root,-)
/usr/share/clr-service-restart/tallow.service
/usr/share/tallow/sshd.json

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/tallow/*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/tallow/8624bcdae55baeef00cd11d5dfcfa60f68710a02

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/tallow.1
/usr/share/man/man5/tallow.conf.5
/usr/share/man/man5/tallow.patterns.5

%files services
%defattr(-,root,root,-)
%exclude /usr/lib/systemd/system/multi-user.target.wants/tallow.service
/usr/lib/systemd/system/tallow.service
