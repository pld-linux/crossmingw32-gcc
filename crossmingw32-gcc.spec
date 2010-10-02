#
# TODO:
# - restore languages other than c, c++
# - openmp
#
# Conditional build:
%bcond_with	bootstrap	# bootstrap build (using binary w32api/mingwrt)
#
Summary:	Cross MinGW32 GNU binary utility development utilities - gcc
Summary(es.UTF-8):	Utilitarios para desarrollo de binarios de la GNU - MinGW32 gcc
Summary(fr.UTF-8):	Utilitaires de développement binaire de GNU - MinGW32 gcc
Summary(pl.UTF-8):	Skrośne narzędzia programistyczne GNU dla MinGW32 - gcc
Summary(pt_BR.UTF-8):	Utilitários para desenvolvimento de binários da GNU - MinGW32 gcc
Summary(tr.UTF-8):	GNU geliştirme araçları - MinGW32 gcc
Name:		crossmingw32-gcc
Version:	4.5.1
Release:	1
Epoch:		1
License:	GPL v3+
Group:		Development/Languages
Source0:	ftp://gcc.gnu.org/pub/gcc/releases/gcc-%{version}/gcc-%{version}.tar.bz2
# Source0-md5:	48231a8e33ed6e058a341c53b819de1a
%define		apiver	3.15
Source1:	http://downloads.sourceforge.net/mingw/w32api-%{apiver}-1-mingw32-dev.tar.lzma
# Source1-md5:	efcbcadd0299a6413d95b9ce919ede9f
%define		runver	3.18
Source2:	http://downloads.sourceforge.net/mingw/mingwrt-%{runver}-mingw32-dev.tar.gz
# Source2-md5:	e49803d8c14b1ffa6e24e5b5fee31a3d
# svn diff -x --ignore-eol-style svn://gcc.gnu.org/svn/gcc/tags/gcc_4_5_1_release svn://gcc.gnu.org/svn/gcc/branches/gcc-4_5-branch > gcc-branch.diff
Patch100:	gcc-branch.diff
Patch0:		%{name}-buildsystem1.patch
Patch1:		%{name}-buildsystem2.patch
Patch2:		%{name}-lfs.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	crossmingw32-binutils >= 2.15.91.0.2-2
BuildRequires:	flex
BuildRequires:	libmpc-devel
%if %{without bootstrap}
BuildRequires:	crossmingw32-runtime >= 3.5
BuildRequires:	crossmingw32-w32api >= 3.1
%endif
BuildRequires:	mpfr-devel
BuildRequires:	texinfo >= 4.2
%if %{with booststrap}
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
%endif
Requires:	crossmingw32-binutils >= 2.15.91.0.2-2
Requires:	gcc-dirs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		target		i386-mingw32
%define		arch		%{_prefix}/%{target}
%define		gccarchdir	%{_libdir}/gcc/%{target}
%define		gcclibdir	%{gccarchdir}/%{version}
%define		_dlldir		/usr/share/wine/windows/system

%define		_noautostrip	.*/lib.*\\.a

%define		_enable_debug_packages 0

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

# does this even work?
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

# does this even work?
%package fortran
Summary:	MinGW32 binary utility development utilities - Fortran
Summary(pl.UTF-8):	Zestaw narzędzi MinGW32 - Fortran
Group:		Development/Languages
Requires:	%{name} = %{epoch}:%{version}-%{release}
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

# does this even work?
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

%if %{with bootstrap}
# note: "winsup" dirs below are special, handled by gcc's configure
install -d winsup/{mingw,w32api}
tar xf %{SOURCE1} -C winsup/w32api
tar xf %{SOURCE2} -C winsup/mingw
%endif

# override snapshot version.
echo %{version} > gcc/BASE-VER
echo "release" > gcc/DEV-PHASE

%build
rm -rf builddir && install -d builddir && cd builddir
%if %{with bootstrap}
install -d %{target}/winsup
# sysroot/%{target}/lib
ln -sf ../../../winsup/mingw/lib %{target}/winsup/mingw
ln -sf ../../../winsup/w32api %{target}/winsup/w32api
WINSUPDIR=$(cd ..; pwd)/winsup
%endif

CC="%{__cc}" \
CFLAGS="%{rpmcflags}" \
CXXFLAGS="%{rpmcxxflags}" \
TEXCONFIG=false \
../configure \
	--prefix=%{arch} \
	--libdir=%{_libdir} \
	--libexecdir=%{_libdir} \
	--infodir=%{_infodir} \
	--mandir=%{_mandir} \
	%{!?with_bootstrap:--with-headers=%{arch}/include} \
	--with-libs=%{!?with_bootstrap:%{arch}/lib}%{?with_bootstrap:${WINSUPDIR}/mingw/lib} \
	--with-build-time-tools=%{arch}/bin \
	--with-dwarf2 \
	--with-gnu-as \
	--with-gnu-ld \
	--with-mangler-in-ld \
	--with-long-double-128 \
	--enable-threads \
	--enable-languages="c,c++" \
	--enable-c99 \
	--enable-long-long \
	--enable-fully-dynamic-string \
	--enable-libstdcxx-allocator=new \
	--enable-version-specific-runtime-libs \
	--enable-shared \
	--disable-nls \
	--disable-symvers \
	--disable-sjlj-exceptions \
	--disable-win32-registry \
	--disable-multilib \
	--disable-libssp \
	--target=%{target}
# ,fortran,java,objc

cd ..
%{__make} -C builddir all-host
patch -p1 <%{PATCH1}
%{__make} -C builddir

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

%{__make} -C builddir install \
	DESTDIR=$RPM_BUILD_ROOT

