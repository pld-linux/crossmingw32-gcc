#
# Conditional build:
%bcond_with	bootstrap	# bootstrap build (using binary w32api/mingwrt, only C/C++, no gomp)
%bcond_without	pthreads	# POSIX threads support (needed for GOMP and C++ 11 thread/mutex support)
%bcond_without	gomp		# OpenMP libraries
%bcond_with	ada		# Ada language support (doesn't build for mingw32)
%bcond_without	d		# D language support
# go is not supported for mingw

%if %{with bootstrap}
%undefine	with_pthreads
%undefine	with_ada
%undefine	with_d
%endif
%if %{without pthreads}
%undefine	with_gomp
%endif
Summary:	Cross MinGW32 GNU binary utility development utilities - gcc
Summary(es.UTF-8):	Utilitarios para desarrollo de binarios de la GNU - MinGW32 gcc
Summary(fr.UTF-8):	Utilitaires de développement binaire de GNU - MinGW32 gcc
Summary(pl.UTF-8):	Skrośne narzędzia programistyczne GNU dla MinGW32 - gcc
Summary(pt_BR.UTF-8):	Utilitários para desenvolvimento de binários da GNU - MinGW32 gcc
Summary(tr.UTF-8):	GNU geliştirme araçları - MinGW32 gcc
Name:		crossmingw32-gcc
Version:	12.4.0
Release:	1
Epoch:		1
License:	GPL v3+
Group:		Development/Languages
Source0:	https://ftp.gnu.org/gnu/gcc/gcc-%{version}/gcc-%{version}.tar.xz
# Source0-md5:	fd7779aee878db67456575922281fa71
%define		w32api_ver	5.4.2
#Source1Download: https://osdn.net/projects/mingw/releases/
Source1:	https://osdn.net/projects/mingw/downloads/74926/w32api-%{w32api_ver}-mingw32-dev.tar.xz
# Source1-md5:	88b0dc6185079e60d83bdbaec92028b8
%define		mingw32_ver	5.4.2
#Source2Download: https://osdn.net/projects/mingw/releases/
Source2:	https://osdn.net/projects/mingw/downloads/74925/mingwrt-%{mingw32_ver}-mingw32-dev.tar.xz
# Source2-md5:	d8dceb05b85602eec82eac4e11d5c027
Source3:	gcc-optimize-la.pl
Patch100:	gcc-branch.diff
# Patch100-md5:	57034537c40d4d70828540f9c0bc2cf3
Patch0:		%{name}-buildsystem1.patch
Patch1:		%{name}-buildsystem2.patch
Patch2:		%{name}-lfs.patch
Patch3:		gcc-mingw32.patch
Patch4:		gcc-build-libvtv.patch
Patch5:		gcc-pthreads-w32.patch
URL:		https://gcc.gnu.org/
BuildRequires:	autoconf >= 2.64
BuildRequires:	automake >= 1:1.11.1
BuildRequires:	bison
BuildRequires:	crossmingw32-binutils >= 2.30
%{?with_pthreads:BuildRequires:	crossmingw32-pthreads-w32}
%if %{without bootstrap}
BuildRequires:	crossmingw32-runtime >= 1:5.4.2-3
BuildRequires:	crossmingw32-w32api >= 1:5.4.2-3
%endif
BuildRequires:	flex >= 2.5.4
%{?with_ada:BuildRequires:	gcc-ada}
BuildRequires:	gettext-tools >= 0.14.5
BuildRequires:	gmp-devel >= 4.3.2
BuildRequires:	isl-devel >= 0.15
BuildRequires:	libmpc-devel >= 0.8.1
BuildRequires:	libstdc++-devel
BuildRequires:	mpfr-devel >= 3.1.0
BuildRequires:	perl-tools-pod
BuildRequires:	tar >= 1:1.22
BuildRequires:	texinfo >= 4.7
BuildRequires:	xz
BuildRequires:	zlib-devel
BuildConflicts:	pdksh < 5.2.14-50
Requires:	crossmingw32-binutils >= 2.30
Requires:	gcc-dirs
Requires:	gmp >= 4.3.2
Requires:	isl >= 0.15
Requires:	libmpc >= 0.8.1
Requires:	mpfr >= 3.1.0
# java support dropped from gcc 7+
Obsoletes:	crossmingw32-java < 1:7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		target		i386-mingw32
%define		sysprefix	/usr
%define		archprefix	%{sysprefix}/%{target}
%define		archbindir	%{archprefix}/bin
%define		archincludedir	%{archprefix}/include
%define		archlibdir	%{archprefix}/lib
%define		gccarchdir	%{_libdir}/gcc/%{target}
%define		gcclibdir	%{gccarchdir}/%{version}
%define		_dlldir		/usr/share/wine/windows/system

%define		_noautostrip	.*/lib.*\\.a

%define		_enable_debug_packages 0

# functions with printf format attribute but with special parser and also
# receiving non constant format strings
%define		Werror_cflags	%{nil}
%define		_ssp_cflags	%{nil}
# -fPIC is not valid for target platform
%define		filterout_c	-fPIC

%description
crossmingw32 is a complete cross-compiling development system for
building stand-alone Microsoft Windows applications under Linux using
the MinGW32 build libraries. This includes a binutils, gcc with g++
and objc, and libstdc++, all cross targeted to i386-mingw32, along
with supporting Win32 libraries in 'coff' format from free sources.

This package contains cross targeted gcc.

%description -l de.UTF-8
Dieses Paket enthält einen Cross-gcc, der es erlaubt, auf einem
anderem Rechner Code für Win32 zu generieren.

