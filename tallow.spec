#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : tallow
Version  : 3
Release  : 6
URL      : https://github.com/sofar/tallow/releases/download/v3/tallow-3.tar.gz
Source0  : https://github.com/sofar/tallow/releases/download/v3/tallow-3.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0
Requires: tallow-bin
Requires: tallow-config
Requires: tallow-doc
Requires: ipset
BuildRequires : pkgconfig(libsystemd)
Patch1: run-as-nice.patch

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
Requires: tallow-config

%description bin
bin components for the tallow package.


%package config
Summary: config components for the tallow package.
Group: Default

%description config
config components for the tallow package.


%package doc
Summary: doc components for the tallow package.
Group: Documentation

%description doc
doc components for the tallow package.


%prep
%setup -q -n tallow-3
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1494261622
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto -fno-semantic-interposition "
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1494261622
rm -rf %{buildroot}
%make_install
## make_install_append content
mkdir -p %{buildroot}/usr/lib/systemd/system/multi-user.target.wants/
ln -s ../tallow.service %{buildroot}/usr/lib/systemd/system/multi-user.target.wants/tallow.service
## make_install_append end

%files
%defattr(-,root,root,-)

%files autostart
%defattr(-,root,root,-)
/usr/lib/systemd/system/multi-user.target.wants/tallow.service

%files bin
%defattr(-,root,root,-)
/usr/bin/tallow

%files config
%defattr(-,root,root,-)
%exclude /usr/lib/systemd/system/multi-user.target.wants/tallow.service
/usr/lib/systemd/system/tallow.service

%files doc
%defattr(-,root,root,-)
%doc /usr/share/doc/tallow/*
%doc /usr/share/man/man1/*
%doc /usr/share/man/man5/*
