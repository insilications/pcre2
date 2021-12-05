#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
%define keepstatic 1
Name     : pcre2
Version  : 10.39
Release  : 505
URL      : file:///aot/build/clearlinux/packages/pcre2/pcre2-v10.39.tar.gz
Source0  : file:///aot/build/clearlinux/packages/pcre2/pcre2-v10.39.tar.gz
Summary  : Posix compatible interface to libpcre2-8
Group    : Development/Tools
License  : FTL GPL-2.0+ MIT Zlib
Requires: pcre2-bin = %{version}-%{release}
Requires: pcre2-lib = %{version}-%{release}
Requires: pcre2-man = %{version}-%{release}
BuildRequires : buildreq-configure
BuildRequires : bzip2-dev
BuildRequires : bzip2-dev32
BuildRequires : bzip2-staticdev
BuildRequires : findutils
BuildRequires : gcc
BuildRequires : gcc-dev
BuildRequires : gcc-dev32
BuildRequires : gcc-doc
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libs-math
BuildRequires : gcc-libstdc++32
BuildRequires : gcc-libubsan
BuildRequires : gcc-locale
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : libgcc1
BuildRequires : libstdc++
BuildRequires : pkgconfig(valgrind)
BuildRequires : zlib-dev
BuildRequires : zlib-dev32
BuildRequires : zlib-staticdev
BuildRequires : zlib-staticdev32
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
------------------------------------------------------------------
PCRE2 is a re-working of the original PCRE1 library to provide an entirely new
API. Since its initial release in 2015, there has been further development of
the code and it now differs from PCRE1 in more than just the API. There are new
features, and the internals have been improved. The original PCRE1 library is
now obsolete and no longer maintained. The latest release of PCRE2 is available
in .tar.gz, tar.bz2, or .zip form from this GitHub repository:

%package bin
Summary: bin components for the pcre2 package.
Group: Binaries

%description bin
bin components for the pcre2 package.


%package dev
Summary: dev components for the pcre2 package.
Group: Development
Requires: pcre2-lib = %{version}-%{release}
Requires: pcre2-bin = %{version}-%{release}
Provides: pcre2-devel = %{version}-%{release}
Requires: pcre2 = %{version}-%{release}

%description dev
dev components for the pcre2 package.


%package dev32
Summary: dev32 components for the pcre2 package.
Group: Default
Requires: pcre2-lib32 = %{version}-%{release}
Requires: pcre2-bin = %{version}-%{release}
Requires: pcre2-dev = %{version}-%{release}

%description dev32
dev32 components for the pcre2 package.


%package doc
Summary: doc components for the pcre2 package.
Group: Documentation
Requires: pcre2-man = %{version}-%{release}

%description doc
doc components for the pcre2 package.


%package lib
Summary: lib components for the pcre2 package.
Group: Libraries

%description lib
lib components for the pcre2 package.


%package lib32
Summary: lib32 components for the pcre2 package.
Group: Default

%description lib32
lib32 components for the pcre2 package.


%package man
Summary: man components for the pcre2 package.
Group: Default

%description man
man components for the pcre2 package.


%package staticdev
Summary: staticdev components for the pcre2 package.
Group: Default
Requires: pcre2-dev = %{version}-%{release}

%description staticdev
staticdev components for the pcre2 package.


%package staticdev32
Summary: staticdev32 components for the pcre2 package.
Group: Default
Requires: pcre2-dev32 = %{version}-%{release}

%description staticdev32
staticdev32 components for the pcre2 package.


%prep
%setup -q -n pcre2
cd %{_builddir}/pcre2
pushd %{_builddir}
cp -a %{_builddir}/pcre2 build32
popd