%description -l pl.UTF-8
crossmingw32 jest kompletnym systemem do kompilacji skrośnej,
pozwalającym budować aplikacje MS Windows pod Linuksem używając
bibliotek MinGW32. System składa się z binutils, gcc z g++ i objc,
libstdc++ - wszystkie generujące kod dla platformy i386-mingw32, oraz
z bibliotek w formacie COFF.

Ten pakiet zawiera gcc generujące skrośnie kod dla Win32.

%package -n crossmingw32-libgcc-dll
Summary:	libgcc DLL library for Windows
Summary(pl.UTF-8):	Biblioteka DLL libgcc dla Windows
Group:		Applications/Emulators
Requires:	wine

%description -n crossmingw32-libgcc-dll
libgcc DLL library for Windows.

%description -n crossmingw32-libgcc-dll -l pl.UTF-8
Biblioteka DLL libgcc dla Windows.

%package -n crossmingw32-libatomic
Summary:	The GNU Atomic library - cross MinGW32 version
Summary(pl.UTF-8):	Biblioteka GNU Atomic - wersja skrośna MinGW32
License:	GPL v3+ with GCC Runtime Library Exception v3.1
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description -n crossmingw32-libatomic
This package contains cross MinGW32 version of the GNU Atomic library
which is a GCC support library for atomic operations not supported by
hardware.

%description -n crossmingw32-libatomic -l pl.UTF-8
Ten pakiet zawiera wersję skrośną MinGW32 biblioteki GNU Atomic,
będącej biblioteką GCC, wspierającej operacje atomowe na sprzęcie ich
nie obsługującym.

%package -n crossmingw32-libatomic-static
Summary:	The GNU Atomic static library - cross MinGW32 version
Summary(pl.UTF-8):	Statyczna biblioteka GNU Atomic - wersja skrośna MinGW32
License:	GPL v3+ with GCC Runtime Library Exception v3.1
Group:		Development/Libraries
Requires:	crossmingw32-libatomic = %{epoch}:%{version}-%{release}

%description -n crossmingw32-libatomic-static
The GNU Atomic static library - cross MinGW32 version.

%description -n crossmingw32-libatomic-static -l pl.UTF-8
Statyczna biblioteka GNU Atomic - wersja skrośna MinGW32.

%package -n crossmingw32-libatomic-dll
Summary:	DLL GNU Atomic library for Windows
Summary(pl.UTF-8):	Biblioteka DLL GNU Atomic dla Windows
License:	GPL v3+ with GCC Runtime Library Exception v3.1
Group:		Applications/Emulators
Requires:	wine

%description -n crossmingw32-libatomic-dll
DLL GNU Atomic library for Windows.

%description -n crossmingw32-libatomic-dll -l pl.UTF-8
Biblioteka DLL GNU Atomic dla Windows.

%package -n crossmingw32-libgomp
Summary:	GNU OpenMP library - cross MinGW32 version
Summary(pl.UTF-8):	Biblioteka GNU OpenMP - wersja skrośna MinGW32
License:	GPL v3+ with GCC Runtime Library Exception v3.1
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description -n crossmingw32-libgomp
This package contains cross MinGW32 version of GNU OpenMP library.

%description -n crossmingw32-libgomp -l pl.UTF-8
Ten pakiet zawiera wersję skrośną MinGW32 biblioteki GNU OpenMP.

%package -n crossmingw32-libgomp-static
Summary:	Static GNU OpenMP library - cross MinGW32 version
Summary(pl.UTF-8):	Statyczna biblioteka GNU OpenMP - wersja skrośna MinGW32
License:	GPL v3+ with GCC Runtime Library Exception v3.1
Group:		Development/Libraries
Requires:	crossmingw32-libgomp = %{epoch}:%{version}-%{release}

%description -n crossmingw32-libgomp-static
Static GNU OpenMP library - cross MinGW32 version.

%description -n crossmingw32-libgomp-static -l pl.UTF-8
Statyczna biblioteka GNU OpenMP - wersja skrośna MinGW32.

%package -n crossmingw32-libgomp-dll
Summary:	DLL GNU OpenMP library for Windows
Summary(pl.UTF-8):	Biblioteka DLL GNU OpenMP dla Windows
License:	GPL v3+ with GCC Runtime Library Exception v3.1
Group:		Applications/Emulators
Requires:	crossmingw32-libgcc-dll = %{epoch}:%{version}-%{release}
Requires:	crossmingw32-pthreads-w32-dll

%description -n crossmingw32-libgomp-dll
DLL GNU OpenMP library for Windows.

%description -n crossmingw32-libgomp-dll -l pl.UTF-8
Biblioteka DLL GNU OpenMP dla Windows.

%package -n crossmingw32-libvtv
Summary:	The Virtual Table Verification library - cross MinGW32 version
Summary(pl.UTF-8):	Biblioteka Virtual Table Verification do weryfikacji tablicy wirtualnej - wersja skrośna MinGW32
License:	GPL v3+ with GCC Runtime Library Exception v3.1
Group:		Development/Libraries
URL:		https://gcc.gnu.org/wiki/vtv
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description -n crossmingw32-libvtv
This package contains cross MinGW32 version of the Virtual Table
Verification library which is used for -fvtable-verify=...
instrumented programs.

%description -n crossmingw32-libvtv -l pl.UTF-8
Ten pakiet zawiera wersję skrośną MinGW32 biblioteki Virtual Table
Verification, służącej do weryfikacji tablicy wirtualnej w programach
kompilowanych z opcją -fvtable-verify=....

