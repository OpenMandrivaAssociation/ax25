%define name ax25
%define version 0.0.11
%define release %mkrel 9

%define major _0
%define libname %mklibname %{name} %major
%define libnamedev %mklibname %{name} %major -d

Name: %{name}
Summary: Libraries for Amateur AX25 
Version: %{version}
Release: %{release}
Source: lib%{name}-%{version}.tar.bz2
Url: http://ax25.sourceforge.net/
Group: Communications
BuildRoot: %{_tmppath}/%{name}-buildroot
License: GPL
Requires: kernel >= 2.2

%description
Libraries for Amateur AX25 (kernel >= 2.2).
This package is split off from the previous ax25-utils.

%package -n %libname
Summary: Libraries for Amateur AX25 
Group: System/Libraries
Obsoletes: libax25
Provides: libax25

%description -n %libname
Libraries for Amateur AX25 


%package -n %libnamedev
Summary: Development package for %{name}
Group: Development/C
Requires: %libname = %version
Provides: libax25-devel
Provides: ax25-devel
Obsoletes: libax25-devel

%description -n %libnamedev
Development package for %{name}
This package is split off from the previous ax25-utils.

%prep

%setup -q -n lib%{name}-%{version}

%configure

%build

%make

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post -n %libname -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %libname -p /sbin/ldconfig
%endif

%files -n %libname
%defattr(-,root,root)
%{_libdir}/*.so.*
%{_mandir}/man5/*

%doc README INSTALL ChangeLog AUTHORS NEWS

%files -n %libnamedev
%defattr(-,root,root)
%{_libdir}/*.so
%{_mandir}/man3/*
%{_libdir}/lib*.a
%{_libdir}/lib*.la
%{_includedir}/netax25/*

