#
# TODO:
# - restore languages other than c, c++
# - openmp
#
# Conditional build:
%bcond_with	bootstrap	# bootstrap build (using binary w32api/mingw)
#
Summary:	Cross Mingw32 GNU binary utility development utilities - gcc
Summary(es.UTF-8):	Utilitarios para desarrollo de binarios de la GNU - Mingw32 gcc
Summary(fr.UTF-8):	Utilitaires de développement binaire de GNU - Mingw32 gcc
Summary(pl.UTF-8):	Skrośne narzędzia programistyczne GNU dla Mingw32 - gcc
Summary(pt_BR.UTF-8):	Utilitários para desenvolvimento de binários da GNU - Mingw32 gcc
Summary(tr.UTF-8):	GNU geliştirme araçları - Mingw32 gcc
Name:		crossmingw32-gcc
Version:	4.5.1
Release:	1
Epoch:		1
License:	GPL v2+
Group:		Development/Languages
Source0:	ftp://gcc.gnu.org/pub/gcc/releases/gcc-%{version}/gcc-%{version}.tar.bz2
# Source0-md5:	48231a8e33ed6e058a341c53b819de1a
%define		apiver	3.10
Source1:	http://dl.sourceforge.net/mingw/w32api-%{apiver}.tar.gz
# Source1-md5:	7067a6b3ac9d94bb753f9f6f37e2033c
%define		runver	3.13
Source2:	http://dl.sourceforge.net/mingw/mingw-runtime-%{runver}.tar.gz
# Source2-md5:	22179021f41d5eee76447b78fb94a3fb
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
Requires:	crossmingw32-binutils >= 2.15.91.0.2-2
Requires:	gcc-dirs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		target		i386-mingw32
%define		arch		%{_prefix}/%{target}
%define		gccarch		%{_libdir}/gcc/%{target}
%define		gcclib		%{gccarch}/%{version}

%define		_noautostrip	.*/lib.*\\.a

%define		_enable_debug_packages 0

%description
crossmingw32 is a complete cross-compiling development system for
building stand-alone Microsoft Windows applications under Linux using
the Mingw32 build libraries. This includes a binutils, gcc with g++
and objc, and libstdc++, all cross targeted to i386-mingw32, along
with supporting Win32 libraries in 'coff' format from free sources.

This package contains cross targeted gcc.

%description -l de.UTF-8
Dieses Paket enthält einen Cross-gcc, der es erlaubt, auf einem
anderem Rechner Code für Win32 zu generieren.

%description -l pl.UTF-8
crossmingw32 jest kompletnym systemem do kompilacji skrośnej,
pozwalającym budować aplikacje MS Windows pod Linuksem używając
bibliotek Mingw32. System składa się z binutils, gcc z g++ i objc,
libstdc++ - wszystkie generujące kod dla platformy i386-mingw32, oraz
z bibliotek w formacie COFF.

Ten pakiet zawiera gcc generujące skrośnie kod dla Win32.

%package c++
Summary:	Mingw32 binary utility development utilities - g++
Summary(pl.UTF-8):	Zestaw narzędzi mingw32 - g++
Group:		Development/Languages
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description c++
crossmingw32 is a complete cross-compiling development system for
building stand-alone Microsoft Windows applications under Linux using
the Mingw32 build libraries. This includes a binutils, gcc with g++
and objc, and libstdc++, all cross targeted to i386-mingw32, along
with supporting Win32 libraries in 'coff' format from free sources.

This package contains cross targeted g++ and (static) libstdc++.

%description c++ -l pl.UTF-8
crossmingw32 jest kompletnym systemem do kompilacji skrośnej,
pozwalającym budować aplikacje MS Windows pod Linuksem używając
bibliotek mingw32. System składa się z binutils, gcc z g++ i objc,
libstdc++ - wszystkie generujące kod dla platformy i386-mingw32, oraz
z bibliotek w formacie COFF.

