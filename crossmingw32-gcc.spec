#
# Conditional build:
%bcond_with	bootstrap	# bootstrap build (using binary w32api/mingwrt, no gomp)
%bcond_without	gomp		# OpenMP libraries
#
%if %{with bootstrap}
%undefine	with_gomp
%endif
Summary:	Cross MinGW32 GNU binary utility development utilities - gcc
Summary(es.UTF-8):	Utilitarios para desarrollo de binarios de la GNU - MinGW32 gcc
Summary(fr.UTF-8):	Utilitaires de développement binaire de GNU - MinGW32 gcc
Summary(pl.UTF-8):	Skrośne narzędzia programistyczne GNU dla MinGW32 - gcc
Summary(pt_BR.UTF-8):	Utilitários para desenvolvimento de binários da GNU - MinGW32 gcc
Summary(tr.UTF-8):	GNU geliştirme araçları - MinGW32 gcc
Name:		crossmingw32-gcc
Version:	4.9.3
Release:	3
Epoch:		1
License:	GPL v3+
Group:		Development/Languages
Source0:	https://ftp.gnu.org/gnu/gcc/gcc-%{version}/gcc-%{version}.tar.bz2
# Source0-md5:	6f831b4d251872736e8e9cc09746f327
%define		mingw32_ver	4.0.3
Source1:	http://downloads.sourceforge.net/mingw/mingwrt-%{mingw32_ver}-1-mingw32-dev.tar.lzma
# Source1-md5:	c2c9aa82e0cb47abac01760525684858
Source2:	gcc-optimize-la.pl
# svn diff -x --ignore-eol-style --force svn://gcc.gnu.org/svn/gcc/tags/gcc_4_9_3_release svn://gcc.gnu.org/svn/gcc/branches/gcc-4_9-branch > gcc-branch.diff
Patch100:	gcc-branch.diff
# Patch100-md5:	253cbf4cc2f71d9c9362f4a3be25bb17
Patch0:		%{name}-buildsystem1.patch
Patch1:		%{name}-buildsystem2.patch
Patch2:		%{name}-lfs.patch
Patch12:	gcc-isl0.15-1.patch
Patch13:	gcc-isl0.15-2.patch
URL:		http://gcc.gnu.org/
BuildRequires:	autoconf >= 2.64
BuildRequires:	automake >= 1:1.9.3
BuildRequires:	bison
BuildRequires:	crossmingw32-binutils >= 2.15.91.0.2-2
%{?with_gomp:BuildRequires:	crossmingw32-pthreads-w32}
%if %{without bootstrap}
BuildRequires:	crossmingw32-runtime >= 3.5
BuildRequires:	crossmingw32-w32api >= 3.1
%endif
BuildRequires:	cloog-isl-devel >= 0.17.0
BuildRequires:	cloog-isl-devel < 0.19
BuildRequires:	flex
BuildRequires:	gmp-devel >= 4.1
BuildRequires:	isl-devel >= 0.13
BuildRequires:	libmpc-devel
BuildRequires:	mpfr-devel
BuildRequires:	perl-tools-pod
BuildRequires:	texinfo >= 4.2
%if %{with booststrap}
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
%endif
Requires:	crossmingw32-binutils >= 2.15.91.0.2-2
Requires:	gcc-dirs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		target		i386-mingw32
%define		sysprefix	/usr
%define		arch		%{sysprefix}/%{target}
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
Group:		Development/Libraries
Requires:	crossmingw32-libgcc-dll = %{epoch}:%{version}-%{release}
Requires:	crossmingw32-pthreads-w32-dll

%description -n crossmingw32-libgomp-dll
DLL GNU OpenMP library for Windows.

%description -n crossmingw32-libgomp-dll -l pl.UTF-8
Biblioteka DLL GNU OpenMP dla Windows.

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

%package fortran
Summary:	MinGW32 binary utility development utilities - Fortran
Summary(pl.UTF-8):	Zestaw narzędzi MinGW32 - Fortran
Group:		Development/Languages
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	crossmingw32-libquadmath = %{epoch}:%{version}-%{release}
Obsoletes:	crossmingw32-gcc-g77

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

