Name:		redis3m
Version:	2.0
Release:	1%{?dist}
Summary:	A C++ Redis client
Group:		System Environment/Libraries
License:	Apache 2.0
URL:		https://github.com/luca3m/redis3m
Source:		redis3m-master.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Packager:	Alexander Hurd <hurdad@gmail.com>

%description
A C++ Redis client

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q -n redis3m-master

%build
cmake -DCMAKE_INSTALL_PREFIX=/usr -DLIB_SUFFIX=64 .
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%post
ldconfig

%postun
ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_datadir}/
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root,-)
%{_includedir}/redis3m
%{_libdir}/*.so
%{_libdir}/pkgconfig/redis3m.pc

%changelog
* Mon Apr 4 2016 Alexander Hurd <hurdad@gmail.com> 1.0.1-1
- Initial specfile writeup.