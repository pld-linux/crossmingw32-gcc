Summary:	Mingw32 GNU Binary Utility Development Utilities - gcc
Name:		crossmingw32-gcc
# sources version is 2.95.2 but patched binaries use 2.95.3 in gcc-lib directory...
%define gccpreversion 2.95.3
%define gccversion 2.95.2
%define version 990111
Version:	%{version}
Release:	3
License:	GPL
Group:		Development/Tools
Group(pl):	Programowanie/Narzêdzia
ExclusiveArch:	%{ix86}
Source0:	ftp://ftp.gnu.org/pub/gnu/gcc-%{gccversion}.tar.gz
Patch0:		gcc-info.patch
#Patch1:	gcc-libgcj-config.patch
Patch2:		gcc-pld-linux.patch
Patch3:		gcc-libstdc++.patch
Patch4:		gcc-bootstrap.patch
Patch5:		gcc-cpp-macro-doc.patch
Patch6:		gcc-default-arch.patch
Patch7:		gcc-cvs-updates.patch
Patch8:		gcc-alpha-ev5-fix.patch
Patch9:		gcc-libstdc++-out-of-mem.patch
Patch10:	gcc-libstdc++-valarray.patch
Patch11:	gcc-libstdc++-wstring.patch
Patch12:	gcc-libstdc++-wall3.patch
Patch13:	gcc-libstdc++-bastring.patch
Patch14:	gcc-manpage.patch
Patch15:	gcc-cpp-dos-newlines.patch
Patch16:	gcc-g++-is-tree.patch
Patch17:	gcc-gpc.patch
Patch18:	gcc-arm-config.patch
Patch19:	gcc-m68k-pic.patch
Patch20:	gcc-sparc32-rfi.patch
Patch21:	gcc-builtin-apply.patch
Patch22:	gcc-ppc-ice.patch
Patch23:	gcc-ppc-descriptions.patch
Patch24:	gcc-ppc-andrew-dwarf-eh.patch
Patch25:	%{name}-libio.patch
Patch26:	%{name}-includes.patch
Patch27:	%{name}-libiberty.diff
BuildRequires:	crossmingw32-platform
BuildRequires:	crossmingw32-binutils
BuildRequires:	flex
BuildRequires:	bison
BuildRequires:	autoconf
Requires:	crossmingw32-binutils
Requires:	crossmingw32-platform
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define target i386-mingw32
%define target_platform i386-pc-mingw32
%define _prefix /usr
%define arch %{_prefix}/%{target}
%define gcclib %{_prefix}/lib/gcc-lib/%{target}/%{gccpreversion}
%define gccarch %{_prefix}/lib/gcc-lib/%{target}

%description
crossmingw32 is a complete cross-compiling development system for
building stand-alone Microsoft Windows applications under Linux using
the Mingw32 build libraries. This includes a binutils, gcc with g++
and objc, and libstdc++, all cross targeted to i386-mingw32, along
with supporting Win32 libraries in 'coff' format from free sources.

This package contains cross targeted gcc, g++, objc and libstdc++.

%prep

%setup -q -T -c -a0
(cd gcc-%{gccversion}
%patch0 -p1
#%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p0
%patch6 -p0
%patch7 -p1
%patch8 -p0
%patch9 -p0
%patch10 -p0
%patch11 -p0
%patch12 -p0
%patch13 -p0
%patch14 -p0
%patch15 -p0
%patch16 -p1
%patch17 -p1
%patch18 -p0
%patch19 -p0
%patch20 -p0
%patch21 -p0
%patch22 -p0
%patch23 -p0
%patch24 -p0

%patch25 -p1
%patch26 -p1
)

# libstdc++ - libiberty patch
(cd gcc-%{gccversion}
%patch27 -p1
cd libiberty
autoconf
)

%build

(cd gcc-%{gccversion}/gcc
autoconf
cd ..
rm -rf obj-%{target_platform}
install -d obj-%{target_platform}
cd obj-%{target_platform}

%{!?debug:CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s"} \
%{?debug:CFLAGS="-g -O" CXXFLAGS="-g -O" LDFLAGS=""} \
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
(cd gcc-%{gccversion}/obj-%{target_platform}

%{__make} install \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	bindir=$RPM_BUILD_ROOT%{arch}/bin \
	mandir=$RPM_BUILD_ROOT%{_mandir} \
	infodir=$RPM_BUILD_ROOT%{_infodir} \
	gxx_include_dir=$RPM_BUILD_ROOT%{arch}/include/g++

cd gcc
install specs.msvcrt specs.msvcrt20 specs.msvcrt40 $RPM_BUILD_ROOT%{gcclib}
mv -f $RPM_BUILD_ROOT%{arch}/bin/%{target}-* $RPM_BUILD_ROOT%{_bindir}

# c++filt is provided by binutils...
rm -f $RPM_BUILD_ROOT%{_bindir}/i386-mingw32-c++filt

# what's this there for???
rm -f $RPM_BUILD_ROOT%{_libdir}/libiberty.a
)

# libstdc++ is now provided by gcc...

#(cd gcc-%{gccversion}/libstdc++
#mkdir %{target}
#cd %{target}
#CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS" ../configure \
#	--prefix=%{prefix} \
#	--target=%{target} \
#	--exec-prefix=%{arch} \
#	--with-gxx-include-dir=%{arch}/include/g++
#
#make
#make install gxx_include_dir=$RPM_BUILD_ROOT%{arch}/include/g++
#)

# check if new rpm automation handles this properly:
#gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/%{target}-*
#strip $RPM_BUILD_ROOT%{_bindir}/%{target}-* || :
#strip $RPM_BUILD_ROOT%{gcclib}/{cc1,cc1chill,cc1obj,cc1plus,cpp,f771,jc1,jvgenmain}

%clean

rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{target}-*
%attr(755,root,root) %{arch}/bin/*
%{arch}/include/*
%{arch}/lib/*
%dir %{gccarch}
%dir %{gcclib}
%{gcclib}/include
%attr(755,root,root) %{gcclib}/cc1
%attr(755,root,root) %{gcclib}/cc1chill
%attr(755,root,root) %{gcclib}/cc1obj
%attr(755,root,root) %{gcclib}/cc1plus
%attr(755,root,root) %{gcclib}/cpp
%attr(755,root,root) %{gcclib}/f771
%attr(755,root,root) %{gcclib}/jc1
%attr(755,root,root) %{gcclib}/jvgenmain
%{gcclib}/SYSCALLS.c.X
%{gcclib}/chillrt0.o
%{gcclib}/libchill.a
%{gcclib}/libgcc.a
%{gcclib}/libobjc.a
%{gcclib}/specs*
%{_mandir}/man1/%{target}-*