%package java
Summary:	MinGW32 binary utility development utilities - Java
Summary(pl.UTF-8):	Zestaw narzędzi MinGW32 - Java
Group:		Development/Languages
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description java
crossmingw32 is a complete cross-compiling development system for
building stand-alone Microsoft Windows applications under Linux using
the MinGW32 build libraries. This includes a binutils, gcc with g++
and objc, and libstdc++, all cross targeted to i386-mingw32, along
with supporting Win32 libraries in 'coff' format from free sources.

This package contains cross targeted Java compiler.

%description java -l pl.UTF-8
crossmingw32 jest kompletnym systemem do kompilacji skrośnej,
pozwalającym budować aplikacje MS Windows pod Linuksem używając
bibliotek MinGW32. System składa się z binutils, gcc z g++ i objc,
libstdc++ - wszystkie generujące kod dla platformy i386-mingw32, oraz
z bibliotek w formacie COFF.

Ten pakiet zawiera kompilator Javy generujący kod pod Win32.

%prep
%setup -q -n gcc-%{version}
%patch100 -p0
%patch0 -p1
%patch2 -p1
%patch12 -p1
%patch13 -p1

%if %{with bootstrap}
# note: "winsup" dir is special, handled by gcc's configure
install -d winsup/mingw
tar xf %{SOURCE1} -C winsup/mingw
%endif

# override snapshot version.
echo %{version} > gcc/BASE-VER
echo "release" > gcc/DEV-PHASE

%build
rm -rf builddir && install -d builddir && cd builddir
%if %{with bootstrap}
install -d %{target}/winsup
ln -sf ../../../winsup/mingw/lib %{target}/winsup/mingw
ln -sf ../../../winsup/mingw/include %{target}/winsup/w32api
WINSUPDIR=$(cd ..; pwd)/winsup
%endif

CC="%{__cc}" \
CFLAGS="%{rpmcflags}" \
CXXFLAGS="%{rpmcxxflags}" \
TEXCONFIG=false \
../configure \
	--prefix=%{sysprefix} \
	--bindir=%{arch}/bin \
	--libdir=%{_libdir} \
	--includedir=%{arch}/include \
	--libexecdir=%{_libdir} \
	--infodir=%{_infodir} \
	--mandir=%{_mandir} \
	--with-build-time-tools=%{arch}/bin \
	%{!?with_bootstrap:--with-headers=%{arch}/include} \
	--with-libs=%{!?with_bootstrap:%{arch}/lib}%{?with_bootstrap:${WINSUPDIR}/mingw/lib} \
	--with-dwarf2 \
	--with-gnu-as \
	--with-gnu-ld \
	--with-mangler-in-ld \
	--with-long-double-128 \
	--with-cloog \
	--with-ppl \
	--disable-isl-version-check \
	--enable-shared \
	--enable-threads \
	--enable-languages="c,c++,fortran,java,objc" \
	--enable-c99 \
	--enable-fully-dynamic-string \
	--enable-libgomp \
	--enable-libstdcxx-allocator=new \
	--enable-long-long \
	--enable-version-specific-runtime-libs \
	--disable-libssp \
	--disable-multilib \
	--disable-nls \
	--disable-sjlj-exceptions \
	--disable-symvers \
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

mv $RPM_BUILD_ROOT%{gcclibdir}/include-fixed/{limits,syslimits}.h $RPM_BUILD_ROOT%{gcclibdir}/include
%{__rm} -r $RPM_BUILD_ROOT%{gcclibdir}/include-fixed
%{__rm} -r $RPM_BUILD_ROOT%{gcclibdir}/install-tools

# these must be symlinks: gcclibdir is calculated relatively to real binary path
ln -sf %{arch}/bin/%{target}-gcc $RPM_BUILD_ROOT%{_bindir}/%{target}-gcc
ln -sf %{arch}/bin/%{target}-g++ $RPM_BUILD_ROOT%{_bindir}/%{target}-g++
ln -sf %{arch}/bin/%{target}-cpp $RPM_BUILD_ROOT%{_bindir}/%{target}-cpp
ln -sf %{arch}/bin/%{target}-gcov $RPM_BUILD_ROOT%{_bindir}/%{target}-gcov
ln -sf %{arch}/bin/%{target}-gcj $RPM_BUILD_ROOT%{_bindir}/%{target}-gcj
ln -sf %{arch}/bin/%{target}-jcf-dump $RPM_BUILD_ROOT%{_bindir}/%{target}-jcf-dump
ln -sf %{arch}/bin/%{target}-gfortran $RPM_BUILD_ROOT%{_bindir}/%{target}-gfortran