%build
unset http_proxy
unset https_proxy
unset no_proxy
export SSL_CERT_FILE=/var/cache/ca-certs/anchors/ca-certificates.crt
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1638700102
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
## altflags_pgo content
## pgo generate
export PGO_GEN="-fprofile-generate=/var/tmp/pgo -fprofile-dir=/var/tmp/pgo -fprofile-abs-path -fprofile-update=atomic -fprofile-arcs -ftest-coverage -fprofile-partial-training -fprofile-correction -freorder-functions --coverage -lgcov"
export CFLAGS_GENERATE="-Ofast --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=auto -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc $PGO_GEN"
export FCFLAGS_GENERATE="-Ofast --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=auto -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc $PGO_GEN"
export FFLAGS_GENERATE="-Ofast --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=auto -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc $PGO_GEN"
export CXXFLAGS_GENERATE="-Ofast --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=auto -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -fvisibility-inlines-hidden -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc $PGO_GEN"
export LDFLAGS_GENERATE="-Ofast --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=auto -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc $PGO_GEN"
export LIBS_GENERATE="-lgcov"
## pgo use
## -fno-tree-vectorize: disable -ftree-vectorize thus disable -ftree-loop-vectorize and -ftree-slp-vectorize -fopt-info-vec
## -Ofast -ffast-math
## -funroll-loops maybe dangerous
## -Wl,-z,max-page-size=0x1000
## -pthread -lpthread
## -Wl,-Bsymbolic-functions
export PGO_USE="-Wmissing-profile -Wcoverage-mismatch -fprofile-use=/var/tmp/pgo -fprofile-dir=/var/tmp/pgo -fprofile-abs-path -fprofile-update=atomic -fprofile-partial-training -fprofile-correction -freorder-functions"
export CFLAGS_USE="-g3 -ggdb -Ofast --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=auto -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc $PGO_USE"
export FCFLAGS_USE="-g3 -ggdb -Ofast --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=auto -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc $PGO_USE"
export FFLAGS_USE="-g3 -ggdb -Ofast --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=auto -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc $PGO_USE"
export CXXFLAGS_USE="-g3 -ggdb -Ofast --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=auto -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -fvisibility-inlines-hidden -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc $PGO_USE"
export LDFLAGS_USE="-g3 -ggdb -Ofast --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=auto -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc $PGO_USE"
#
export AR=/usr/bin/gcc-ar
export RANLIB=/usr/bin/gcc-ranlib
export NM=/usr/bin/gcc-nm
#
export MAKEFLAGS=%{?_smp_mflags}
#
%global _lto_cflags 1
#global _lto_cflags %{nil}
%global _disable_maintainer_mode 1
#%global _disable_maintainer_mode %{nil}
#
export CCACHE_DISABLE=true
export CCACHE_NOHASHDIR=true
export CCACHE_CPP2=true
export CCACHE_SLOPPINESS=pch_defines,time_macros,locale,file_stat_matches,file_stat_matches_ctime,include_file_ctime,include_file_mtime,modules,system_headers,clang_index_store,file_macro
#export CCACHE_SLOPPINESS=modules,include_file_mtime,include_file_ctime,time_macros,pch_defines,file_stat_matches,clang_index_store,system_headers,locale
#export CCACHE_SLOPPINESS=pch_defines,time_macros,locale,clang_index_store,file_macro
export CCACHE_DIR=/var/tmp/ccache
export CCACHE_BASEDIR=/builddir/build/BUILD
#export CCACHE_LOGFILE=/var/tmp/ccache/cache.debug
#export CCACHE_DEBUG=true
#export CCACHE_NODIRECT=true
#
export LD_LIBRARY_PATH="/usr/nvidia/lib64:/usr/nvidia/lib64/vdpau:/usr/nvidia/lib64/xorg/modules/drivers:/usr/nvidia/lib64/xorg/modules/extensions:/usr/local/cuda/lib64:/usr/lib64/haswell:/usr/lib64/haswell/pulseaudio:/usr/lib64/haswell/alsa-lib:/usr/lib64/haswell/gstreamer-1.0:/usr/lib64/haswell/pipewire-0.3:/usr/lib64/haswell/spa-0.2:/usr/lib64/dri:/usr/lib64/chromium:/usr/lib64:/usr/lib64/pulseaudio:/usr/lib64/alsa-lib:/usr/lib64/gstreamer-1.0:/usr/lib64/pipewire-0.3:/usr/lib64/spa-0.2:/usr/lib:/aot/intel/oneapi/compiler/latest/linux/compiler/lib/intel64_lin:/aot/intel/oneapi/compiler/latest/linux/lib:/aot/intel/oneapi/mkl/latest/lib/intel64:/aot/intel/oneapi/tbb/latest/lib/intel64/gcc4.8:/usr/share:/usr/lib64/wine:/usr/nvidia/lib32:/usr/nvidia/lib32/vdpau:/usr/lib32:/usr/lib32/wine"
#
export LIBRARY_PATH="/usr/nvidia/lib64:/usr/nvidia/lib64/vdpau:/usr/nvidia/lib64/xorg/modules/drivers:/usr/nvidia/lib64/xorg/modules/extensions:/usr/local/cuda/lib64:/usr/lib64/haswell:/usr/lib64/haswell/pulseaudio:/usr/lib64/haswell/alsa-lib:/usr/lib64/haswell/gstreamer-1.0:/usr/lib64/haswell/pipewire-0.3:/usr/lib64/haswell/spa-0.2:/usr/lib64/dri:/usr/lib64/chromium:/usr/lib64:/usr/lib64/pulseaudio:/usr/lib64/alsa-lib:/usr/lib64/gstreamer-1.0:/usr/lib64/pipewire-0.3:/usr/lib64/spa-0.2:/usr/lib:/aot/intel/oneapi/compiler/latest/linux/compiler/lib/intel64_lin:/aot/intel/oneapi/compiler/latest/linux/lib:/aot/intel/oneapi/mkl/latest/lib/intel64:/aot/intel/oneapi/tbb/latest/lib/intel64/gcc4.8:/usr/share:/usr/lib64/wine:/usr/nvidia/lib32:/usr/nvidia/lib32/vdpau:/usr/lib32:/usr/lib32/wine"
#
export PATH="/usr/lib64/ccache/bin:/usr/local/cuda/bin:/usr/nvidia/bin:/usr/bin/haswell:/usr/bin:/usr/sbin"
#
export CPATH="/usr/local/cuda/include"
#
export DISPLAY=:0
export __GL_SYNC_TO_VBLANK=1
export __GL_SYNC_DISPLAY_DEVICE=HDMI-0
export VDPAU_NVIDIA_SYNC_DISPLAY_DEVICE=HDMI-0
export LANG=en_US.UTF-8
export XDG_CONFIG_DIRS=/usr/share/xdg:/etc/xdg
export XDG_SEAT=seat0
export XDG_SESSION_TYPE=tty
export XDG_CURRENT_DESKTOP=KDE
export XDG_SESSION_CLASS=user
export XDG_VTNR=1
export XDG_SESSION_ID=1
export XDG_RUNTIME_DIR=/run/user/1000
export XDG_DATA_DIRS=/usr/local/share:/usr/share
export KDE_SESSION_VERSION=5
export KDE_SESSION_UID=1000
export KDE_FULL_SESSION=true
export KDE_APPLICATIONS_AS_SCOPE=1
export VDPAU_DRIVER=nvidia
export LIBVA_DRIVER_NAME=vdpau
export LIBVA_DRIVERS_PATH=/usr/lib64/dri
export GTK_RC_FILES=/etc/gtk/gtkrc
export FONTCONFIG_PATH=/usr/share/defaults/fonts
## altflags_pgo end
sd -r '\s--dirty\s' ' ' .
sd -r 'git describe' 'git describe --abbrev=0' .
if [ ! -f statuspgo ]; then
echo PGO Phase 1
export CFLAGS="${CFLAGS_GENERATE}"
export CXXFLAGS="${CXXFLAGS_GENERATE}"
export FFLAGS="${FFLAGS_GENERATE}"
export FCFLAGS="${FCFLAGS_GENERATE}"
export LDFLAGS="${LDFLAGS_GENERATE}"
export LIBS="${LIBS_GENERATE}"
%autogen  --enable-shared \
--enable-static \
--enable-pcre2-16 \
--enable-pcre2-32 \
--enable-unicode \
--enable-jit=yes
make  %{?_smp_mflags}  V=1 VERBOSE=1  V=1 VERBOSE=1

