%define major 1
%define libname %mklibname netfilter_queue %{major}
%define libnamedevel %mklibname netfilter_queue -d

Summary:	Provides an API for packets that have been queued by the kernel packet filter
Name:		libnetfilter_queue
Version:	1.0.3
Release:	1
Group:		System/Libraries
License:	GPL
URL:		http://www.netfilter.org/projects/libnetfilter_queue/index.html
Source0:	http://www.netfilter.org/projects/libnetfilter_queue/files/libnetfilter_queue-%{version}.tar.bz2
BuildRequires:	nfnetlink-devel >= 0:0.0.38
BuildRequires:	pkgconfig(libmnl)

%description
libnetfilter_queue is a userspace library providing an API to
packets that have been queued by the kernel packet filter. It is
part of a system that deprecates the old ip_queue/libipq mechanism.

%package -n %{libname}
Summary:	Main library for %{name}
Group:		System/Libraries
Provides:	%{name} = %{EVRD}
Provides:	netfilter_queue = %{EVRD}

%description -n %{libname}
libnetfilter_queue is a userspace library providing an API for
packets that have been queued by the kernel packet filter. It is
part of a system that deprecates the old ip_queue/libipq mechanism.

%package -n %{libnamedevel}
Summary:        Development files for %{name}
Group:          System/Libraries
Obsoletes:	%{mklibname netfilter_queue 1}-devel < %{EVRD}
Obsoletes:	%{mklibname netfilter_queue -d -s} < %{EVRD}
Provides:	netfilter_queue-devel = %{EVRD}
Requires:	%{libname} = %{EVRD}

%description -n %{libnamedevel}
This package contains the development files for %{name}.

%prep
%autosetup -p1

%build
autoreconf -fi
%configure
%make_build

%install
%make_install

rm -f %{buildroot}%{_libdir}/*.la

%files -n %{libname}
%doc COPYING
%{_libdir}/*.so.%{major}*

%files -n %{libnamedevel}
%{_includedir}/libnetfilter_queue
%{_libdir}/*.so
%{_libdir}/pkgconfig/libnetfilter_queue.pc
