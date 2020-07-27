#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
%define keepstatic 1
Name     : numactl
Version  : 2.0.13
Release  : 22
URL      : file:///insilications/build/clearlinux/packages/numactl/numactl-v2.0.13.zip
Source0  : file:///insilications/build/clearlinux/packages/numactl/numactl-v2.0.13.zip
Summary  : libnuma libraries
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.0 LGPL-2.1
Requires: numactl-bin = %{version}-%{release}
Requires: numactl-lib = %{version}-%{release}
Requires: numactl-man = %{version}-%{release}
BuildRequires : findutils
BuildRequires : gcc-dev
BuildRequires : glibc-dev
BuildRequires : util-linux
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Simple NUMA policy support. It consists of a numactl program to run
other programs with a specific NUMA policy.

%package bin
Summary: bin components for the numactl package.
Group: Binaries

%description bin
bin components for the numactl package.


%package dev
Summary: dev components for the numactl package.
Group: Development
Requires: numactl-lib = %{version}-%{release}
Requires: numactl-bin = %{version}-%{release}
Provides: numactl-devel = %{version}-%{release}
Requires: numactl = %{version}-%{release}

%description dev
dev components for the numactl package.


%package lib
Summary: lib components for the numactl package.
Group: Libraries

%description lib
lib components for the numactl package.


%package man
Summary: man components for the numactl package.
Group: Default

%description man
man components for the numactl package.


%package staticdev
Summary: staticdev components for the numactl package.
Group: Default
Requires: numactl-dev = %{version}-%{release}

%description staticdev
staticdev components for the numactl package.


%prep
%setup -q -n numactl-v2.0.13
cd %{_builddir}/numactl-v2.0.13

%build
unset http_proxy
unset https_proxy
unset no_proxy
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1595847236
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
## altflags1 content
export CFLAGS="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe"
# -ffat-lto-objects -fno-PIE -fno-PIE -m64 -no-pie -fpic -fvisibility=hidden
# gcc: -feliminate-unused-debug-types -fipa-pta -flto=16 -Wno-error -Wp,-D_REENTRANT -fno-common
export CXXFLAGS="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -fvisibility-inlines-hidden -pipe"
#
export FCFLAGS="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe"
export FFLAGS="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe"
export CFFLAGS="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe"
#
export LDFLAGS="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe"
#
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
#export CCACHE_DISABLE=1
## altflags1 end
%autogen  --enable-shared --enable-static
make  %{?_smp_mflags}  V=1 VERBOSE=1

%check
export LANG=C.UTF-8
unset http_proxy
unset https_proxy
unset no_proxy
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1595847236
rm -rf %{buildroot}
%make_install
## Remove excluded files
rm -f %{buildroot}/usr/share/man/man2/move_pages.2

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/memhog
/usr/bin/migratepages
/usr/bin/migspeed
/usr/bin/numactl
/usr/bin/numademo
/usr/bin/numastat

%files dev
%defattr(-,root,root,-)
/usr/include/numa.h
/usr/include/numacompat1.h
/usr/include/numaif.h
/usr/lib64/libnuma.so
/usr/lib64/pkgconfig/numa.pc
/usr/share/man/man3/numa.3

%files lib
%defattr(-,root,root,-)
/usr/lib64/libnuma.so.1
/usr/lib64/libnuma.so.1.0.0

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man8/memhog.8
/usr/share/man/man8/migratepages.8
/usr/share/man/man8/migspeed.8
/usr/share/man/man8/numactl.8
/usr/share/man/man8/numastat.8

%files staticdev
%defattr(-,root,root,-)
/usr/lib64/libnuma.a
