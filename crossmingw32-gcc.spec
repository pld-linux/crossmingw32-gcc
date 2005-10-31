#
# Conditional build:
%bcond_with	bootstrap	# bootstrap build (using binary w32api/mingw)
#
%define		DASHED_SNAP	%{nil}
%define		SNAP		%(echo %{DASHED_SNAP} | sed -e "s#-##g")
%define		GCC_VERSION	3.4.3
%define		apiver		3.5
%define		apisrc		w32api-%{apiver}
%define		runver		3.9
%define		runsrc		mingw-runtime-%{runver}
Summary:	Cross Mingw32 GNU binary utility development utilities - gcc
Summary(es):	Utilitarios para desarrollo de binarios de la GNU - Mingw32 gcc
Summary(fr):	Utilitaires de développement binaire de GNU - Mingw32 gcc
Summary(pl):	Skro¶ne narzêdzia programistyczne GNU dla Mingw32 - gcc
Summary(pt_BR): Utilitários para desenvolvimento de binários da GNU - Mingw32 gcc
Summary(tr):	GNU geliþtirme araçlarý - Mingw32 gcc
Name:		crossmingw32-gcc
Version:	%{GCC_VERSION}
Release:	4
Epoch:		1
License:	GPL
Group:		Development/Languages
Source0:	ftp://gcc.gnu.org/pub/gcc/releases/gcc-%{GCC_VERSION}/gcc-%{GCC_VERSION}.tar.bz2
# Source0-md5:	e744b30c834360fccac41eb7269a3011
Source1:	http://dl.sourceforge.net/mingw/%{apisrc}.tar.gz
# Source1-md5:	2529dffea94118865cdc06c1f7ead697
Source2:	http://dl.sourceforge.net/mingw/%{runsrc}.tar.gz
# Source2-md5:	0cb66b1071da224ea2174f960c593e2e
Patch0:		gcc-nodebug.patch
Patch1:		%{name}-noioctl.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	crossmingw32-binutils >= 2.15.91.0.2-2
BuildRequires:	flex
%if %{without bootstrap}
BuildRequires:	crossmingw32-runtime >= 3.5
BuildRequires:	crossmingw32-w32api >= 3.1
%endif
Requires:	crossmingw32-binutils >= 2.15.91.0.2-2
Requires:	gcc-dirs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		no_install_post_strip	1

%define		target		i386-mingw32
%define		target_platform i386-pc-mingw32
%define		arch		%{_prefix}/%{target}
%define		gccarch		%{_libdir}/gcc/%{target}
%define		gcclib		%{_libdir}/gcc/%{target}/%{version}

%description
crossmingw32 is a complete cross-compiling development system for
building stand-alone Microsoft Windows applications under Linux using
the Mingw32 build libraries. This includes a binutils, gcc with g++
and objc, and libstdc++, all cross targeted to i386-mingw32, along
with supporting Win32 libraries in 'coff' format from free sources.

This package contains cross targeted gcc.

%description -l de
Dieses Paket enthält einen Cross-gcc, der es erlaubt, auf einem
anderem Rechner Code für Win32 zu generieren.

%description -l pl
crossmingw32 jest kompletnym systemem do kompilacji skro¶nej,
pozwalaj±cym budowaæ aplikacje MS Windows pod Linuksem u¿ywaj±c
bibliotek Mingw32. System sk³ada siê z binutils, gcc z g++ i objc,
libstdc++ - wszystkie generuj±ce kod dla platformy i386-mingw32, oraz
z bibliotek w formacie COFF.

Ten pakiet zawiera gcc generuj±ce skro¶nie kod dla Win32.

%package c++
Summary:	Mingw32 binary utility development utilities - g++
Summary(pl):	Zestaw narzêdzi mingw32 - g++
Group:		Development/Languages
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description c++
crossmingw32 is a complete cross-compiling development system for
building stand-alone Microsoft Windows applications under Linux using
the Mingw32 build libraries. This includes a binutils, gcc with g++
and objc, and libstdc++, all cross targeted to i386-mingw32, along
with supporting Win32 libraries in 'coff' format from free sources.

This package contains cross targeted g++ and (static) libstdc++.

%description c++ -l pl
crossmingw32 jest kompletnym systemem do kompilacji skro¶nej,
pozwalaj±cym budowaæ aplikacje MS Windows pod Linuksem u¿ywaj±c
bibliotek mingw32. System sk³ada siê z binutils, gcc z g++ i objc,
libstdc++ - wszystkie generuj±ce kod dla platformy i386-mingw32, oraz
z bibliotek w formacie COFF.

Ten pakiet zawiera g++ generuj±ce kod pod Win32 oraz bibliotekê
libstdc++.

# does this even work?
%package objc
Summary:	Mingw32 binary utility development utilities - objc
Summary(pl):	Zestaw narzêdzi mingw32 - objc
Group:		Development/Languages
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description objc
crossmingw32 is a complete cross-compiling development system for
building stand-alone Microsoft Windows applications under Linux using
the Mingw32 build libraries. This includes a binutils, gcc with g++
and objc, and libstdc++, all cross targeted to i386-mingw32, along
with supporting Win32 libraries in 'coff' format from free sources.