%package -n crossmingw32-libvtv-static
Summary:	The Virtual Table Verification static library - cross MinGW32 version
Summary(pl.UTF-8):	Statyczna biblioteka Virtual Table Verification - wersja skrośna MinGW32
License:	GPL v3+ with GCC Runtime Library Exception v3.1
Group:		Development/Libraries
URL:		https://gcc.gnu.org/wiki/vtv
Requires:	crossmingw32-libvtv = %{epoch}:%{version}-%{release}

%description -n crossmingw32-libvtv-static
The Virtual Table Verification static library - cross MinGW32 version.

%description -n crossmingw32-libvtv-static -l pl.UTF-8
Statyczna biblioteka Virtual Table Verification - wersja skrośna
MinGW32.

%package -n crossmingw32-libvtv-dll
Summary:	DLL Virtual Table Verification libraries for Windows
Summary(pl.UTF-8):	Biblioteki DLL Virtual Table Verification dla Windows
License:	GPL v3+ with GCC Runtime Library Exception v3.1
Group:		Applications/Emulators
URL:		https://gcc.gnu.org/wiki/vtv
Requires:	crossmingw32-libgcc-dll = %{epoch}:%{version}-%{release}

%description -n crossmingw32-libvtv-dll
DLL Virtual Table Verification libraries for Windows.

%description -n crossmingw32-libvtv-dll -l pl.UTF-8
Biblioteki DLL Virtual Table Verification dla Windows.

%package c++
Summary:	MinGW32 binary utility development utilities - g++
Summary(pl.UTF-8):	Zestaw narzędzi MinGW32 - g++
Group:		Development/Languages
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description c++
crossmingw32 is a complete cross-compiling development system for
building stand-alone Microsoft Windows applications under Linux using
the MinGW32 build libraries. This includes a binutils, gcc with g++
and objc, and libstdc++, all cross targeted to i386-mingw32, along
with supporting Win32 libraries in 'coff' format from free sources.

This package contains cross targeted g++ and (static) libstdc++.

%description c++ -l pl.UTF-8
crossmingw32 jest kompletnym systemem do kompilacji skrośnej,
pozwalającym budować aplikacje MS Windows pod Linuksem używając
bibliotek MinGW32. System składa się z binutils, gcc z g++ i objc,
libstdc++ - wszystkie generujące kod dla platformy i386-mingw32, oraz
z bibliotek w formacie COFF.

Ten pakiet zawiera g++ generujące kod pod Win32 oraz bibliotekę
libstdc++.

%package -n crossmingw32-libstdc++-static
Summary:	Static standard C++ library - cross MinGW32 version
Summary(pl.UTF-8):	Statyczna biblioteka standardowa C++ - wersja skrośna MinGW32
Group:		Development/Libraries
Requires:	%{name}-c++ = %{epoch}:%{version}-%{release}

%description -n crossmingw32-libstdc++-static
Static standard C++ library - cross MinGW32 version.

%description -n crossmingw32-libstdc++-static -l pl.UTF-8
Statyczna biblioteka standardowa C++ - wersja skrośna MinGW32.

%package -n crossmingw32-libstdc++-dll
Summary:	libstdc++ DLL library for Windows
Summary(pl.UTF-8):	Biblioteka DLL libstdc++ dla Windows
Group:		Applications/Emulators
Requires:	crossmingw32-libgcc-dll = %{epoch}:%{version}-%{release}
Requires:	wine

%description -n crossmingw32-libstdc++-dll
libstdc++ DLL library for Windows.

%description -n crossmingw32-libstdc++-dll -l pl.UTF-8
Biblioteka DLL libstdc++ dla Windows.

%package objc
Summary:	MinGW32 binary utility development utilities - objc
Summary(pl.UTF-8):	Zestaw narzędzi MinGW32 - objc
Group:		Development/Languages
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description objc
crossmingw32 is a complete cross-compiling development system for
building stand-alone Microsoft Windows applications under Linux using
the MinGW32 build libraries. This includes a binutils, gcc with g++
and objc, and libstdc++, all cross targeted to i386-mingw32, along
with supporting Win32 libraries in 'coff' format from free sources.

This package contains cross targeted objc compiler.

%description objc -l pl.UTF-8
crossmingw32 jest kompletnym systemem do kompilacji skrośnej,
pozwalającym budować aplikacje MS Windows pod Linuksem używając
bibliotek MinGW32. System składa się z binutils, gcc z g++ i objc,
libstdc++ - wszystkie generujące kod dla platformy i386-mingw32, oraz
z bibliotek w formacie COFF.

Ten pakiet zawiera kompilator objc generujący kod pod Win32.

%package objc++
Summary:	MinGW32 binary utility development utilities - objc++
Summary(pl.UTF-8):	Zestaw narzędzi MinGW32 - objc++
Group:		Development/Languages
Requires:	%{name}-objc = %{epoch}:%{version}-%{release}

%description objc++
crossmingw32 is a complete cross-compiling development system for
building stand-alone Microsoft Windows applications under Linux using
the MinGW32 build libraries. This includes a binutils, gcc with g++
and objc, and libstdc++, all cross targeted to i386-mingw32, along
with supporting Win32 libraries in 'coff' format from free sources.

This package contains Objective C++ support.