## profile_payload start
unset LD_LIBRARY_PATH
unset LIBRARY_PATH
make -j1 check VERBOSE=1 V=1 || :
export LD_LIBRARY_PATH="/usr/nvidia/lib64:/usr/nvidia/lib64/vdpau:/usr/nvidia/lib64/xorg/modules/drivers:/usr/nvidia/lib64/xorg/modules/extensions:/usr/local/cuda/lib64:/usr/lib64/haswell:/usr/lib64/haswell/pulseaudio:/usr/lib64/haswell/alsa-lib:/usr/lib64/haswell/gstreamer-1.0:/usr/lib64/haswell/pipewire-0.3:/usr/lib64/haswell/spa-0.2:/usr/lib64/dri:/usr/lib64/chromium:/usr/lib64:/usr/lib64/pulseaudio:/usr/lib64/alsa-lib:/usr/lib64/gstreamer-1.0:/usr/lib64/pipewire-0.3:/usr/lib64/spa-0.2:/usr/lib:/aot/intel/oneapi/compiler/latest/linux/compiler/lib/intel64_lin:/aot/intel/oneapi/compiler/latest/linux/lib:/aot/intel/oneapi/mkl/latest/lib/intel64:/aot/intel/oneapi/tbb/latest/lib/intel64/gcc4.8:/usr/share:/usr/lib64/wine:/usr/nvidia/lib32:/usr/nvidia/lib32/vdpau:/usr/lib32:/usr/lib32/wine"
export LIBRARY_PATH="/usr/nvidia/lib64:/usr/nvidia/lib64/vdpau:/usr/nvidia/lib64/xorg/modules/drivers:/usr/nvidia/lib64/xorg/modules/extensions:/usr/local/cuda/lib64:/usr/lib64/haswell:/usr/lib64/haswell/pulseaudio:/usr/lib64/haswell/alsa-lib:/usr/lib64/haswell/gstreamer-1.0:/usr/lib64/haswell/pipewire-0.3:/usr/lib64/haswell/spa-0.2:/usr/lib64/dri:/usr/lib64/chromium:/usr/lib64:/usr/lib64/pulseaudio:/usr/lib64/alsa-lib:/usr/lib64/gstreamer-1.0:/usr/lib64/pipewire-0.3:/usr/lib64/spa-0.2:/usr/lib:/aot/intel/oneapi/compiler/latest/linux/compiler/lib/intel64_lin:/aot/intel/oneapi/compiler/latest/linux/lib:/aot/intel/oneapi/mkl/latest/lib/intel64:/aot/intel/oneapi/tbb/latest/lib/intel64/gcc4.8:/usr/share:/usr/lib64/wine:/usr/nvidia/lib32:/usr/nvidia/lib32/vdpau:/usr/lib32:/usr/lib32/wine"
## profile_payload end
make clean || :
echo USED > statuspgo
fi
if [ -f statuspgo ]; then
echo PGO Phase 2
export CFLAGS="${CFLAGS_USE}"
export CXXFLAGS="${CXXFLAGS_USE}"
export FFLAGS="${FFLAGS_USE}"
export FCFLAGS="${FCFLAGS_USE}"
export LDFLAGS="${LDFLAGS_USE}"
export LIBS="${LIBS_USE}"
%autogen --enable-shared \
--enable-static \
--enable-pcre2-16 \
--enable-pcre2-32 \
--enable-unicode \
--enable-jit=yes
make  %{?_smp_mflags}  V=1 VERBOSE=1  V=1 VERBOSE=1
fi

