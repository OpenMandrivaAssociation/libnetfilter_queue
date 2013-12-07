%define major                 1
%define libname               %mklibname netfilter_queue %{major}
%define libnamedevel          %mklibname netfilter_queue -d

Summary:	Provides an API for packets that have been queued by the kernel packet filter
Name:		libnetfilter_queue
Version:	1.0.1
Release:	3
Epoch:		0
Group:		System/Libraries
License:	GPL
URL:		http://www.netfilter.org/projects/libnetfilter_queue/index.html
Source0:	http://www.netfilter.org/projects/libnetfilter_queue/files/libnetfilter_queue-%{version}.tar.bz2
Source1:	http://www.netfilter.org/projects/libnetfilter_queue/files/libnetfilter_queue-%{version}.tar.bz2.sig
BuildRequires:	nfnetlink-devel >= 0:0.0.38

%description
libnetfilter_queue is a userspace library providing an API to
packets that have been queued by the kernel packet filter. It is
part of a system that deprecates the old ip_queue/libipq mechanism.

%package -n %{libname}
Summary:	Main library for %{name}
Group:		System/Libraries
Provides:	%{name} = %{epoch}:%{version}-%{release}
Provides:	netfilter_queue = %{epoch}:%{version}-%{release}

%description -n %{libname}
libnetfilter_queue is a userspace library providing an API for
packets that have been queued by the kernel packet filter. It is
part of a system that deprecates the old ip_queue/libipq mechanism.

%package -n %{libnamedevel}
Summary:        Development files for %{name}
Group:          System/Libraries
Obsoletes:	%{mklibname netfilter_queue 1}-devel < %{epoch}:%{version}-%{release}
Obsoletes:	%{mklibname netfilter_queue -d -s} < %{epoch}:%{version}-%{release}
Provides:	netfilter_queue-devel = %{epoch}:%{version}-%{release}
Requires:	%{libname} = %{epoch}:%{version}-%{release}

%description -n %{libnamedevel}
This package contains the development files for %{name}.

%prep
%setup -q

%build
autoreconf -fi
%configure2_5x
%make

%check
make check

%install
%makeinstall_std

rm -f %{buildroot}%{_libdir}/*.la

%files -n %{libname}
%doc COPYING
%{_libdir}/*.so.%{major}*

%files -n %{libnamedevel}
%{_includedir}/libnetfilter_queue
%{_libdir}/*.so
%{_libdir}/pkgconfig/libnetfilter_queue.pc


%changelog
* Fri Apr 29 2011 Oden Eriksson <oeriksson@mandriva.com> 0:1.0.0-2mdv2011.0
+ Revision: 660271
- mass rebuild

* Thu Jul 15 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 0:1.0.0-1mdv2011.0
+ Revision: 553703
- update to new version 1.0.0

* Sun Sep 13 2009 Thierry Vignaud <tv@mandriva.org> 0:0.0.17-2mdv2010.0
+ Revision: 438719
- rebuild

* Mon Mar 16 2009 Jérôme Soyer <saispo@mandriva.org> 0:0.0.17-1mdv2009.1
+ Revision: 355843
- New upstream release

* Sun Jul 27 2008 David Walluck <walluck@mandriva.org> 0:0.0.16-1mdv2009.0
+ Revision: 250517
- 0.0.16

* Tue Jul 22 2008 Thierry Vignaud <tv@mandriva.org> 0:0.0.15-4mdv2009.0
+ Revision: 240983
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Tue Sep 04 2007 David Walluck <walluck@mandriva.org> 0:0.0.15-2mdv2008.0
+ Revision: 79236
- chrpath is no longer required when building
- 0.0.15
- new lib policy

* Thu May 24 2007 David Walluck <walluck@mandriva.org> 0:0.0.13-3mdv2008.0
+ Revision: 30590
- rebuild

* Thu May 24 2007 David Walluck <walluck@mandriva.org> 0:0.0.13-2mdv2008.0
+ Revision: 30565
- rebuild for new libnfnetlink-devel

* Wed May 23 2007 David Walluck <walluck@mandriva.org> 0:0.0.13-1mdv2008.0
+ Revision: 30371
- 0.13


* Fri Sep 15 2006 David Walluck <walluck@mandriva.org> 0:0.0.12-1mdv2007.0
- release