%description objc++ -l pl.UTF-8
crossmingw32 jest kompletnym systemem do kompilacji skrośnej,
pozwalającym budować aplikacje MS Windows pod Linuksem używając
bibliotek MinGW32. System składa się z binutils, gcc z g++ i objc,
libstdc++ - wszystkie generujące kod dla platformy i386-mingw32, oraz
z bibliotek w formacie COFF.

Ten pakiet zawiera obsługę języka Objective C++.

%package -n crossmingw32-libobjc-static
Summary:	Static Objective C library - cross MinGW32 version
Summary(pl.UTF-8):	Statyczna biblioteka Objective C - wersja skrośna MinGW32
Group:		Development/Libraries
Requires:	%{name}-objc = %{epoch}:%{version}-%{release}

%description -n crossmingw32-libobjc-static
Static Objective C library - cross MinGW32 version.

%description -n crossmingw32-libobjc-static -l pl.UTF-8
Statyczna biblioteka Objective C - wersja skrośna MinGW32.

%package -n crossmingw32-libobjc-dll
Summary:	libobjc DLL library for Windows
Summary(pl.UTF-8):	Biblioteka DLL libobjc dla Windows
Group:		Applications/Emulators
Requires:	crossmingw32-libgcc-dll = %{epoch}:%{version}-%{release}
Requires:	wine

%description -n crossmingw32-libobjc-dll
libobjc DLL library for Windows.

%description -n crossmingw32-libobjc-dll -l pl.UTF-8
Biblioteka DLL libobjc dla Windows.

%package d
Summary:	MinGW32 binary utility development utilities - D
Summary(pl.UTF-8):	Zestaw narzędzi MinGW32 - D
Group:		Development/Languages
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description d
crossmingw32 is a complete cross-compiling development system for
building stand-alone Microsoft Windows applications under Linux using
the MinGW32 build libraries. This includes a binutils, gcc with g++
and objc, and libstdc++, all cross targeted to i386-mingw32, along
with supporting Win32 libraries in 'coff' format from free sources.

This package contains cross targeted D compiler.

%description d -l pl.UTF-8
crossmingw32 jest kompletnym systemem do kompilacji skrośnej,
pozwalającym budować aplikacje MS Windows pod Linuksem używając
bibliotek MinGW32. System składa się z binutils, gcc z g++ i objc,
libstdc++ - wszystkie generujące kod dla platformy i386-mingw32, oraz
z bibliotek w formacie COFF.

Ten pakiet zawiera kompilator języka D generujący kod pod Win32.

%package fortran
Summary:	MinGW32 binary utility development utilities - Fortran
Summary(pl.UTF-8):	Zestaw narzędzi MinGW32 - Fortran
Group:		Development/Languages
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	crossmingw32-libquadmath = %{epoch}:%{version}-%{release}
Obsoletes:	crossmingw32-gcc-g77 < 1:4

%description fortran
crossmingw32 is a complete cross-compiling development system for
building stand-alone Microsoft Windows applications under Linux using
the MinGW32 build libraries. This includes a binutils, gcc with g++
and objc, and libstdc++, all cross targeted to i386-mingw32, along
with supporting Win32 libraries in 'coff' format from free sources.

This package contains cross targeted Fortran compiler.

%description fortran -l pl.UTF-8
crossmingw32 jest kompletnym systemem do kompilacji skrośnej,
pozwalającym budować aplikacje MS Windows pod Linuksem używając
bibliotek MinGW32. System składa się z binutils, gcc z g++ i objc,
libstdc++ - wszystkie generujące kod dla platformy i386-mingw32, oraz
z bibliotek w formacie COFF.

Ten pakiet zawiera kompilator Fortranu generujący kod pod Win32.

%package -n crossmingw32-libgfortran-static
Summary:	Static Fortran library - cross MinGW32 version
Summary(pl.UTF-8):	Statyczna biblioteka Fortranu - wersja skrośna MinGW32
Group:		Development/Libraries
Requires:	%{name}-fortran = %{epoch}:%{version}-%{release}

%description -n crossmingw32-libgfortran-static
Static Fortran library - cross MinGW32 version.

%description -n crossmingw32-libgfortran-static -l pl.UTF-8
Statyczna biblioteka Fortranu - wersja skrośna MinGW32.

%package -n crossmingw32-libgfortran-dll
Summary:	libgfortran DLL library for Windows
Summary(pl.UTF-8):	Biblioteka DLL libgfortran dla Windows
Group:		Applications/Emulators
Requires:	crossmingw32-libquadmath-dll

%description -n crossmingw32-libgfortran-dll
libgfortran DLL library for Windows.

%description -n crossmingw32-libgfortran-dll -l pl.UTF-8
Biblioteka DLL libgfortran dla Windows.

%package -n crossmingw32-libquadmath
Summary:	GCC __float128 support library - cross MinGW32 version
Summary(pl.UTF-8):	Biblioteka do obsługi typu __float128 - wersja skrośna MinGW32
License:	GPL v2+ with linking exception
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description -n crossmingw32-libquadmath
This package contains cross MinGW32 version of GCC support library
which is needed for __float128 math support and for Fortran REAL*16
support.

%description -n crossmingw32-libquadmath -l pl.UTF-8
Ten pakiet zawiera wersję skrośną MinGW32 biblioteki GCC do obsługi
operacji matematycznych na zmiennych typu __float128 oraz typu REAL*16
w Fortranie.

%package -n crossmingw32-libquadmath-static
Summary:	Static GCC __float128 support library - cross MinGW32 version
Summary(pl.UTF-8):	Biblioteka statyczna GCC do obsługi typu __float128 - wersja skrośna MinGW32
License:	GPL v2+ with linking exception
Group:		Development/Libraries
Requires:	crossmingw32-libquadmath = %{epoch}:%{version}-%{release}

