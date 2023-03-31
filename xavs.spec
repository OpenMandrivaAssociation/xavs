%define	major	1
%define	libname	%mklibname xavs %{major}
%define	devname	%mklibname -d xavs

Summary:	Audio Video Standard of China
Name:		xavs
Version:	0.1.55
Release:	19
License:	GPLv2+
Group:		Video
URL:		http://xavs.sourceforge.net/
Source0:	%{name}-%{version}.tar.xz
Patch0:		xavs-0.1.55-dont-strip-symbols.patch

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
%patch0 -p1 -b .nostrip~

%build
CFLAGS="%{optflags} -Ofast -fPIC" \
%configure	--enable-shared \
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


%changelog
* Thu Nov 24 2011 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.1.55-2
+ Revision: 733114
- don't strip symbols during build (P0)

* Thu Nov 24 2011 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.1.55-1
+ Revision: 733097
- imported package xavs


* Thu Nov 24 2011 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.1.55-1
- initial Mandriva package

* Mon Mar 14 2011 Axel Thimm <Axel.Thimm@ATrpms.net> - 0.1.51-2
- Initial build.
