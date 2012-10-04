Summary:	Realtime Audio Utility Library
Name:		raul
Version:	0.8.0
Release:	2
License:	GPL v2
Group:		Libraries
Source0:	http://download.drobilla.net/%{name}-%{version}.tar.bz2
# Source0-md5:	8fa71a20db81fbed5fb6516dea383ea8
Patch0:		%{name}-buildfix.patch
BuildRequires:	boost-devel
BuildRequires:	gtkmm-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
RAUL is a C++ utility library primarily aimed at audio/musical
applications.

%package devel
Summary:	Header files for RAUL library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This is the package containing the header files for RAUL library.

%prep
%setup -q
%patch0 -p1

%build
export CC="%{__cc}"
export CXX="%{__cxx}"
export CCFLAGS="%{rpmcflags}"
export CXXFLAGS="%{rpmcxxflags}"
./waf -v configure \
	--prefix=%{_prefix}	\
	--libdir=%{_libdir}	\
	--nocache
./waf -v build

%install
rm -rf $RPM_BUILD_ROOT

./waf -v install	\
	--destdir=$RPM_BUILD_ROOT

chmod +x $RPM_BUILD_ROOT%{_libdir}/*.so*

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %ghost %{_libdir}/libraul.so.??
%attr(755,root,root) %{_libdir}/libraul.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libraul.so
%{_includedir}/raul
%{_pkgconfigdir}/*.pc

