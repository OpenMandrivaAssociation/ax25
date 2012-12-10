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
BuildRequires:	zlib-devel
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


%changelog
* Fri Oct 08 2010 Jani Välimaa <wally@mandriva.org> 0.0.12-0.rc2.1mdv2011.0
+ Revision: 584209
- add missing BR
- new version 0.0.12 rc2
- clean spec
- fix url and license

* Wed Sep 02 2009 Thierry Vignaud <tv@mandriva.org> 0.0.11-11mdv2010.0
+ Revision: 424585
- use %%configure2_5x
- rebuild
- rebuild

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0.0.11-9mdv2009.0
+ Revision: 243098
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Tue Mar 25 2008 Emmanuel Andry <eandry@mandriva.org> 0.0.11-7mdv2008.1
+ Revision: 189880
- Fix groups

* Thu Dec 20 2007 Olivier Blin <oblin@mandriva.com> 0.0.11-6mdv2008.1
+ Revision: 135826
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - import ax25


* Mon Jul 31 2006 Lenny Cartier <lenny@mandriva.com> 0.0.11-6mdv2007.0
- rebuild

* Tue May 16 2006 Lenny Cartier <lenny@mandriva.com> 0.0.11-5mdk
- rebuild

* Fri Apr 08 2005 Olivier Thauvin <nanardon@mandrake.org> 0.0.11-4mdk
- reupload

* Thu Jun 03 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.0.11-3mdk
- provides ax25-devel

* Mon May 24 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.0.11-2mdk
- rename libraries packages

* Sat Mar 22 2003 Lenny Cartier <lenny@mandrakesoft.com> 0.0.11-1mdk
- 0.0.11

* Fri Jan 17 2003 Lenny Cartier <lenny@mandrakesoft.com> 0.0.10-2mdk
- rebuild

* Thu May 16 2002 Lenny Cartier <lenny@mandrakesoft.com> 0.0.10-1mdk
- 0.0.10
- fix spec

* Mon Aug 20 2001  Lenny Cartier <lenny@mandrakesoft.com> 0.0.7-5mdk
- rebuild

* Thu Jun 14 2001 Lenny Cartier <lenny@mandrakesoft.com> 0.0.7-4mdk
- fixed by Laurent Grawet <laurent.grawet@ibelgique.com> :
	- Corrected group

* Fri Aug 08 2000 Lenny Cartier <lenny@mandrakesoft.com> 0.0.7-3mdk
- clean spec

* Thu Jul 27 2000 Lenny Cartier <lenny@mandrakesoft.com> 0.0.7-2mdk
- macros
- bm

* Tue Jun 27 2000 Lenny Cartier <lenny@mandrakesoft.com> 0.0.7-1mdk
- new in contribs