# DLLs
install -d $RPM_BUILD_ROOT%{_dlldir}
mv -f $RPM_BUILD_ROOT%{gccarchdir}/*.dll $RPM_BUILD_ROOT%{_dlldir}
mv -f $RPM_BUILD_ROOT%{gcclibdir}/*.dll $RPM_BUILD_ROOT%{_dlldir}
if [ ! -f $RPM_BUILD_ROOT%{_dlldir}/libgcc_s_dw2-1.dll ]; then
	echo "libgcc DLL not installed?"
	install builddir/i386-mingw32/libgcc/shlib/libgcc_s_dw2-1.dll $RPM_BUILD_ROOT%{_dlldir}
fi

%if 0%{!?debug:1}
%{target}-strip --strip-unneeded -R.comment -R.note $RPM_BUILD_ROOT%{_dlldir}/*.dll
%{target}-strip -g -R.comment -R.note $RPM_BUILD_ROOT%{gcclibdir}/lib*.a
%endif

# avoid -L poisoning in *.la
for f in libcaf_single.la libgfortran.la libgfortranbegin.la libobjc.la libquadmath.la %{?with_gomp:libgomp.la} ; do
	file="$RPM_BUILD_ROOT%{gcclibdir}/$f"
	%{__perl} %{SOURCE2} "$file" %{gcclibdir} >"${file}.fixed"
	%{__mv} "${file}.fixed" "$file"
done

# for pretty-printers see native gcc
%{__rm} $RPM_BUILD_ROOT%{gcclibdir}/libstdc++.dll.a-gdb.py
%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/gcc-%{version}/python/libstdcxx
# no plugin development for mingw32 (at least for now)
%{__rm} $RPM_BUILD_ROOT%{gcclibdir}/liblto_plugin.la
%{__rm} -r $RPM_BUILD_ROOT%{gcclibdir}/plugin
# already in native gcc
%{__rm} -r $RPM_BUILD_ROOT%{_infodir}
# common FSF man pages
%{__rm} $RPM_BUILD_ROOT%{_mandir}/man7/{fsf-funding,gfdl,gpl}.7
# programs not packaged
%{__rm} $RPM_BUILD_ROOT%{_mandir}/man1/%{target}-{aot-compile,gc-analyze,gcj-dbtool,gij,grmic,jv-convert,rebuild-gcj-db}.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{target}-gcc
%attr(755,root,root) %{_bindir}/%{target}-cpp
%attr(755,root,root) %{_bindir}/%{target}-gcov
%attr(755,root,root) %{arch}/bin/%{target}-gcc
%attr(755,root,root) %{arch}/bin/%{target}-gcc-%{version}
%attr(755,root,root) %{arch}/bin/%{target}-gcc-ar
%attr(755,root,root) %{arch}/bin/%{target}-gcc-nm
%attr(755,root,root) %{arch}/bin/%{target}-gcc-ranlib
%attr(755,root,root) %{arch}/bin/%{target}-cpp
%attr(755,root,root) %{arch}/bin/%{target}-gcov
%dir %{gccarchdir}
%dir %{gcclibdir}
%attr(755,root,root) %{gcclibdir}/cc1
%attr(755,root,root) %{gcclibdir}/collect2
%attr(755,root,root) %{gcclibdir}/lto-wrapper
%attr(755,root,root) %{gcclibdir}/lto1
%attr(755,root,root) %{gcclibdir}/liblto_plugin.so*
%{gcclibdir}/libgcc.a
%{gcclibdir}/libgcc_eh.a
%{gcclibdir}/libgcc_s.a
%{gcclibdir}/libgcov.a
%{gcclibdir}/crtbegin.o
%{gcclibdir}/crtend.o
%{gcclibdir}/crtfastmath.o
%dir %{gcclibdir}/include
%{gcclibdir}/include/*.h
%{_mandir}/man1/%{target}-cpp.1*
%{_mandir}/man1/%{target}-gcc.1*
%{_mandir}/man1/%{target}-gcov.1*

%files -n crossmingw32-libgcc-dll
%defattr(644,root,root,755)
%{_dlldir}/libgcc_s_dw2-1.dll

%if %{with gomp}
%files -n crossmingw32-libgomp
%defattr(644,root,root,755)
%{gcclibdir}/libgomp.dll.a
%{gcclibdir}/libgomp.la
%{gcclibdir}/libgomp.spec

%files -n crossmingw32-libgomp-static
%defattr(644,root,root,755)
%{gcclibdir}/libgomp.a

%files -n crossmingw32-libgomp-dll
%defattr(644,root,root,755)
%{_dlldir}/libgomp-1.dll
%endif

%files c++
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{target}-g++
%attr(755,root,root) %{arch}/bin/%{target}-c++
%attr(755,root,root) %{arch}/bin/%{target}-g++
%attr(755,root,root) %{gcclibdir}/cc1plus
%{gcclibdir}/libstdc++.dll.a
%{gcclibdir}/libstdc++.la
%{gcclibdir}/libsupc++.la
%{gcclibdir}/libsupc++.a
%{gcclibdir}/include/c++
%{_mandir}/man1/%{target}-g++.1*

%files -n crossmingw32-libstdc++-static
%defattr(644,root,root,755)
%{gcclibdir}/libstdc++.a

%files -n crossmingw32-libstdc++-dll
%defattr(644,root,root,755)
%{_dlldir}/libstdc++-6.dll

%files objc
%defattr(644,root,root,755)
%attr(755,root,root) %{gcclibdir}/cc1obj
%{gcclibdir}/libobjc.dll.a
%{gcclibdir}/libobjc.la
%{gcclibdir}/include/objc

%files -n crossmingw32-libobjc-static
%defattr(644,root,root,755)
%{gcclibdir}/libobjc.a

%files -n crossmingw32-libobjc-dll
%defattr(644,root,root,755)
%{_dlldir}/libobjc-4.dll

%files fortran
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{target}-gfortran
%attr(755,root,root) %{arch}/bin/%{target}-gfortran
%attr(755,root,root) %{gcclibdir}/f951
%{gcclibdir}/finclude
%{gcclibdir}/libcaf_single.a
%{gcclibdir}/libcaf_single.la
%{gcclibdir}/libgfortran.dll.a
%{gcclibdir}/libgfortran.la
%{gcclibdir}/libgfortran.spec
%{gcclibdir}/libgfortranbegin.a
%{gcclibdir}/libgfortranbegin.la
%{_mandir}/man1/%{target}-gfortran.1*

%files -n crossmingw32-libgfortran-static
%defattr(644,root,root,755)
%{gcclibdir}/libgfortran.a

%files -n crossmingw32-libgfortran-dll
%defattr(644,root,root,755)
%{_dlldir}/libgfortran-3.dll

%files -n crossmingw32-libquadmath
%defattr(644,root,root,755)
%{gcclibdir}/libquadmath.dll.a
%{gcclibdir}/libquadmath.la

%files -n crossmingw32-libquadmath-static
%defattr(644,root,root,755)
%{gcclibdir}/libquadmath.a

%files -n crossmingw32-libquadmath-dll
%defattr(644,root,root,755)
%{_dlldir}/libquadmath-0.dll

%files java
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{target}-gcj
%attr(755,root,root) %{_bindir}/%{target}-jcf-dump
%attr(755,root,root) %{arch}/bin/%{target}-gcj
%attr(755,root,root) %{arch}/bin/%{target}-jcf-dump
%attr(755,root,root) %{gcclibdir}/jc1
%attr(755,root,root) %{gcclibdir}/jvgenmain
%{_mandir}/man1/%{target}-gcj.1*
%{_mandir}/man1/%{target}-jcf-dump.1*
