Summary:	Mingw32 GNU Binary Utility Development Utilities - gcc
Name:		crossmingw32-gcc
%define	gccversion	2.95.3-test5
Version:	2.95.3
Release:	5
Epoch:		1
License:	GPL
Group:		Development/Languages
Group(de):	Entwicklung/Sprachen
Group(pl):	Programowanie/Jêzyki
ExclusiveArch:	%{ix86}
Source0:	ftp://ftp.gnu.org/pub/gnu/gcc-%{gccversion}.tar.gz
Patch0:		gcc-info.patch
Patch1:		gcc-pld-linux.patch
Patch2:		gcc-libstdc++.patch
Patch3:		gcc-bootstrap.patch
Patch4:		gcc-cpp-macro-doc.patch
Patch5:		gcc-default-arch.patch
Patch6:		gcc-libstdc++-out-of-mem.patch
Patch7:		gcc-libstdc++-wstring.patch
Patch8:		gcc-libstdc++-bastring.patch
Patch9:		gcc-manpage.patch
Patch10:	gcc-cpp-dos-newlines.patch
Patch11:	gcc-gpc.patch
Patch12:	gcc-m68k-pic.patch
Patch13:	gcc-sparc32-rfi.patch
Patch14:	gcc-builtin-apply.patch
Patch15:	gcc-ppc-ice.patch
Patch16:	gcc-ppc-descriptions.patch
Patch17:	gcc-alpha-complex-float.patch
Patch18:	gcc-gcj-vs-iconv.patch
Patch19:	gcc-libobjc.patch
Patch20:	gcc-pointer-arith.patch
Patch21:	%{name}-libio.patch
Patch22:	%{name}-includes.patch
Patch23:	%{name}-libiberty.patch
BuildRequires:	crossmingw32-platform
BuildRequires:	crossmingw32-binutils
BuildRequires:	flex
BuildRequires:	bison
BuildRequires:	autoconf
Requires:	crossmingw32-binutils
Requires:	crossmingw32-platform
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		target		i386-mingw32
%define		target_platform i386-pc-mingw32
%define		_prefix		/usr
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

%package c++
Summary:	Mingw32 GNU Binary Utility Development Utilities - g++
Group:		Development/Languages
Group(de):	Entwicklung/Sprachen
Group(pl):	Programowanie/Jêzyki
Requires:	%{name} = %{version}

%description c++
crossmingw32 is a complete cross-compiling development system for
building stand-alone Microsoft Windows applications under Linux using
the Mingw32 build libraries. This includes a binutils, gcc with g++
and objc, and libstdc++, all cross targeted to i386-mingw32, along
with supporting Win32 libraries in 'coff' format from free sources.

This package contains cross targeted g++ and (static) libstdc++.

# does this even work?
%package objc
Summary:	Mingw32 GNU Binary Utility Development Utilities - objc
Group:		Development/Languages
Group(de):	Entwicklung/Sprachen
Group(pl):	Programowanie/Jêzyki
Requires:	%{name} = %{version}

%description objc
crossmingw32 is a complete cross-compiling development system for
building stand-alone Microsoft Windows applications under Linux using
the Mingw32 build libraries. This includes a binutils, gcc with g++
and objc, and libstdc++, all cross targeted to i386-mingw32, along
with supporting Win32 libraries in 'coff' format from free sources.

This package contains cross targeted objc.

# does this even work?
%package g77
Summary:	Mingw32 GNU Binary Utility Development Utilities - g77
Group:		Development/Languages
Group(de):	Entwicklung/Sprachen
Group(pl):	Programowanie/Jêzyki
Requires:	%{name} = %{version}

%description g77
crossmingw32 is a complete cross-compiling development system for
building stand-alone Microsoft Windows applications under Linux using
the Mingw32 build libraries. This includes a binutils, gcc with g++
and objc, and libstdc++, all cross targeted to i386-mingw32, along
with supporting Win32 libraries in 'coff' format from free sources.

This package contains cross targeted g77.

# does this even work?
%package chill
Summary:	Mingw32 GNU Binary Utility Development Utilities - chill
Group:		Development/Languages
Group(de):	Entwicklung/Sprachen
Group(pl):	Programowanie/Jêzyki
Requires:	%{name} = %{version}

%description chill
crossmingw32 is a complete cross-compiling development system for
building stand-alone Microsoft Windows applications under Linux using
the Mingw32 build libraries. This includes a binutils, gcc with g++
and objc, and libstdc++, all cross targeted to i386-mingw32, along
with supporting Win32 libraries in 'coff' format from free sources.

This package contains cross targeted chill.

# does this even work?
%package java
Summary:	Mingw32 GNU Binary Utility Development Utilities - java
Group:		Development/Languages
Group(de):	Entwicklung/Sprachen
Group(pl):	Programowanie/Jêzyki
Requires:	%{name} = %{version}

%description java
crossmingw32 is a complete cross-compiling development system for
building stand-alone Microsoft Windows applications under Linux using
the Mingw32 build libraries. This includes a binutils, gcc with g++
and objc, and libstdc++, all cross targeted to i386-mingw32, along
with supporting Win32 libraries in 'coff' format from free sources.

This package contains cross targeted java.

%prep
%setup -q -n gcc-%{gccversion}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p0
%patch5 -p0
%patch6 -p0
%patch7 -p0
%patch8 -p0
%patch9 -p0
%patch10 -p0
%patch11 -p1
%ifarch m68k
%patch12 -p0
%endif
%ifarch sparc sparc32
%patch13 -p0
%patch14 -p0
%endif
%ifarch ppc
%patch15 -p0
%patch16 -p0
%endif
%ifarch alpha
%patch17 -p1
%endif
%patch18 -p0
%patch19 -p0
%patch20 -p0