Ten pakiet zawiera g++ generujące kod pod Win32 oraz bibliotekę
libstdc++.

# no obj-c, fortran, java for the moment
%if 0
# does this even work?
%package objc
Summary:	Mingw32 binary utility development utilities - objc
Summary(pl.UTF-8):	Zestaw narzędzi mingw32 - objc
Group:		Development/Languages
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description objc
crossmingw32 is a complete cross-compiling development system for
building stand-alone Microsoft Windows applications under Linux using
the Mingw32 build libraries. This includes a binutils, gcc with g++
and objc, and libstdc++, all cross targeted to i386-mingw32, along
with supporting Win32 libraries in 'coff' format from free sources.

This package contains cross targeted objc compiler.

%description objc -l pl.UTF-8
crossmingw32 jest kompletnym systemem do kompilacji skrośnej,
pozwalającym budować aplikacje MS Windows pod Linuksem używając
bibliotek mingw32. System składa się z binutils, gcc z g++ i objc,
libstdc++ - wszystkie generujące kod dla platformy i386-mingw32, oraz
z bibliotek w formacie COFF.

Ten pakiet zawiera kompilator objc generujący kod pod Win32.

# does this even work?
%package fortran
Summary:	Mingw32 binary utility development utilities - Fortran
Summary(pl.UTF-8):	Zestaw narzędzi mingw32 - Fortran
Group:		Development/Languages
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	crossmingw32-gcc-g77

%description fortran
crossmingw32 is a complete cross-compiling development system for
building stand-alone Microsoft Windows applications under Linux using
the Mingw32 build libraries. This includes a binutils, gcc with g++
and objc, and libstdc++, all cross targeted to i386-mingw32, along
with supporting Win32 libraries in 'coff' format from free sources.

This package contains cross targeted Fortran compiler.

%description fortran -l pl.UTF-8
crossmingw32 jest kompletnym systemem do kompilacji skrośnej,
pozwalającym budować aplikacje MS Windows pod Linuksem używając
bibliotek mingw32. System składa się z binutils, gcc z g++ i objc,
libstdc++ - wszystkie generujące kod dla platformy i386-mingw32, oraz
z bibliotek w formacie COFF.

Ten pakiet zawiera kompilator Fortranu generujący kod pod Win32.

# does this even work?
%package java
Summary:	Mingw32 binary utility development utilities - Java
Summary(pl.UTF-8):	Zestaw narzędzi mingw32 - Java
Group:		Development/Languages
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description java
crossmingw32 is a complete cross-compiling development system for
building stand-alone Microsoft Windows applications under Linux using
the Mingw32 build libraries. This includes a binutils, gcc with g++
and objc, and libstdc++, all cross targeted to i386-mingw32, along
with supporting Win32 libraries in 'coff' format from free sources.

This package contains cross targeted Java compiler.

%description java -l pl.UTF-8

crossmingw32 jest kompletnym systemem do kompilacji skrośnej,
pozwalającym budować aplikacje MS Windows pod Linuksem używając
bibliotek mingw32. System składa się z binutils, gcc z g++ i objc,
libstdc++ - wszystkie generujące kod dla platformy i386-mingw32, oraz
z bibliotek w formacie COFF.

Ten pakiet zawiera kompilator Javy generujący kod pod Win32.
%endif

%prep
%setup -q -n gcc-%{version}
%patch100 -p0
%patch0 -p1
%patch2 -p1

%if %{with bootstrap}
mkdir winsup
tar xzf %{SOURCE1} -C winsup
tar xzf %{SOURCE2} -C winsup
%endif

# override snapshot version.
echo %{version} > gcc/BASE-VER
echo "release" > gcc/DEV-PHASE

%build
%if %{with bootstrap}
for tool in as ar dlltool ld nm ranlib strip ; do
	ln -sf %{arch}/bin/$tool winsup/bin/$tool
done
%endif

rm -rf builddir && install -d builddir && cd builddir

