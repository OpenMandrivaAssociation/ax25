%define name	ax25
%define version	0.0.12
%define prerel	rc2
%define release	1

%define major		_0
%define libname		%mklibname %{name} %{major}
%define libnamedev	%mklibname %{name} %{major} -d

Name:		%{name}
Summary:	Libraries for Amateur AX25 
Version:	%{version}
Release:	%mkrel -c %{prerel} %{release}
Source:		http://www.linux-ax25.org/pub/libax25/lib%{name}-%{version}-%{prerel}.tar.gz
Url:		http://www.linux-ax25.org/wiki/LinuxAX25
Group:		Communications
BuildRoot:	%{_tmppath}/%{name}-buildroot
License:	LGPLv2+

%description
Libraries for Amateur AX25.

This package is split off from the previous ax25-utils.

%package -n %{libname}
Summary:	Libraries for Amateur AX25 
Group:		System/Libraries
Obsoletes:	libax25
Provides:	libax25

%description -n %{libname}
Libraries for Amateur AX25.

%package -n %{libnamedev}
Summary:	Development package for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	libax25-devel
Provides:	ax25-devel
Obsoletes:	libax25-devel

%description -n %{libnamedev}
Development package for %{name}.
This package is split off from the previous ax25-utils.

%prep
%setup -q -n lib%{name}-%{version}-%{prerel}
%configure2_5x --disable-static

%build

#fix build
sed -i -e 's|LIBS =|LIBS = -lz|' Makefile

%make

%install
rm -rf %{buildroot}
%makeinstall_std

#we don't want these
find %{buildroot} -name "*.la" -exec rm -rf {} \;

%clean
rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%doc README ChangeLog AUTHORS NEWS
%{_libdir}/*.so.*
%{_mandir}/man5/*

%files -n %{libnamedev}
%defattr(-,root,root)
%{_libdir}/*.so
%{_mandir}/man3/*
%{_includedir}/netax25/*
