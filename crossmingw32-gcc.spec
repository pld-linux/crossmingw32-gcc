%define		DASHED_SNAP	%{nil}
%define		SNAP		%(echo %{DASHED_SNAP} | sed -e "s#-##g")
%define		GCC_VERSION	3.2.2
Summary:	Mingw32 Binary Utility Development Utilities - gcc
Summary(pl):	Zestaw narzêdzi mingw32 - gcc
Name:		crossmingw32-gcc
Version:	%{GCC_VERSION}
Release:	1
Epoch:		1
License:	GPL
Group:		Development/Languages
ExclusiveArch:	%{ix86}
Source0:	ftp://gcc.gnu.org/pub/gcc/releases/gcc-%{GCC_VERSION}/gcc-%{GCC_VERSION}.tar.bz2
Patch0:		gcc-slibdir.patch
BuildRequires:	autoconf
BuildRequires:	bison
BuildRequires:	crossmingw32-binutils
BuildRequires:	crossmingw32-w32api
BuildRequires:	flex
Requires:	crossmingw32-binutils
Requires:	crossmingw32-w32api
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		no_install_post_strip	1

%define		target		i386-mingw32
%define		target_platform i386-pc-mingw32
%define		arch		%{_prefix}/%{target}
%define		gccarch		%{_prefix}/lib/gcc-lib/%{target}
%define		gcclib		%{_prefix}/lib/gcc-lib/%{target}/%{version}

%description
crossmingw32 is a complete cross-compiling development system for
building stand-alone Microsoft Windows applications under Linux using
the Mingw32 build libraries. This includes a binutils, gcc with g++
and objc, and libstdc++, all cross targeted to i386-mingw32, along
with supporting Win32 libraries in 'coff' format from free sources.

This package contains cross targeted gcc.

%description -l pl
crossmingw32 jest kompletnym systemem do kroskompilacji, pozwalaj±cym
budowaæ aplikacje MS Windows pod Linuksem u¿ywaj±c bibliotek mingw32.
System sk³ada siê z binutils, gcc z g++ i objc, libstdc++ - wszystkie
generuj±ce kod dla platformy i386-mingw32, oraz z bibliotek w formacie
COFF.

Ten pakiet zawiera gcc generuj±ce kod dla Win32.

%package c++
Summary:	Mingw32 Binary Utility Development Utilities - g++
Summary(pl):	Zestaw narzêdzi mingw32 - g++
Group:		Development/Languages
Requires:	%{name} = %{version}

%description c++
crossmingw32 is a complete cross-compiling development system for
building stand-alone Microsoft Windows applications under Linux using
the Mingw32 build libraries. This includes a binutils, gcc with g++
and objc, and libstdc++, all cross targeted to i386-mingw32, along
with supporting Win32 libraries in 'coff' format from free sources.

This package contains cross targeted g++ and (static) libstdc++.

%description c++ -l pl
crossmingw32 jest kompletnym systemem do kroskompilacji, pozwalaj±cym
budowaæ aplikacje MS Windows pod Linuksem u¿ywaj±c bibliotek mingw32.
System sk³ada siê z binutils, gcc z g++ i objc, libstdc++ - wszystkie
generuj±ce kod dla platformy i386-mingw32, oraz z bibliotek w formacie
COFF.

Ten pakiet zawiera g++ generuj±ce kod pod Win32 oraz bibliotekê
libstdc++.

# does this even work?
%package objc
Summary:	Mingw32 Binary Utility Development Utilities - objc
Summary(pl):	Zestaw narzêdzi mingw32 - objc
Group:		Development/Languages
Requires:	%{name} = %{version}

%description objc
crossmingw32 is a complete cross-compiling development system for
building stand-alone Microsoft Windows applications under Linux using
the Mingw32 build libraries. This includes a binutils, gcc with g++
and objc, and libstdc++, all cross targeted to i386-mingw32, along
with supporting Win32 libraries in 'coff' format from free sources.

This package contains cross targeted objc.

%description objc -l pl
crossmingw32 jest kompletnym systemem do kroskompilacji, pozwalaj±cym
budowaæ aplikacje MS Windows pod Linuksem u¿ywaj±c bibliotek mingw32.
System sk³ada siê z binutils, gcc z g++ i objc, libstdc++ - wszystkie
generuj±ce kod dla platformy i386-mingw32, oraz z bibliotek w formacie
COFF.

Ten pakiet zawiera kompilator objc generuj±cy kod pod Win32.

# does this even work?
%package g77
Summary:	Mingw32 Binary Utility Development Utilities - g77
Summary(pl):	Zestaw narzêdzi mingw32 - g77
Group:		Development/Languages
Requires:	%{name} = %{version}