CC="%{__cc}" \
CFLAGS="%{rpmcflags}" \
CXXFLAGS="%{rpmcxxflags}" \
TEXCONFIG=false \
../configure \
	--prefix=%{arch} \
	--infodir=%{_infodir} \
	--mandir=%{_mandir} \
	--with-headers=%{arch}/include \
	--with-libs=%{arch}/lib \
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

cd ..
%{__make} -C builddir all-host
patch -p1 <%{PATCH1}
%{__make} -C builddir

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}}

%{__make} -C builddir install \
	DESTDIR=$RPM_BUILD_ROOT

%if 0%{!?debug:1}
%{target}-strip -g -R.note -R.comment $RPM_BUILD_ROOT%{arch}/lib/lib*.a
%endif

# restore hardlinks
ln -f $RPM_BUILD_ROOT%{arch}/bin/%{target}-gcc $RPM_BUILD_ROOT%{_bindir}/%{target}-gcc
ln -f $RPM_BUILD_ROOT%{arch}/bin/%{target}-g++ $RPM_BUILD_ROOT%{_bindir}/%{target}-g++
ln -f $RPM_BUILD_ROOT%{arch}/bin/%{target}-cpp $RPM_BUILD_ROOT%{_bindir}/%{target}-cpp
ln -f $RPM_BUILD_ROOT%{arch}/bin/%{target}-gcov $RPM_BUILD_ROOT%{_bindir}/%{target}-gcov

install -d $RPM_BUILD_ROOT%{_libdir}
install -d $RPM_BUILD_ROOT%{_libdir}/gcc

cp -r $RPM_BUILD_ROOT%{arch}/libexec/gcc/%{target} $RPM_BUILD_ROOT%{_libdir}/gcc
cp -r $RPM_BUILD_ROOT%{arch}/lib/gcc/%{target} $RPM_BUILD_ROOT%{_libdir}/gcc
rm -rf $RPM_BUILD_ROOT%{_libdir}/gcc/%{target}/%{version}/install-tools
rm -rf $RPM_BUILD_ROOT%{arch}/libexec
rm -rf $RPM_BUILD_ROOT%{arch}/lib/gcc

mv -f $RPM_BUILD_ROOT%{_libdir}/gcc/%{target}/%{version}/cc1 $RPM_BUILD_ROOT%{arch}/bin/cc1
mv -f $RPM_BUILD_ROOT%{_libdir}/gcc/%{target}/%{version}/cc1plus $RPM_BUILD_ROOT%{arch}/bin/cc1plus
mv -f $RPM_BUILD_ROOT%{_libdir}/gcc/%{target}/%{version}/collect2 $RPM_BUILD_ROOT%{arch}/bin/collect2

install builddir/i386-mingw32/libgcc/shlib/libgcc_s_dw2-1.dll $RPM_BUILD_ROOT%{arch}/bin
%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{target}-gcc
%attr(755,root,root) %{_bindir}/%{target}-cpp
%attr(755,root,root) %{_bindir}/%{target}-gcov
%attr(755,root,root) %{arch}/bin/%{target}-gcc*
%attr(755,root,root) %{arch}/bin/%{target}-cpp
%attr(755,root,root) %{arch}/bin/%{target}-gcov
%attr(755,root,root) %{arch}/bin/cc1
%attr(755,root,root) %{arch}/bin/collect2
%{arch}/bin/*.dll

%{_libdir}/gcc/%{target}
%{arch}/%{_lib}/libiberty.a

%{_mandir}/man1/%{target}-cpp.1*
%{_mandir}/man1/%{target}-gcc.1*
%{_mandir}/man1/%{target}-gcov.1*

%files c++
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{target}-g++
%attr(755,root,root) %{arch}/bin/%{target}-c++
%attr(755,root,root) %{arch}/bin/%{target}-g++
%attr(755,root,root) %{arch}/bin/cc1plus

%{_mandir}/man1/%{target}-g++.1*

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
