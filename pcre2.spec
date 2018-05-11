#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x9766E084FB0F43D8 (ph10@cam.ac.uk)
#
Name     : pcre2
Version  : 10.31
Release  : 15
URL      : https://sourceforge.net/projects/pcre/files/pcre2/10.31/pcre2-10.31.tar.gz
Source0  : https://sourceforge.net/projects/pcre/files/pcre2/10.31/pcre2-10.31.tar.gz
Source99 : https://sourceforge.net/projects/pcre/files/pcre2/10.31/pcre2-10.31.tar.gz.sig
Summary  : PCRE2 - Perl compatible regular expressions C library (2nd API) with 32 bit character support
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pcre2-bin
Requires: pcre2-lib
Requires: pcre2-doc
BuildRequires : bzip2-dev
BuildRequires : pkgconfig(valgrind)
BuildRequires : pkgconfig(zlib)
BuildRequires : zlib-dev
Patch1: cve-2017-8399.nopatch

%description
------------------------------------------------------------------
PCRE2 is a re-working of the original PCRE library to provide an entirely new
API. The latest release of PCRE2 is always available in three alternative
formats from:

%package bin
Summary: bin components for the pcre2 package.
Group: Binaries

%description bin
bin components for the pcre2 package.


%package dev
Summary: dev components for the pcre2 package.
Group: Development
Requires: pcre2-lib
Requires: pcre2-bin
Provides: pcre2-devel

%description dev
dev components for the pcre2 package.


%package doc
Summary: doc components for the pcre2 package.
Group: Documentation

%description doc
doc components for the pcre2 package.


%package lib
Summary: lib components for the pcre2 package.
Group: Libraries

%description lib
lib components for the pcre2 package.


%prep
%setup -q -n pcre2-10.31

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1526014098
export CFLAGS="$CFLAGS -fstack-protector-strong -mzero-caller-saved-regs=used "
export FCFLAGS="$CFLAGS -fstack-protector-strong -mzero-caller-saved-regs=used "
export FFLAGS="$CFLAGS -fstack-protector-strong -mzero-caller-saved-regs=used "
export CXXFLAGS="$CXXFLAGS -fstack-protector-strong -mzero-caller-saved-regs=used "
%configure --disable-static --enable-pcre2-16 \
--enable-unicode
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1526014098
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/pcre2-config
/usr/bin/pcre2grep
/usr/bin/pcre2test

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
/usr/lib64/libpcre2-16.so
/usr/lib64/libpcre2-8.so
/usr/lib64/libpcre2-posix.so
/usr/lib64/pkgconfig/libpcre2-16.pc
/usr/lib64/pkgconfig/libpcre2-8.pc
/usr/lib64/pkgconfig/libpcre2-posix.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/doc/pcre2/*
%doc /usr/share/man/man1/*
%doc /usr/share/man/man3/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libpcre2-16.so.0
/usr/lib64/libpcre2-16.so.0.7.0
/usr/lib64/libpcre2-8.so.0
/usr/lib64/libpcre2-8.so.0.7.0
/usr/lib64/libpcre2-posix.so.2
/usr/lib64/libpcre2-posix.so.2.0.0