pushd ../build32/
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
unset LD_LIBRARY_PATH
unset LIBRARY_PATH
unset CPATH
unset ASFLAGS
unset CFLAGS
unset CXXFLAGS
unset FCFLAGS
unset FFLAGS
unset CFFLAGS
unset LDFLAGS
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig:/usr/share/pkgconfig"
export ASFLAGS="--32"
export CFLAGS="-O2 -ffat-lto-objects -fuse-linker-plugin -pipe -fPIC -march=native -mtune=native -m32 -mstackrealign"
export CXXFLAGS="-O2 -ffat-lto-objects -fuse-linker-plugin -fvisibility-inlines-hidden -pipe -fPIC -march=native -mtune=native -m32 -mstackrealign"
export FCFLAGS="-O2 -ffat-lto-objects -fuse-linker-plugin -fvisibility-inlines-hidden -pipe -fPIC -march=native -mtune=native -m32 -mstackrealign"
export FFLAGS="-O2 -ffat-lto-objects -fuse-linker-plugin -fvisibility-inlines-hidden -pipe -fPIC -march=native -mtune=native -m32 -mstackrealign"
export CFFLAGS="-O2 -ffat-lto-objects -fuse-linker-plugin -fvisibility-inlines-hidden -pipe -fPIC -march=native -mtune=native -m32 -mstackrealign"
export LDFLAGS="-O2 -ffat-lto-objects -fuse-linker-plugin -pipe -fPIC -march=native -mtune=native -m32 -mstackrealign"
%autogen  --enable-shared \
--enable-static \
--enable-pcre2-16 \
--enable-pcre2-32 \
--enable-unicode \
--enable-jit=yes --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make  %{?_smp_mflags}  V=1 VERBOSE=1  V=1 VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1638700102
rm -rf %{buildroot}
pushd ../build32/
%make_install32 V=1 VERBOSE=1
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
    pushd %{buildroot}/usr/lib32/pkgconfig
    for i in *.pc ; do ln -s $i 32$i ; done
    popd
