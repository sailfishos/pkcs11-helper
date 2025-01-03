Name:       pkcs11-helper
Summary:    A library for using PKCS#11 providers
Version:    1.30.0
Release:    1
License:    GPLv2 or BSD
URL:        https://github.com/OpenSC/pkcs11-helper
Source0:    %{name}-%{version}.tar.bz2
Patch1:     0001-openssl-fix-openssl_ex_data_dup-prototype-for-openss.patch
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  autoconf
BuildRequires:  libtool
BuildRequires:  pkgconfig(openssl)

%description
pkcs11-helper is a library that simplifies the interaction with PKCS#11
providers for end-user applications using a simple API and optional OpenSSL
engine. The library allows using multiple PKCS#11 providers at the same time,
enumerating available token certificates, or selecting a certificate directly
by serialized id, handling card removal and card insert events, handling card
re-insert to a different slot, supporting session expiration and much more all
using a simple API.


%package devel
Summary:    Development files for pkcs11-helper
Requires:   %{name} = %{version}-%{release}
Requires:   pkgconfig(openssl)
# For /usr/share/aclocal
Requires:   automake

%description devel
This package contains header files and documentation necessary for developing
programs using the pkcs11-helper library.


%package doc
Summary:    Documentation for %{name}
BuildArch:  noarch
Requires:   %{name} = %{version}-%{release}

%description doc
%{summary}.


%prep
%autosetup -p1 -n %{name}-%{version}/upstream

%build
%reconfigure --disable-static --disable-doc
%make_build

%install
%make_install

# Use %%doc to properly install README in a standard location
rm -rf $RPM_BUILD_ROOT%{_datadir}/doc/%{name}/

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%license COPYING COPYING.BSD COPYING.GPL
%{_libdir}/libpkcs11-helper.so.*

%files devel
%{_includedir}/pkcs11-helper-1.0/
%{_libdir}/libpkcs11-helper.so
%{_libdir}/pkgconfig/libpkcs11-helper-1.pc
%{_datadir}/aclocal/pkcs11-helper-1.m4

%files doc
%doc ChangeLog README
%{_mandir}/man8/pkcs11-helper-1.8*