%description g77
crossmingw32 is a complete cross-compiling development system for
building stand-alone Microsoft Windows applications under Linux using
the Mingw32 build libraries. This includes a binutils, gcc with g++
and objc, and libstdc++, all cross targeted to i386-mingw32, along
with supporting Win32 libraries in 'coff' format from free sources.

This package contains cross targeted g77.

%description g77 -l pl
crossmingw32 jest kompletnym systemem do kroskompilacji, pozwalaj±cym
budowaæ aplikacje MS Windows pod Linuksem u¿ywaj±c bibliotek mingw32.
System sk³ada siê z binutils, gcc z g++ i objc, libstdc++ - wszystkie
generuj±ce kod dla platformy i386-mingw32, oraz z bibliotek w formacie
COFF.

Ten pakiet zawiera g77 generuj±cy kod pod Win32.

# does this even work?
%package java
Summary:	Mingw32 Binary Utility Development Utilities - java
Summary(pl):	Zestaw narzêdzi mingw32 - java
Group:		Development/Languages
Requires:	%{name} = %{version}

%description java
crossmingw32 is a complete cross-compiling development system for
building stand-alone Microsoft Windows applications under Linux using
the Mingw32 build libraries. This includes a binutils, gcc with g++
and objc, and libstdc++, all cross targeted to i386-mingw32, along
with supporting Win32 libraries in 'coff' format from free sources.

This package contains cross targeted java.

%description java -l pl
crossmingw32 jest kompletnym systemem do kroskompilacji, pozwalaj±cym
budowaæ aplikacje MS Windows pod Linuksem u¿ywaj±c bibliotek mingw32.
System sk³ada siê z binutils, gcc z g++ i objc, libstdc++ - wszystkie
generuj±ce kod dla platformy i386-mingw32, oraz z bibliotek w formacie
COFF.

Ten pakiet zawiera kompilator Javy generuj±cy kod pod Win32.

%prep
%setup -q -n gcc-%{version}
%patch0 -p1

%build
rm -rf obj-%{target_platform} && install -d obj-%{target_platform} && cd obj-%{target_platform}

CFLAGS="%{rpmcflags}" \
CXXFLAGS="%{rpmcflags}"  \
LDFLAGS="%{rpmldflags}" \
TEXCONFIG=false \
../configure \
	--prefix=%{_prefix} \
	--infodir=%{_infodir} \
	--mandir=%{_mandir} \
	--bindir=%{arch}/bin \
	--enable-languages="c,c++,f77,gcov,java,objc" \
	--with-gnu-as \
	--with-gnu-ld \
	--with-gxx-include-dir=%{arch}/include/g++ \
	--enable-threads \
	--target=%{target}

#touch ../gcc/c-gperf.h

%{__make} \
	LDFLAGS_FOR_TARGET="%{rpmldflags}" \
	TARGET_LIBGCC2_CFLAGS="-UCROSS_COMPILE"

# build libobjc.dll for Objective C
# to trzeba wywo³ywaæ z katalogu obj-%{target_platform}/%{target}/libobjc
# ale trzeba podaæ jeszcze GCC_FOR_TARGET - a mi siê nie chce.
# BTW, ten dll jest do czego¶ potrzebny???
#
#make \
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

install -d $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT%{_datadir}
cd obj-%{target_platform}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cd gcc
install specs.msvcrt specs.msvcrt20 specs.msvcrt40 $RPM_BUILD_ROOT%{gcclib}
cd ../..

mv -f $RPM_BUILD_ROOT%{arch}/bin/%{target}-* $RPM_BUILD_ROOT%{_bindir}

# c++filt is provided by binutils
rm -f $RPM_BUILD_ROOT%{_bindir}/i386-mingw32-c++filt

# already in arch/lib, shouldn't be here
rm -f $RPM_BUILD_ROOT%{_libdir}/libiberty.a

%if 0%{!?debug:1}
# strip linux binaries
strip -R .comment -R .note \
	`echo $RPM_BUILD_ROOT{%{_bindir}/*,%{arch}/bin/*} | grep -v gccbug` \
	$RPM_BUILD_ROOT%{gcclib}/{cc1*,cpp0,f771,jc1,jvgenmain,tradcpp0}

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
%attr(755,root,root) %{gcclib}/cpp0
%attr(755,root,root) %{gcclib}/tradcpp0
%{gcclib}/libgcc.a
%{gcclib}/libgcc.a
%{gcclib}/specs*
%{gcclib}/include

%{_mandir}/man1/%{target}-gcc.1*

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
%attr(755,root,root) %{_bindir}/%{target}-jcf-dump
%attr(755,root,root) %{_bindir}/%{target}-jv-scan
%attr(755,root,root) %{arch}/bin/grepjar
%attr(755,root,root) %{arch}/bin/jar
%attr(755,root,root) %{gcclib}/jc1
%attr(755,root,root) %{gcclib}/jvgenmain
%{_mandir}/man1/%{target}-gcj.1*