This package contains cross targeted objc.

%description objc -l pl
crossmingw32 jest kompletnym systemem do kompilacji skro¶nej,
pozwalaj±cym budowaæ aplikacje MS Windows pod Linuksem u¿ywaj±c
bibliotek mingw32. System sk³ada siê z binutils, gcc z g++ i objc,
libstdc++ - wszystkie generuj±ce kod dla platformy i386-mingw32, oraz
z bibliotek w formacie COFF.

Ten pakiet zawiera kompilator objc generuj±cy kod pod Win32.

# does this even work?
%package g77
Summary:	Mingw32 binary utility development utilities - g77
Summary(pl):	Zestaw narzêdzi mingw32 - g77
Group:		Development/Languages
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description g77
crossmingw32 is a complete cross-compiling development system for
building stand-alone Microsoft Windows applications under Linux using
the Mingw32 build libraries. This includes a binutils, gcc with g++
and objc, and libstdc++, all cross targeted to i386-mingw32, along
with supporting Win32 libraries in 'coff' format from free sources.

This package contains cross targeted g77.

%description g77 -l pl
crossmingw32 jest kompletnym systemem do kompilacji skro¶nej,
pozwalaj±cym budowaæ aplikacje MS Windows pod Linuksem u¿ywaj±c
bibliotek mingw32. System sk³ada siê z binutils, gcc z g++ i objc,
libstdc++ - wszystkie generuj±ce kod dla platformy i386-mingw32, oraz
z bibliotek w formacie COFF.

Ten pakiet zawiera g77 generuj±cy kod pod Win32.

# does this even work?
%package java
Summary:	Mingw32 binary utility development utilities - java
Summary(pl):	Zestaw narzêdzi mingw32 - java
Group:		Development/Languages
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description java
crossmingw32 is a complete cross-compiling development system for
building stand-alone Microsoft Windows applications under Linux using
the Mingw32 build libraries. This includes a binutils, gcc with g++
and objc, and libstdc++, all cross targeted to i386-mingw32, along
with supporting Win32 libraries in 'coff' format from free sources.

This package contains cross targeted java.

%description java -l pl

crossmingw32 jest kompletnym systemem do kompilacji skro¶nej,
pozwalaj±cym budowaæ aplikacje MS Windows pod Linuksem u¿ywaj±c
bibliotek mingw32. System sk³ada siê z binutils, gcc z g++ i objc,
libstdc++ - wszystkie generuj±ce kod dla platformy i386-mingw32, oraz
z bibliotek w formacie COFF.

Ten pakiet zawiera kompilator Javy generuj±cy kod pod Win32.

%prep
%setup -q -c
cd gcc-%{version}
%if %{with bootstrap}
mkdir winsup
tar xzf %{SOURCE1} -C winsup
tar xzf %{SOURCE2} -C winsup
%endif
%{!?debug:%patch0 -p1}
%patch1 -p1

%build
cd gcc-%{version}
%if %{with bootstrap}
for tool in as ar dlltool ld nm ranlib strip ; do
	ln -sf %{arch}/bin/$tool winsup/bin/$tool
done
build_tooldir=`pwd`/winsup
%else
build_tooldir=%{arch}
%endif

cp /usr/share/automake/config.sub .
cp /usr/share/automake/config.sub boehm-gc

rm -rf obj-%{target_platform} && install -d obj-%{target_platform} && cd obj-%{target_platform}

# note: alpha's -mieee and sparc's -mtune=* are not valid for target's g++
CFLAGS="%{rpmcflags}" \
%ifarch alpha
CXXFLAGS="`echo '%{rpmcflags}' | sed -e 's/ \?-mieee\>//'`" \
%else
%ifarch sparc sparc64 sparcv9
CXXFLAGS="`echo '%{rpmcflags}' | sed -e 's/ \?-mtune[=0-9a-z]*//'`" \
%else
CXXFLAGS="%{rpmcflags}" \
%endif
%endif
LDFLAGS="%{rpmldflags}" \
TEXCONFIG=false \
../configure \
	--prefix=%{_prefix} \
	--infodir=%{_infodir} \
	--mandir=%{_mandir} \
	--bindir=%{arch}/bin \
	--libdir=%{_libdir} \
	--libexecdir=%{_libexecdir} \
	--includedir=%{arch}/include \
	--enable-languages="c,c++,f77,java,objc" \
	--with-gnu-as \
	--with-gnu-ld \
	--with-gxx-include-dir=%{arch}/include/g++ \
	--enable-threads \
	--build=%{_target_platform} \
	--host=%{_target_platform} \
	--target=%{target}

#touch ../gcc/c-gperf.h

