%define major                 1
%define libname               %mklibname netfilter_queue %{major}
%define libnamedevel          %mklibname netfilter_queue -d
%define libnamedevelold       %{mklibname netfilter_queue 1}-devel
%define libnamestaticdevel    %mklibname netfilter_queue -d -s
%define libnamestaticdevelold %{mklibname netfilter_queue 1}-static-devel

Name:           libnetfilter_queue
Version:        0.0.15
Release:        %mkrel 2
Epoch:          0
Summary:        Provides an API for packets that have been queued by the kernel packet filter
Group:          System/Libraries
License:        GPL
URL:            http://www.netfilter.org/projects/libnetfilter_queue/index.html
Source0:        http://www.netfilter.org/projects/libnetfilter_queue/files/libnetfilter_queue-%{version}.tar.bz2
Source1:        http://www.netfilter.org/projects/libnetfilter_queue/files/libnetfilter_queue-%{version}.tar.bz2.sig
BuildRequires:  nfnetlink-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

%description
libnetfilter_queue is a userspace library providing an API to
packets that have been queued by the kernel packet filter. It is
part of a system that deprecates the old ip_queue/libipq mechanism.

%package -n %{libname}
Summary:        Main library for %{name}
Group:          System/Libraries
Provides:       %{name} = %{epoch}:%{version}-%{release}
Provides:       netfilter_queue = %{epoch}:%{version}-%{release}

%description -n %{libname}
libnetfilter_queue is a userspace library providing an API for
packets that have been queued by the kernel packet filter. It is
part of a system that deprecates the old ip_queue/libipq mechanism.

%package -n %{libnamedevel}
Summary:        Development files for %{name}
Group:          System/Libraries
Obsoletes:      %{libnamedevelold} < %{epoch}:%{version}-%{release}
Provides:       netfilter_queue-devel = %{epoch}:%{version}-%{release}
Requires:       %{libname} = %{epoch}:%{version}-%{release}

%description -n %{libnamedevel}
This package contains the development files for %{name}.

%package -n %{libnamestaticdevel}
Summary:        Static development files for %{name}
Group:          System/Libraries
Obsoletes:      %{libnamestaticdevelold} < %{epoch}:%{version}-%{release}
Provides:       netfilter_queue-static-devel = %{epoch}:%{version}-%{release}
Requires:       %{libnamedevel} = %{epoch}:%{version}-%{release}

%description -n %{libnamestaticdevel}
This package contains the static development files for %{name}.

%prep
%setup -q

%build
%{configure2_5x}
%{make}

%install
%{__rm} -rf %{buildroot}
%{makeinstall_std}

%check
%{make} check

%clean
%{__rm} -rf %{buildroot}

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%defattr(-,root,root,-)
%doc COPYING
%{_libdir}/*.so.*

%files -n %{libnamedevel}
%defattr(-,root,root,-)
%{_includedir}/libnetfilter_queue
%{_libdir}/*.so
%{_libdir}/pkgconfig/libnetfilter_queue.pc
%{_libdir}/*.la

%files -n %{libnamestaticdevel}
%defattr(-,root,root,-)
%{_libdir}/*.a
