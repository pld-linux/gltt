Summary:   	Gltt - library that allows use TrueType fonts in OpenGL application
Name:      	gltt
Version:   	2.4
Release:   	1
Copyright: 	LGPL
Group:     	Libraries
Group(pl):	Biblioteki
Source:    	http://home.worldnet.fr/~rehel/gltt/%{name}-%{version}.tar.gz
URL:       	http://home.worldnet.fr/~rehel/gltt/gltt.html
BuildRequires:	Mesa-devel
Requires:  	Mesa >= 2.6
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Gltt is a library that allows you to read and draw TrueType fonts in          
any OpenGL application.                                                       
It supports bitmapped and anti-aliased font drawing as well as                
vectorized and polygonized drawing.                                           

%package devel
Summary:   	Header files for gltt
Group:     	Development/Libraries
Requires:  	%{name} = %{version}

%description devel
This package contains the gltt header files required to develop gltt-based
applications.

%package static
Summary:   	gltt - static library and header files
Group:     	Development/Libraries
Requires:  	%{name}-devel = %{version}

%description static
This package contains the gltt static libraries.

%prep
%setup -q

%build
CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS" \
./configure %{_target_platform} \
	--prefix=/usr
make

%install
rm -rf $RPM_BUILD_ROOT
make prefix=$RPM_BUILD_ROOT/usr install

strip $RPM_BUILD_ROOT%{_libdir}/lib*.so.*.*

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%attr(755,root ,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root ,root,755)
%dir %{_includedir}/gltt
%{_includedir}/gltt/*
%{_libdir}/lib*.so

%files static
%attr(644,root ,root) %{_libdir}/lib*.a