# host (ELF) library
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libiberty.a

# cross library - strange path
install -d $RPM_BUILD_ROOT%{arch}/lib
mv -f $RPM_BUILD_ROOT%{arch}/%{target}/lib/libiberty.a $RPM_BUILD_ROOT%{arch}/lib

mv $RPM_BUILD_ROOT%{gcclibdir}/include-fixed/{limits,syslimits}.h $RPM_BUILD_ROOT%{gcclibdir}/include
%{__rm} -r $RPM_BUILD_ROOT%{gcclibdir}/include-fixed
%{__rm} -r $RPM_BUILD_ROOT%{gcclibdir}/install-tools

# restore hardlinks
ln -f $RPM_BUILD_ROOT%{arch}/bin/%{target}-gcc $RPM_BUILD_ROOT%{_bindir}/%{target}-gcc
ln -f $RPM_BUILD_ROOT%{arch}/bin/%{target}-g++ $RPM_BUILD_ROOT%{_bindir}/%{target}-g++
ln -f $RPM_BUILD_ROOT%{arch}/bin/%{target}-cpp $RPM_BUILD_ROOT%{_bindir}/%{target}-cpp
ln -f $RPM_BUILD_ROOT%{arch}/bin/%{target}-gcov $RPM_BUILD_ROOT%{_bindir}/%{target}-gcov

# DLLs
install -d $RPM_BUILD_ROOT%{_dlldir}
mv -f $RPM_BUILD_ROOT%{arch}/bin/libstdc++-6.dll $RPM_BUILD_ROOT%{_dlldir}
install builddir/i386-mingw32/libgcc/shlib/libgcc_s_dw2-1.dll $RPM_BUILD_ROOT%{_dlldir}

%if 0%{!?debug:1}
%{target}-strip --strip-unneeded -R.comment -R.note $RPM_BUILD_ROOT%{_dlldir}/*.dll
%{target}-strip -g -R.comment -R.note $RPM_BUILD_ROOT%{gcclibdir}/lib*.a \
	$RPM_BUILD_ROOT%{arch}/lib/lib*.a
%endif

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
%attr(755,root,root) %{arch}/bin/%{target}-gcc
%attr(755,root,root) %{arch}/bin/%{target}-gcc-%{version}
%attr(755,root,root) %{arch}/bin/%{target}-gccbug
%attr(755,root,root) %{arch}/bin/%{target}-cpp
%attr(755,root,root) %{arch}/bin/%{target}-gcov
%{arch}/lib/libiberty.a
%dir %{gccarchdir}
%dir %{gcclibdir}
%attr(755,root,root) %{gcclibdir}/cc1
%attr(755,root,root) %{gcclibdir}/collect2
%attr(755,root,root) %{gcclibdir}/lto-wrapper
%{gcclibdir}/libgcc.a
%{gcclibdir}/libgcc_eh.a
%{gcclibdir}/libgcc_s.a
%{gcclibdir}/libgcov.a
%dir %{gcclibdir}/include
%{gcclibdir}/include/*.h
%{_mandir}/man1/%{target}-cpp.1*
%{_mandir}/man1/%{target}-gcc.1*
%{_mandir}/man1/%{target}-gcov.1*

%files -n crossmingw32-libgcc-dll
%defattr(644,root,root,755)
%{_dlldir}/libgcc_s_dw2-1.dll

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
%{gcclibdir}/crtbegin.o
%{gcclibdir}/crtend.o
%{gcclibdir}/crtfastmath.o
%{gcclibdir}/include/c++
%{_mandir}/man1/%{target}-g++.1*

%files -n crossmingw32-libstdc++-static
%defattr(644,root,root,755)
%{gcclibdir}/libstdc++.a

%files -n crossmingw32-libstdc++-dll
%defattr(644,root,root,755)
%{_dlldir}/libstdc++-6.dll

# no obj-c, fortran, java for the moment
%if 0
%files objc
%defattr(644,root,root,755)
%attr(755,root,root) %{gcclib}/cc1obj
%{arch}/lib/libobjc.a
%{arch}/lib/libobjc.la

%files fortran
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{target}-gfortran
%attr(755,root,root) %{arch}/bin/gfortran
%attr(755,root,root) %{gcclib}/f951
%{arch}/lib/libgfortran.a
%{arch}/lib/libgfortran.la
%{arch}/lib/libgfortranbegin.a
%{arch}/lib/libgfortranbegin.la
%{_mandir}/man1/%{target}-gfortran.1*

%files java
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{target}-gcj
%attr(755,root,root) %{_bindir}/%{target}-gcjh
%attr(755,root,root) %{_bindir}/%{target}-gjnih
%attr(755,root,root) %{_bindir}/%{target}-grepjar
%attr(755,root,root) %{_bindir}/%{target}-fastjar
%attr(755,root,root) %{_bindir}/%{target}-jcf-dump
%attr(755,root,root) %{_bindir}/%{target}-jv-scan
#%attr(755,root,root) %{arch}/bin/grepjar
#%attr(755,root,root) %{arch}/bin/jar
%attr(755,root,root) %{gcclib}/jc1
%attr(755,root,root) %{gcclib}/jvgenmain
%{_mandir}/man1/%{target}-gcj.1*
%{_mandir}/man1/%{target}-gcjh.1*
%{_mandir}/man1/%{target}-gjnih.1*
%{_mandir}/man1/%{target}-grepjar.1*
%{_mandir}/man1/%{target}-fastjar.1*
%{_mandir}/man1/%{target}-jcf-dump.1*
%{_mandir}/man1/%{target}-jv-scan.1*
%endif
