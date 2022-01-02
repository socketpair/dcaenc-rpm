Name: dcaenc
Summary: Dcaenc DTS 5.1 encoder
Version: 3
Release: 1%{?icsgit}%{?dist}
License: LGPLv2
URL: https://gitlab.com/patrakov/dcaenc

BuildRequires: alsa-lib-devel
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: gcc
BuildRequires: libtool
BuildRequires: make
BuildRequires: pkgconf

Source0: https://gitlab.com/patrakov/dcaenc/-/archive/v%{version}/%{name}-v%{version}.tar.gz
Source1: HOWTO.TXT
Patch0: warnings.patch

%description
Dcaenc DTS 5.1 encoder.

%package utils
Summary: Dcaenc DTS 5.1 encoder command-line tool

%description utils
Dcaenc DTS 5.1 encoder command-line tool.

%package -n libdcaenc
Summary: Dcaenc DTS 5.1 encoder shared library

%description -n libdcaenc
Dcaenc DTS 5.1 encoder shared library.

%package -n alsa-plugins-%{name}
Summary: Dcaenc DTS 5.1 encoder Alsa plugin

%description -n alsa-plugins-%{name}
This plugin allows to encode (compress) raw 6-stream
PCM audio to "2-channel" DTS format. Suitable for
transferring to HDMI or S/PDIF receivers.

Another option is to encode to AC3 (AC-3) using
alsa-plugins-freeworld-a52 package, but it is different
codec.

See %{_defaultdocdir}/alsa-plugins-%{name}/HOWTO.TXT for explanations.

%package devel
Summary: Dcaenc DTS 5.1 encoder development files
Requires: libdcaenc = %{version}-%{release}

%description devel
Dcaenc DTS 5.1 encoder development files.

%prep
%autosetup -n %{name}-v%{version}
install -p -D -m 644 %{SOURCE1} HOWTO.TXT

%build
# Source archive does not provide ./configure.
autoreconf -fiv
%configure
%make_build

%install
%make_install
find %{buildroot} -type f -name '*.la' -delete

mkdir -p                        %{buildroot}%{_datadir}/alsa/alsa.conf.d
echo '<confdir:pcm/dca.conf>' > %{buildroot}%{_datadir}/alsa/alsa.conf.d/60-%{name}.conf

mkdir -p                                           %{buildroot}%{_sysconfdir}/alsa/conf.d
ln -s %{_datadir}/alsa/alsa.conf.d/60-%{name}.conf %{buildroot}%{_sysconfdir}/alsa/conf.d/

%files utils
%{_bindir}/*

%files devel
%{_includedir}/*
%{_libdir}/pkgconfig/*
%{_libdir}/*.so

%files -n libdcaenc
%{_libdir}/*.so.*

%files -n alsa-plugins-%{name}
%{_libdir}/alsa-lib/*.so
%{_datadir}/alsa/pcm/*
%{_datadir}/alsa/alsa.conf.d/*
%config %{_sysconfdir}/alsa/conf.d/*
%doc README
%doc TODO
%doc BUGS
%doc AUTHORS
%doc HOWTO.TXT