%description -n crossmingw32-libquadmath-static
Static GCC __float128 support library - cross MinGW32 version.

%description -n crossmingw32-libquadmath-static -l pl.UTF-8
Biblioteka statyczna GCC do obsługi typu __float128 - wersja skrośna
MinGW32.

%package -n crossmingw32-libquadmath-dll
Summary:	DLL GCC __float128 support library for Windows
Summary(pl.UTF-8):	Biblioteka DLL GCC do obsługi typu __float128 dla Windows
License:	GPL v2+ with linking exception
Group:		Applications/Emulators
Requires:	wine

%description -n crossmingw32-libquadmath-dll
DLL GCC __float128 support library for Windows.

%description -n crossmingw32-libquadmath-dll -l pl.UTF-8
Biblioteka DLL GCC do obsługi typu __float128 dla Windows.

%prep
%setup -q -n gcc-%{version}
%patch -P100 -p1
%patch -P0 -p1
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p1
%patch -P5 -p1

%if %{with bootstrap}
# note: "winsup" dirs are special, handled by gcc's configure
install -d winsup/{mingw,w32api}
tar xf %{SOURCE1} -C winsup/w32api
tar xf %{SOURCE2} -C winsup/mingw
# required by _mingw.h
touch winsup/mingw/include/features.h
%endif

# override snapshot version.
echo %{version} > gcc/BASE-VER
echo "release" > gcc/DEV-PHASE

%build
cd libvtv
%{__aclocal} -I .. -I ../config
%{__autoconf}
%{__automake}
cd ..

rm -rf builddir && install -d builddir && cd builddir
%if %{with bootstrap}
install -d %{target}/winsup
ln -sf ../../../winsup/mingw/lib %{target}/winsup/mingw
ln -sf ../../../winsup/w32api %{target}/winsup/w32api
WINSUPDIR=$(cd ..; pwd)/winsup
%endif

# note: libbacktrace requires at least i486 now
CC="%{__cc}" \
CFLAGS="%{rpmcflags}" \
CXXFLAGS="%{rpmcxxflags}" \
TEXCONFIG=false \
CFLAGS_FOR_TARGET="-O2 -march=i486" \
CXXFLAGS_FOR_TARGET="-O2 -march=i486" \
../configure \
	--prefix=%{sysprefix} \
	--bindir=%{archbindir} \
	--libdir=%{_libdir} \
	--includedir=%{archincludedir} \
	--libexecdir=%{_libdir} \
	--infodir=%{_infodir} \
	--mandir=%{_mandir} \
	--with-bugurl="http://bugs.pld-linux.org" \
	--with-build-time-tools=%{archbindir} \
	%{!?with_bootstrap:--with-headers=%{archincludedir}} \
	--with-libs=%{!?with_bootstrap:%{archlibdir}}%{?with_bootstrap:${WINSUPDIR}/mingw/lib} \
	--with-demangler-in-ld \
	--with-dwarf2 \
	--with-gnu-as \
	--with-gnu-ld \
	--with-long-double-128 \
	--with-pkgversion="PLD-Linux" \
	--enable-c99 \
	--enable-fully-dynamic-string \
	--disable-isl-version-check \
	--enable-languages="c,c++%{!?with_bootstrap:,fortran,objc,obj-c++}%{?with_ada:,ada}%{?with_d:,d}" \
	%{?with_bootstrap:--disable-libatomic} \
	--disable-libcc1 \
	--enable-libgomp%{!?with_gomp:=no} \
	%{?with_bootstrap:--disable-libquadmath} \
	--disable-libssp \
	--enable-libstdcxx-allocator=new \
	%{?with_bootstrap:--disable-libvtv} \
	--enable-linker-build-id \
	--enable-long-long \
	--enable-lto \
	--disable-multilib \
	--disable-nls \
	--enable-shared \
	--disable-sjlj-exceptions \
	--disable-symvers \
	--enable-threads%{?with_pthreads:=posix} \
	--disable-werror \
	--disable-win32-registry \
	--target=%{target}

cd ..
%{__make} -C builddir all-host
patch -p1 <%{PATCH1}
%{__make} -C builddir

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

%{__make} -C builddir install \
	DESTDIR=$RPM_BUILD_ROOT

%{__mv} $RPM_BUILD_ROOT%{gcclibdir}/include-fixed/{limits,syslimits}.h $RPM_BUILD_ROOT%{gcclibdir}/include
%{__rm} -r $RPM_BUILD_ROOT%{gcclibdir}/include-fixed
%{__rm} -r $RPM_BUILD_ROOT%{gcclibdir}/install-tools

# these must be symlinks: gcclibdir is calculated relatively to real binary path
ln -sf %{archbindir}/%{target}-gcc $RPM_BUILD_ROOT%{_bindir}/%{target}-gcc
ln -sf %{archbindir}/%{target}-g++ $RPM_BUILD_ROOT%{_bindir}/%{target}-g++
ln -sf %{archbindir}/%{target}-cpp $RPM_BUILD_ROOT%{_bindir}/%{target}-cpp
ln -sf %{archbindir}/%{target}-gcov $RPM_BUILD_ROOT%{_bindir}/%{target}-gcov
ln -sf %{archbindir}/%{target}-gcov-dump $RPM_BUILD_ROOT%{_bindir}/%{target}-gcov-dump
ln -sf %{archbindir}/%{target}-gcov-tool $RPM_BUILD_ROOT%{_bindir}/%{target}-gcov-tool
ln -sf %{archbindir}/%{target}-lto-dump $RPM_BUILD_ROOT%{_bindir}/%{target}-lto-dump
%if %{without bootstrap}
ln -sf %{archbindir}/%{target}-gfortran $RPM_BUILD_ROOT%{_bindir}/%{target}-gfortran
%endif
%if %{with d}
ln -sf %{archbindir}/%{target}-gdc $RPM_BUILD_ROOT%{_bindir}/%{target}-gdc
%endif