fi
if [ -d %{buildroot}/usr/share/pkgconfig ]
then
pushd %{buildroot}/usr/share/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
%make_install V=1 VERBOSE=1
## install_append content
install -dm 0755 %{buildroot}/usr/lib64/haswell/ || :
cp --archive %{buildroot}/usr/lib64/libpcre* %{buildroot}/usr/lib64/haswell/ || :
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/pcre2-config
/usr/bin/pcre2grep
/usr/bin/pcre2test

%files dev
%defattr(-,root,root,-)
/usr/include/pcre2.h
/usr/include/pcre2posix.h
/usr/lib64/haswell/libpcre2-16.la
/usr/lib64/haswell/libpcre2-16.so
/usr/lib64/haswell/libpcre2-32.la
/usr/lib64/haswell/libpcre2-32.so
/usr/lib64/haswell/libpcre2-8.la
/usr/lib64/haswell/libpcre2-8.so
/usr/lib64/haswell/libpcre2-posix.la
/usr/lib64/haswell/libpcre2-posix.so
/usr/lib64/libpcre2-16.la
/usr/lib64/libpcre2-16.so
/usr/lib64/libpcre2-32.la
/usr/lib64/libpcre2-32.so
/usr/lib64/libpcre2-8.la
/usr/lib64/libpcre2-8.so
/usr/lib64/libpcre2-posix.la
/usr/lib64/libpcre2-posix.so
/usr/lib64/pkgconfig/libpcre2-16.pc
/usr/lib64/pkgconfig/libpcre2-32.pc
/usr/lib64/pkgconfig/libpcre2-8.pc
/usr/lib64/pkgconfig/libpcre2-posix.pc

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libpcre2-16.la
/usr/lib32/libpcre2-16.so
/usr/lib32/libpcre2-32.la
/usr/lib32/libpcre2-32.so
/usr/lib32/libpcre2-8.la
/usr/lib32/libpcre2-8.so
/usr/lib32/libpcre2-posix.la
/usr/lib32/libpcre2-posix.so
/usr/lib32/pkgconfig/32libpcre2-16.pc
/usr/lib32/pkgconfig/32libpcre2-32.pc
/usr/lib32/pkgconfig/32libpcre2-8.pc
/usr/lib32/pkgconfig/32libpcre2-posix.pc
/usr/lib32/pkgconfig/libpcre2-16.pc
/usr/lib32/pkgconfig/libpcre2-32.pc
/usr/lib32/pkgconfig/libpcre2-8.pc
/usr/lib32/pkgconfig/libpcre2-posix.pc

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/pcre2/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/haswell/libpcre2-16.so.0
/usr/lib64/haswell/libpcre2-16.so.0.10.4
/usr/lib64/haswell/libpcre2-32.so.0
/usr/lib64/haswell/libpcre2-32.so.0.10.4
/usr/lib64/haswell/libpcre2-8.so.0
/usr/lib64/haswell/libpcre2-8.so.0.10.4
/usr/lib64/haswell/libpcre2-posix.so.3
/usr/lib64/haswell/libpcre2-posix.so.3.0.1
/usr/lib64/libpcre2-16.so.0
/usr/lib64/libpcre2-16.so.0.10.4
/usr/lib64/libpcre2-32.so.0
/usr/lib64/libpcre2-32.so.0.10.4
/usr/lib64/libpcre2-8.so.0
/usr/lib64/libpcre2-8.so.0.10.4
/usr/lib64/libpcre2-posix.so.3
/usr/lib64/libpcre2-posix.so.3.0.1

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libpcre2-16.so.0
/usr/lib32/libpcre2-16.so.0.10.4
/usr/lib32/libpcre2-32.so.0
/usr/lib32/libpcre2-32.so.0.10.4
/usr/lib32/libpcre2-8.so.0
/usr/lib32/libpcre2-8.so.0.10.4
/usr/lib32/libpcre2-posix.so.3
/usr/lib32/libpcre2-posix.so.3.0.1

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/pcre2-config.1
/usr/share/man/man1/pcre2grep.1
/usr/share/man/man1/pcre2test.1
/usr/share/man/man3/pcre2.3
/usr/share/man/man3/pcre2_callout_enumerate.3
/usr/share/man/man3/pcre2_code_copy.3
/usr/share/man/man3/pcre2_code_copy_with_tables.3
/usr/share/man/man3/pcre2_code_free.3
/usr/share/man/man3/pcre2_compile.3
/usr/share/man/man3/pcre2_compile_context_copy.3
/usr/share/man/man3/pcre2_compile_context_create.3
/usr/share/man/man3/pcre2_compile_context_free.3
/usr/share/man/man3/pcre2_config.3
/usr/share/man/man3/pcre2_convert_context_copy.3
/usr/share/man/man3/pcre2_convert_context_create.3
/usr/share/man/man3/pcre2_convert_context_free.3
/usr/share/man/man3/pcre2_converted_pattern_free.3
/usr/share/man/man3/pcre2_dfa_match.3
/usr/share/man/man3/pcre2_general_context_copy.3
/usr/share/man/man3/pcre2_general_context_create.3
/usr/share/man/man3/pcre2_general_context_free.3
/usr/share/man/man3/pcre2_get_error_message.3
/usr/share/man/man3/pcre2_get_mark.3
/usr/share/man/man3/pcre2_get_match_data_size.3
/usr/share/man/man3/pcre2_get_ovector_count.3
/usr/share/man/man3/pcre2_get_ovector_pointer.3
/usr/share/man/man3/pcre2_get_startchar.3
/usr/share/man/man3/pcre2_jit_compile.3
/usr/share/man/man3/pcre2_jit_free_unused_memory.3
/usr/share/man/man3/pcre2_jit_match.3
/usr/share/man/man3/pcre2_jit_stack_assign.3
/usr/share/man/man3/pcre2_jit_stack_create.3
/usr/share/man/man3/pcre2_jit_stack_free.3
/usr/share/man/man3/pcre2_maketables.3
/usr/share/man/man3/pcre2_maketables_free.3
/usr/share/man/man3/pcre2_match.3
/usr/share/man/man3/pcre2_match_context_copy.3
/usr/share/man/man3/pcre2_match_context_create.3
/usr/share/man/man3/pcre2_match_context_free.3
/usr/share/man/man3/pcre2_match_data_create.3
/usr/share/man/man3/pcre2_match_data_create_from_pattern.3
/usr/share/man/man3/pcre2_match_data_free.3
/usr/share/man/man3/pcre2_pattern_convert.3
/usr/share/man/man3/pcre2_pattern_info.3
/usr/share/man/man3/pcre2_serialize_decode.3
/usr/share/man/man3/pcre2_serialize_encode.3
/usr/share/man/man3/pcre2_serialize_free.3
/usr/share/man/man3/pcre2_serialize_get_number_of_codes.3
/usr/share/man/man3/pcre2_set_bsr.3
/usr/share/man/man3/pcre2_set_callout.3
/usr/share/man/man3/pcre2_set_character_tables.3
/usr/share/man/man3/pcre2_set_compile_extra_options.3
/usr/share/man/man3/pcre2_set_compile_recursion_guard.3
/usr/share/man/man3/pcre2_set_depth_limit.3
/usr/share/man/man3/pcre2_set_glob_escape.3
/usr/share/man/man3/pcre2_set_glob_separator.3
/usr/share/man/man3/pcre2_set_heap_limit.3
/usr/share/man/man3/pcre2_set_match_limit.3
/usr/share/man/man3/pcre2_set_max_pattern_length.3
/usr/share/man/man3/pcre2_set_newline.3
/usr/share/man/man3/pcre2_set_offset_limit.3
/usr/share/man/man3/pcre2_set_parens_nest_limit.3
/usr/share/man/man3/pcre2_set_recursion_limit.3
/usr/share/man/man3/pcre2_set_recursion_memory_management.3
/usr/share/man/man3/pcre2_set_substitute_callout.3
/usr/share/man/man3/pcre2_substitute.3
/usr/share/man/man3/pcre2_substring_copy_byname.3
/usr/share/man/man3/pcre2_substring_copy_bynumber.3
/usr/share/man/man3/pcre2_substring_free.3
/usr/share/man/man3/pcre2_substring_get_byname.3
/usr/share/man/man3/pcre2_substring_get_bynumber.3
/usr/share/man/man3/pcre2_substring_length_byname.3
/usr/share/man/man3/pcre2_substring_length_bynumber.3
/usr/share/man/man3/pcre2_substring_list_free.3
/usr/share/man/man3/pcre2_substring_list_get.3
/usr/share/man/man3/pcre2_substring_nametable_scan.3
/usr/share/man/man3/pcre2_substring_number_from_name.3
/usr/share/man/man3/pcre2api.3
/usr/share/man/man3/pcre2build.3
/usr/share/man/man3/pcre2callout.3
/usr/share/man/man3/pcre2compat.3
/usr/share/man/man3/pcre2convert.3
/usr/share/man/man3/pcre2demo.3
/usr/share/man/man3/pcre2jit.3
/usr/share/man/man3/pcre2limits.3
/usr/share/man/man3/pcre2matching.3
/usr/share/man/man3/pcre2partial.3
/usr/share/man/man3/pcre2pattern.3
/usr/share/man/man3/pcre2perform.3
/usr/share/man/man3/pcre2posix.3
/usr/share/man/man3/pcre2sample.3
/usr/share/man/man3/pcre2serialize.3
/usr/share/man/man3/pcre2syntax.3
/usr/share/man/man3/pcre2unicode.3

%files staticdev
%defattr(-,root,root,-)
/usr/lib64/haswell/libpcre2-16.a
/usr/lib64/haswell/libpcre2-32.a
/usr/lib64/haswell/libpcre2-8.a
/usr/lib64/haswell/libpcre2-posix.a
/usr/lib64/libpcre2-16.a
/usr/lib64/libpcre2-32.a
/usr/lib64/libpcre2-8.a
/usr/lib64/libpcre2-posix.a

%files staticdev32
%defattr(-,root,root,-)
/usr/lib32/libpcre2-16.a
/usr/lib32/libpcre2-32.a
/usr/lib32/libpcre2-8.a
/usr/lib32/libpcre2-posix.a
