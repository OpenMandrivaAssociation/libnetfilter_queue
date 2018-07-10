%define major                 1
%define libname               %mklibname netfilter_queue %{major}
%define libnamedevel          %mklibname netfilter_queue -d

Summary:	Provides an API for packets that have been queued by the kernel packet filter
Name:		libnetfilter_queue
Version:	1.0.2
Release:	4
Epoch:		0
Group:		System/Libraries
License:	GPL
URL:		http://www.netfilter.org/projects/libnetfilter_queue/index.html
Source0:	http://www.netfilter.org/projects/libnetfilter_queue/files/libnetfilter_queue-%{version}.tar.bz2
Source1:	http://www.netfilter.org/projects/libnetfilter_queue/files/libnetfilter_queue-%{version}.tar.bz2.sig
BuildRequires:	nfnetlink-devel >= 0:0.0.38
BuildRequires:	pkgconfig(libmnl)

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
%configure
%make

%check
make check

%install
%makeinstall_std

rm -f %{buildroot}%{_libdir}/*.la
rm %{buildroot}/%{_includedir}/internal.h

%files -n %{libname}
%doc COPYING
%{_libdir}/*.so.%{major}*

%files -n %{libnamedevel}
%{_includedir}/libnetfilter_queue
%{_libdir}/*.so
%{_libdir}/pkgconfig/libnetfilter_queue.pc