%{__make} \
	LDFLAGS_FOR_TARGET="%{rpmldflags}" \
	TARGET_LIBGCC2_CFLAGS="-UCROSS_COMPILE" \
	build_tooldir="$build_tooldir" \
	FLAGS_FOR_TARGET="-B${build_tooldir}/bin -B${build_tooldir}/lib -isystem ${build_tooldir}/include -nostdinc" \
	CFLAGS_FOR_TARGET="-nostdinc" \
	NM_FOR_TARGET="%{target}-nm"

# build libobjc.dll for Objective C
# it must be called from obj-%{target_platform}/%{target}/libobjc, but
# GCC_FOR_TARGET must be passed
#
#make -C %{target}/libobjc \
#	LDFLAGS="%{rpmldflags}" \
#	TARGET_LIBGCC2_CFLAGS="-UCROSS_COMPILE" \
#	DLLTOOL="%{target}-dlltool --as=%{target}-as" libobjc.dll

# spec files for msvcrt*.dll configurations
cd gcc
for n in msvcrt msvcrt20 msvcrt40; do
	sed "s/crtdll/$n/g" <specs | sed "s/crt1/crt2/g" >specs.$n
done

%install
rm -rf $RPM_BUILD_ROOT
cd gcc-%{version}

install -d $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT%{_datadir}
cd obj-%{target_platform}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cd gcc
install specs.msvcrt specs.msvcrt20 specs.msvcrt40 $RPM_BUILD_ROOT%{gcclib}
cd ../..

mv -f $RPM_BUILD_ROOT%{arch}/bin/%{target}-* $RPM_BUILD_ROOT%{_bindir}

# already in arch/lib, shouldn't be here
rm -f $RPM_BUILD_ROOT%{_libdir}/libiberty.a

%if 0%{!?debug:1}
# strip linux binaries
strip -R .comment -R .note \
	`echo $RPM_BUILD_ROOT{%{_bindir}/*,%{arch}/bin/*} | grep -v gccbug` \
	$RPM_BUILD_ROOT%{gcclib}/{cc1*,f771,jc1,jvgenmain}

# strip mingw32 libraries
%{target}-strip -g \
	$RPM_BUILD_ROOT%{gcclib}/libgcc.a \
	$RPM_BUILD_ROOT%{arch}/lib/lib*.a
%endif

# restore hardlinks
ln -f $RPM_BUILD_ROOT%{_bindir}/%{target}-{g++,c++}
ln -f $RPM_BUILD_ROOT%{arch}/bin/{g++,c++}

# the same... make hardlink
ln -f $RPM_BUILD_ROOT%{arch}/bin/gcc $RPM_BUILD_ROOT%{_bindir}/%{target}-gcc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{target}-gcc*
%attr(755,root,root) %{_bindir}/%{target}-cpp
%attr(755,root,root) %{_bindir}/%{target}-gcov
%attr(755,root,root) %{arch}/bin/gcc
%{arch}/lib/libiberty.a

%dir %{gccarch}
%dir %{gcclib}
%attr(755,root,root) %{gcclib}/cc1
%{gcclib}/libgcc.a
%{gcclib}/libgcov.a
%{gcclib}/specs*
%{gcclib}/include

%{_mandir}/man1/%{target}-cpp.1*
%{_mandir}/man1/%{target}-gcc.1*
%{_mandir}/man1/%{target}-gcov.1*

%files c++
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{target}-[cg]++
%attr(755,root,root) %{arch}/bin/[cg]++
%attr(755,root,root) %{gcclib}/cc1plus
%{arch}/lib/libstdc++.a
%{arch}/lib/libstdc++.la
%{arch}/lib/libsupc++.a
%{arch}/lib/libsupc++.la
%{arch}/include/g++
%{_mandir}/man1/%{target}-g++.1*

%files objc
%defattr(644,root,root,755)
%attr(755,root,root) %{gcclib}/cc1obj
%{arch}/lib/libobjc.a
%{arch}/lib/libobjc.la

%files g77
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{target}-g77
%attr(755,root,root) %{gcclib}/f771
%{arch}/lib/libfrtbegin.a
%{arch}/lib/libg2c.a
%{arch}/lib/libg2c.la
%{_mandir}/man1/%{target}-g77.1*

%files java
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{target}-gcj
%attr(755,root,root) %{_bindir}/%{target}-gcjh
%attr(755,root,root) %{_bindir}/%{target}-grepjar
%attr(755,root,root) %{_bindir}/%{target}-jar
%attr(755,root,root) %{_bindir}/%{target}-jcf-dump
%attr(755,root,root) %{_bindir}/%{target}-jv-scan
#%attr(755,root,root) %{arch}/bin/grepjar
#%attr(755,root,root) %{arch}/bin/jar
%attr(755,root,root) %{gcclib}/jc1
%attr(755,root,root) %{gcclib}/jvgenmain
%{_mandir}/man1/%{target}-gcj.1*
%{_mandir}/man1/%{target}-gcjh.1*
%{_mandir}/man1/%{target}-grepjar.1*
%{_mandir}/man1/%{target}-jar.1*
%{_mandir}/man1/%{target}-jcf-dump.1*
%{_mandir}/man1/%{target}-jv-scan.1*
