%define lib_major       1
%define lib_name_orig   %mklibname netfilter_queue
%define lib_name        %{lib_name_orig}%{lib_major}

Name:           libnetfilter_queue
Version:        0.0.12
Release:        %mkrel 2
Epoch:          0
Summary:        Provides an API for packets that have been queued by the kernel packet filter
Group:          System/Libraries
License:        GPL
URL:            http://www.netfilter.org/projects/%{name}/index.html
Source0:        http://ftp.netfilter.org/pub/%{name}/%{name}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires:  chrpath
BuildRequires:  libnfnetlink-devel

%description
libnetfilter_queue is a userspace library providing an API to
packets that have been queued by the kernel packet filter. It is
part of a system that deprecates the old ip_queue/libipq mechanism.

%package -n %{lib_name}
Summary:        Main library for %{name}
Group:          System/Libraries
Provides:       %{lib_name_orig} = %{epoch}:%{version}-%{release}
Provides:       %{name} = %{epoch}:%{version}-%{release}

%description -n %{lib_name}
libnetfilter_queue is a userspace library providing an API for
packets that have been queued by the kernel packet filter. It is
part of a system that deprecates the old ip_queue/libipq mechanism.

%package -n %{lib_name}-devel
Summary:        Development files for %{name}
Group:          System/Libraries
Requires:       %{lib_name} = %{epoch}:%{version}-%{release}
Provides:       %{lib_name_orig}-devel = %{epoch}:%{version}-%{release}
Provides:       %{name}-devel = %{epoch}:%{version}-%{release}
Provides:       lib%{name}-devel = %{epoch}:%{version}-%{release}

%description -n %{lib_name}-devel
This package contains the development files for %{name}.

%package -n %{lib_name}-static-devel
Summary:        Static development files for %{name}
Group:          System/Libraries
Requires:       %{lib_name}-devel = %{epoch}:%{version}-%{release}
Provides:       %{lib_name_orig}-static-devel = %{epoch}:%{version}-%{release}
Provides:       %{name}-static-devel = %{epoch}:%{version}-%{release}
Provides:       lib%{name}-static-devel = %{epoch}:%{version}-%{release}

%description -n %{lib_name}-static-devel
This package contains the static development files for %{name}.

%prep
%setup -q

%build
%configure2_5x
%make

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{_bindir}/chrpath -d %{buildroot}%{_libdir}/libnetfilter_queue_libipq.so.%{lib_major}.*.*

%check
%make check

%clean
%{__rm} -rf %{buildroot}

%post -n %{lib_name} -p /sbin/ldconfig

%postun -n %{lib_name} -p /sbin/ldconfig

%files -n %{lib_name}
%defattr(-,root,root,-)
%doc ChangeLog COPYING
%{_libdir}/*.so.*

%files -n %{lib_name}-devel
%defattr(-,root,root,-)
%{_includedir}/%{name}
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/*.la

%files -n %{lib_name}-static-devel
%defattr(-,root,root,-)
%{_libdir}/*.a