# DLLs
install -d $RPM_BUILD_ROOT%{_dlldir}
%{__mv} $RPM_BUILD_ROOT%{archlibdir}/*.dll $RPM_BUILD_ROOT%{_dlldir}
if [ ! -f $RPM_BUILD_ROOT%{_dlldir}/libgcc_s_dw2-1.dll ]; then
	echo "libgcc DLL not installed?"
	install builddir/i386-mingw32/libgcc/shlib/libgcc_s_dw2-1.dll $RPM_BUILD_ROOT%{_dlldir}
fi

%if 0%{!?debug:1}
%{target}-strip --strip-unneeded -R.comment -R.note $RPM_BUILD_ROOT%{_dlldir}/*.dll
%{target}-strip -g -R.comment -R.note $RPM_BUILD_ROOT%{archlibdir}/lib*.a
%{target}-strip -g -R.comment -R.note $RPM_BUILD_ROOT%{gcclibdir}/lib*.a
%endif

# avoid -L poisoning in *.la
%if %{without bootstrap}
for f in libatomic.la libgfortran.la libobjc.la libquadmath.la %{?with_gomp:libgomp.la} ; do
	file="$RPM_BUILD_ROOT%{archlibdir}/$f"
	%{__perl} %{SOURCE3} "$file" %{gcclibdir} >"${file}.fixed"
	%{__mv} "${file}.fixed" "$file"
done
for f in libcaf_single.la ; do
	file="$RPM_BUILD_ROOT%{gcclibdir}/$f"
	%{__perl} %{SOURCE3} "$file" %{gcclibdir} >"${file}.fixed"
	%{__mv} "${file}.fixed" "$file"
done
%endif

# for pretty-printers see native gcc
%{__rm} $RPM_BUILD_ROOT%{archlibdir}/libstdc++.dll.a-gdb.py
%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/gcc-%{version}/python/libstdcxx
# no plugin development for mingw32 (at least for now)
%{__rm} $RPM_BUILD_ROOT%{gcclibdir}/liblto_plugin.la
%{__rm} -r $RPM_BUILD_ROOT%{gcclibdir}/plugin
# already in native gcc
%{__rm} -r $RPM_BUILD_ROOT%{_infodir}
# common FSF man pages
%{__rm} $RPM_BUILD_ROOT%{_mandir}/man7/{fsf-funding,gfdl,gpl}.7

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{target}-gcc
%attr(755,root,root) %{_bindir}/%{target}-cpp
%attr(755,root,root) %{_bindir}/%{target}-gcov
%attr(755,root,root) %{_bindir}/%{target}-gcov-dump
%attr(755,root,root) %{_bindir}/%{target}-gcov-tool
%attr(755,root,root) %{_bindir}/%{target}-lto-dump
%attr(755,root,root) %{archbindir}/%{target}-cpp
%attr(755,root,root) %{archbindir}/%{target}-gcc
%attr(755,root,root) %{archbindir}/%{target}-gcc-%{version}
%attr(755,root,root) %{archbindir}/%{target}-gcc-ar
%attr(755,root,root) %{archbindir}/%{target}-gcc-nm
%attr(755,root,root) %{archbindir}/%{target}-gcc-ranlib
%attr(755,root,root) %{archbindir}/%{target}-gcov
%attr(755,root,root) %{archbindir}/%{target}-gcov-dump
%attr(755,root,root) %{archbindir}/%{target}-gcov-tool
%attr(755,root,root) %{archbindir}/%{target}-lto-dump
%{archlibdir}/libgcc_s.a
%dir %{gccarchdir}
%dir %{gcclibdir}
%attr(755,root,root) %{gcclibdir}/cc1
%attr(755,root,root) %{gcclibdir}/collect2
%attr(755,root,root) %{gcclibdir}/lto-wrapper
%attr(755,root,root) %{gcclibdir}/lto1
%attr(755,root,root) %{gcclibdir}/liblto_plugin.so*
%{gcclibdir}/libgcc.a
%{gcclibdir}/libgcc_eh.a
%{gcclibdir}/libgcov.a
%{gcclibdir}/crtbegin.o
%{gcclibdir}/crtend.o
%{gcclibdir}/crtfastmath.o
%dir %{gcclibdir}/include
%{gcclibdir}/include/adxintrin.h
%{gcclibdir}/include/ammintrin.h
%{gcclibdir}/include/amxbf16intrin.h
%{gcclibdir}/include/amxint8intrin.h
%{gcclibdir}/include/amxtileintrin.h
%{gcclibdir}/include/avx2intrin.h
%{gcclibdir}/include/avx5124fmapsintrin.h
%{gcclibdir}/include/avx5124vnniwintrin.h
%{gcclibdir}/include/avx512bf16intrin.h
%{gcclibdir}/include/avx512bf16vlintrin.h
%{gcclibdir}/include/avx512bitalgintrin.h
%{gcclibdir}/include/avx512bwintrin.h
%{gcclibdir}/include/avx512cdintrin.h
%{gcclibdir}/include/avx512dqintrin.h
%{gcclibdir}/include/avx512erintrin.h
%{gcclibdir}/include/avx512fintrin.h
%{gcclibdir}/include/avx512fp16intrin.h
%{gcclibdir}/include/avx512fp16vlintrin.h
%{gcclibdir}/include/avx512ifmaintrin.h
%{gcclibdir}/include/avx512ifmavlintrin.h
%{gcclibdir}/include/avx512pfintrin.h
%{gcclibdir}/include/avx512vbmi2intrin.h
%{gcclibdir}/include/avx512vbmi2vlintrin.h
%{gcclibdir}/include/avx512vbmiintrin.h
%{gcclibdir}/include/avx512vbmivlintrin.h
%{gcclibdir}/include/avx512vlbwintrin.h
%{gcclibdir}/include/avx512vldqintrin.h
%{gcclibdir}/include/avx512vlintrin.h
%{gcclibdir}/include/avx512vnniintrin.h
%{gcclibdir}/include/avx512vnnivlintrin.h
%{gcclibdir}/include/avx512vp2intersectintrin.h
%{gcclibdir}/include/avx512vp2intersectvlintrin.h
%{gcclibdir}/include/avx512vpopcntdqintrin.h
%{gcclibdir}/include/avx512vpopcntdqvlintrin.h
%{gcclibdir}/include/avxintrin.h
%{gcclibdir}/include/avxvnniintrin.h
%{gcclibdir}/include/bmi2intrin.h
%{gcclibdir}/include/bmiintrin.h
%{gcclibdir}/include/bmmintrin.h
%{gcclibdir}/include/cet.h
%{gcclibdir}/include/cetintrin.h
%{gcclibdir}/include/cldemoteintrin.h
%{gcclibdir}/include/clflushoptintrin.h
%{gcclibdir}/include/clwbintrin.h
%{gcclibdir}/include/clzerointrin.h
%{gcclibdir}/include/cpuid.h
%{gcclibdir}/include/cross-stdarg.h
%{gcclibdir}/include/emmintrin.h
%{gcclibdir}/include/enqcmdintrin.h
%{gcclibdir}/include/f16cintrin.h
%{gcclibdir}/include/float.h
%{gcclibdir}/include/fma4intrin.h
%{gcclibdir}/include/fmaintrin.h
%{gcclibdir}/include/fxsrintrin.h
%{gcclibdir}/include/gcov.h
%{gcclibdir}/include/gfniintrin.h
%{gcclibdir}/include/hresetintrin.h
%{gcclibdir}/include/ia32intrin.h
%{gcclibdir}/include/immintrin.h
%{gcclibdir}/include/iso646.h
%{gcclibdir}/include/keylockerintrin.h
%{gcclibdir}/include/limits.h
%{gcclibdir}/include/lwpintrin.h
%{gcclibdir}/include/lzcntintrin.h
%{gcclibdir}/include/mm3dnow.h
%{gcclibdir}/include/mm_malloc.h
%{gcclibdir}/include/mmintrin.h
%{gcclibdir}/include/movdirintrin.h
%{gcclibdir}/include/mwaitintrin.h
%{gcclibdir}/include/mwaitxintrin.h
%{gcclibdir}/include/nmmintrin.h
%{gcclibdir}/include/pconfigintrin.h
%{gcclibdir}/include/pkuintrin.h
%{gcclibdir}/include/pmmintrin.h
%{gcclibdir}/include/popcntintrin.h
%{gcclibdir}/include/prfchwintrin.h
%{gcclibdir}/include/rdseedintrin.h
%{gcclibdir}/include/rtmintrin.h
%{gcclibdir}/include/serializeintrin.h
%{gcclibdir}/include/sgxintrin.h
%{gcclibdir}/include/shaintrin.h
%{gcclibdir}/include/smmintrin.h
%{gcclibdir}/include/stdalign.h
%{gcclibdir}/include/stdarg.h
%{gcclibdir}/include/stdatomic.h
%{gcclibdir}/include/stdbool.h
%{gcclibdir}/include/stddef.h
%{gcclibdir}/include/stdfix.h
%{gcclibdir}/include/stdint-gcc.h
%{gcclibdir}/include/stdint.h
%{gcclibdir}/include/stdnoreturn.h
%{gcclibdir}/include/syslimits.h
%{gcclibdir}/include/tbmintrin.h
%{gcclibdir}/include/tgmath.h
%{gcclibdir}/include/tmmintrin.h
%{gcclibdir}/include/tsxldtrkintrin.h
%{gcclibdir}/include/uintrintrin.h
%{gcclibdir}/include/unwind.h
%{gcclibdir}/include/vaesintrin.h
%{gcclibdir}/include/varargs.h
%{gcclibdir}/include/vpclmulqdqintrin.h
%{gcclibdir}/include/waitpkgintrin.h
%{gcclibdir}/include/wbnoinvdintrin.h
%{gcclibdir}/include/wmmintrin.h
%{gcclibdir}/include/x86gprintrin.h
%{gcclibdir}/include/x86intrin.h
%{gcclibdir}/include/xmmintrin.h
%{gcclibdir}/include/xopintrin.h
%{gcclibdir}/include/xsavecintrin.h
%{gcclibdir}/include/xsaveintrin.h
%{gcclibdir}/include/xsaveoptintrin.h
%{gcclibdir}/include/xsavesintrin.h
%{gcclibdir}/include/xtestintrin.h
%{_mandir}/man1/%{target}-cpp.1*
%{_mandir}/man1/%{target}-gcc.1*
%{_mandir}/man1/%{target}-gcov.1*
%{_mandir}/man1/%{target}-gcov-dump.1*
%{_mandir}/man1/%{target}-gcov-tool.1*
%{_mandir}/man1/%{target}-lto-dump.1*

%files -n crossmingw32-libgcc-dll
%defattr(644,root,root,755)
%{_dlldir}/libgcc_s_dw2-1.dll

%if %{without bootstrap}
%files -n crossmingw32-libatomic
%defattr(644,root,root,755)
%{archlibdir}/libatomic.dll.a
%{archlibdir}/libatomic.la

%files -n crossmingw32-libatomic-static
%defattr(644,root,root,755)
%{archlibdir}/libatomic.a

%files -n crossmingw32-libatomic-dll
%defattr(644,root,root,755)
%{_dlldir}/libatomic-1.dll
%endif

%if %{with gomp}
%files -n crossmingw32-libgomp
%defattr(644,root,root,755)
%{archlibdir}/libgomp.dll.a
%{archlibdir}/libgomp.la
%{archlibdir}/libgomp.spec
%{gcclibdir}/include/acc_prof.h
%{gcclibdir}/include/omp.h
%{gcclibdir}/include/openacc.h

%files -n crossmingw32-libgomp-static
%defattr(644,root,root,755)
%{archlibdir}/libgomp.a

%files -n crossmingw32-libgomp-dll
%defattr(644,root,root,755)
%{_dlldir}/libgomp-1.dll
%endif

%if %{without bootstrap}
%files -n crossmingw32-libvtv
%defattr(644,root,root,755)
%{archlibdir}/libvtv.dll.a
%{archlibdir}/libvtv.la
%{archlibdir}/libvtv_stubs.dll.a
%{archlibdir}/libvtv_stubs.la

%files -n crossmingw32-libvtv-static
%defattr(644,root,root,755)
%{archlibdir}/libvtv.a
%{archlibdir}/libvtv_stubs.a

%files -n crossmingw32-libvtv-dll
%defattr(644,root,root,755)
%{_dlldir}/libvtv-0.dll
%{_dlldir}/libvtv_stubs-0.dll
%endif

%files c++
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{target}-g++
%attr(755,root,root) %{archbindir}/%{target}-c++
%attr(755,root,root) %{archbindir}/%{target}-g++
%attr(755,root,root) %{gcclibdir}/cc1plus
%attr(755,root,root) %{gcclibdir}/g++-mapper-server
%{archlibdir}/libstdc++.dll.a
%{archlibdir}/libstdc++.la
%{archlibdir}/libstdc++fs.a
%{archlibdir}/libstdc++fs.la
%{archlibdir}/libsupc++.la
%{archlibdir}/libsupc++.a
%{archincludedir}/c++
%{_mandir}/man1/%{target}-g++.1*

%files -n crossmingw32-libstdc++-static
%defattr(644,root,root,755)
%{archlibdir}/libstdc++.a

%files -n crossmingw32-libstdc++-dll
%defattr(644,root,root,755)
%{_dlldir}/libstdc++-6.dll

%if %{without bootstrap}
%files objc
%defattr(644,root,root,755)
%doc libobjc/README
%attr(755,root,root) %{gcclibdir}/cc1obj
%{archlibdir}/libobjc.dll.a
%{archlibdir}/libobjc.la
%{gcclibdir}/include/objc

%files objc++
%defattr(644,root,root,755)
%doc gcc/objcp/ChangeLog
%attr(755,root,root) %{gcclibdir}/cc1objplus

%files -n crossmingw32-libobjc-static
%defattr(644,root,root,755)
%{archlibdir}/libobjc.a

%files -n crossmingw32-libobjc-dll
%defattr(644,root,root,755)
%{_dlldir}/libobjc-4.dll

%if %{with d}
%files d
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{target}-gdc
%attr(755,root,root) %{archbindir}/%{target}-gdc
%attr(755,root,root) %{gcclibdir}/d21
%{_mandir}/man1/%{target}-gdc.1*
%endif

%files fortran
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{target}-gfortran
%attr(755,root,root) %{archbindir}/%{target}-gfortran
%attr(755,root,root) %{gcclibdir}/f951
%{archlibdir}/libgfortran.dll.a
%{archlibdir}/libgfortran.la
%{archlibdir}/libgfortran.spec
%{gcclibdir}/finclude
%{gcclibdir}/include/ISO_Fortran_binding.h
%{gcclibdir}/libcaf_single.a
%{gcclibdir}/libcaf_single.la
%{_mandir}/man1/%{target}-gfortran.1*

%files -n crossmingw32-libgfortran-static
%defattr(644,root,root,755)
%{archlibdir}/libgfortran.a

%files -n crossmingw32-libgfortran-dll
%defattr(644,root,root,755)
%{_dlldir}/libgfortran-5.dll

%files -n crossmingw32-libquadmath
%defattr(644,root,root,755)
%{archlibdir}/libquadmath.dll.a
%{archlibdir}/libquadmath.la
%{gcclibdir}/include/quadmath.h
%{gcclibdir}/include/quadmath_weak.h

%files -n crossmingw32-libquadmath-static
%defattr(644,root,root,755)
%{archlibdir}/libquadmath.a

%files -n crossmingw32-libquadmath-dll
%defattr(644,root,root,755)
%{_dlldir}/libquadmath-0.dll
%endif
