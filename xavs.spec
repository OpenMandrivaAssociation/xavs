%define	major	1
%define	libname	%mklibname xavs %{major}
%define	devname	%mklibname -d xavs

Summary:	Audio Video Standard of China
Name:		xavs
Version:	0.1.55
Release:	1
License:	GPLv2+
Group:		Video
URL:		http://xavs.sourceforge.net/
Source0:	%{name}-%{version}.tar.xz

%description
AVS is the Audio Video Standard of China.  This project aims to
implement high quality AVS encoder and decoder.

%package -n	%{libname}
Group:		System/Libraries
Summary:	Audio Video Standard of China

%description -n	%{libname}
AVS is the Audio Video Standard of China.  This project aims to
implement high quality AVS encoder and decoder.

%package -n	%{devname}
Group:		Development/C
Summary:	Development files for libxavs
Requires:	%{libname} = %{EVRD}

%description -n	%{devname}
This package contains development files required to build applications against
libxavs.

%prep
%setup -q

%build
CFLAGS="%{optflags} -Ofast" \
%configure2_5x	--enable-shared \
		--disable-asm
# enabling asm code breaks build

%install
%makeinstall_std

%files
%doc doc/*.txt
%{_bindir}/xavs

%files -n %{libname}
%{_libdir}/libxavs.so.%{major}*

%files -n %{devname}
%{_includedir}/xavs.h
%{_libdir}/libxavs.a
%{_libdir}/libxavs.so
%{_libdir}/pkgconfig/xavs.pc