%patch21 -p1
%patch22 -p1
%patch23 -p1

%build
(cd libiberty ; autoconf)
(cd gcc
autoconf
cd ..
rm -rf obj-%{target_platform}
install -d obj-%{target_platform}
cd obj-%{target_platform}

%{!?debug:CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s"} \
%{?debug:CFLAGS="-g -O0" CXXFLAGS="-g -O0" LDFLAGS=""} \
../configure \
	--prefix=%{_prefix} \
	--infodir=%{_infodir} \
	--mandir=%{_mandir} \
	--bindir=%{arch}/bin \
	--with-gnu-as \
	--with-gnu-ld \
	--with-gxx-include-dir=%{arch}/include/g++ \
	--target=%{target}

# to nie dzia³a bo kto¶ ukrad³ gthr-win32.h i nie wiem co tam wpisaæ
#	--enable-threads \

touch ../gcc/c-gperf.h

%{__make} \
	%{!?debug:LDFLAGS_FOR_TARGET="-s"}%{?debug:LDFLAGS_FOR_TARGET=""} \
	TARGET_LIBGCC2_CFLAGS="-UCROSS_COMPILE"

# build libobjc.dll for Objective C
# to trzeba wywo³ywaæ z katalogu obj-%{target_platform}/%{target}/libobjc
# ale trzeba podaæ jeszcze GCC_FOR_TARGET - a mi siê nie chce.
# BTW, ten dll jest do czego¶ potrzebny???
#
#make \
#	LDFLAGS="-s" \
#	TARGET_LIBGCC2_CFLAGS="-UCROSS_COMPILE" \
#	DLLTOOL="%{target}-dlltool --as=%{target}-as" libobjc.dll

# spec files for msvcrt*.dll configurations
cd gcc
for n in msvcrt msvcrt20 msvcrt40; do
	sed "s/crtdll/$n/g" <specs | sed "s/crt1/crt2/g" >specs.$n
done
)

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT%{_datadir}
(cd obj-%{target_platform}

%{__make} install \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	bindir=$RPM_BUILD_ROOT%{arch}/bin \
	mandir=$RPM_BUILD_ROOT%{_mandir} \
	infodir=$RPM_BUILD_ROOT%{_infodir} \
	gxx_include_dir=$RPM_BUILD_ROOT%{arch}/include/g++

cd gcc
install specs.msvcrt specs.msvcrt20 specs.msvcrt40 $RPM_BUILD_ROOT%{gcclib}
)

mv -f $RPM_BUILD_ROOT%{arch}/bin/%{target}-* $RPM_BUILD_ROOT%{_bindir}

# c++filt is provided by binutils
rm -f $RPM_BUILD_ROOT%{_bindir}/i386-mingw32-c++filt

# what is this there for???
rm -f $RPM_BUILD_ROOT%{_libdir}/libiberty.a

# the same... make hardlink
ln -f $RPM_BUILD_ROOT%{arch}/bin/gcc $RPM_BUILD_ROOT%{_bindir}/%{target}-gcc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{target}-gcc
%attr(755,root,root) %{_bindir}/%{target}-*protoize
%dir %{arch}/bin
%attr(755,root,root) %{arch}/bin/cpp
%attr(755,root,root) %{arch}/bin/gcc
%attr(755,root,root) %{arch}/bin/gcov
%{arch}/include/_G_config.h
%{arch}/lib/libiberty.a
%dir %{gccarch}
%dir %{gcclib}
%attr(755,root,root) %{gcclib}/cc1
%attr(755,root,root) %{gcclib}/cpp0
%{gcclib}/SYSCALLS.c.X
%{gcclib}/libgcc.a
%{gcclib}/specs*
%dir %{gcclib}/include
%{gcclib}/include/float.h
%{gcclib}/include/iso646.h
%{gcclib}/include/limits.h
%{gcclib}/include/proto.h
%{gcclib}/include/stdarg.h
%{gcclib}/include/stdbool.h
%{gcclib}/include/stddef.h
%{gcclib}/include/syslimits.h
%{gcclib}/include/varargs.h
%{gcclib}/include/va-*.h
%{_mandir}/man1/%{target}-gcc.1*

%files c++
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{target}-[cg]++
%{arch}/include/g++
%{arch}/lib/libstdc++.a
%attr(755,root,root) %{gcclib}/cc1plus
%{gcclib}/libstdc++*
%{gcclib}/include/new.h
%{gcclib}/include/exception
%{gcclib}/include/new
%{gcclib}/include/typeinfo
%{_mandir}/man1/%{target}-g++.1*

%files objc
%defattr(644,root,root,755)
%attr(755,root,root) %{gcclib}/cc1obj
%{gcclib}/libobjc.a
%{gcclib}/include/objc

%files g77
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{target}-g77
%attr(755,root,root) %{gcclib}/f771
%{_mandir}/man1/%{target}-g77.1*

%files chill
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{target}-chill
%attr(755,root,root) %{gcclib}/cc1chill
%{gcclib}/chillrt0.o
%{gcclib}/libchill.a

%files java
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{target}-gcj
%attr(755,root,root) %{arch}/bin/gcjh
%attr(755,root,root) %{arch}/bin/jcf-dump
%attr(755,root,root) %{arch}/bin/jv-scan
%attr(755,root,root) %{gcclib}/jc1
%attr(755,root,root) %{gcclib}/jvgenmain
