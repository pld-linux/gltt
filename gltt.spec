Summary:   Gltt - library that allows use TrueType fonts in OpenGL application
Name:      gltt
Version:   2.3
Release:   1
Copyright: LGPL
Group:     Development/Version Control
Source:    http://home.worldnet.fr/~rehel/gltt/%{name}-%{version}.tar.gz
URL:       http://home.worldnet.fr/~rehel/gltt/gltt.html
Requires:  Mesa >= 2.6
BuildRoot: /tmp/%{name}-%{version}-root

%description
Gltt is a library that allows you to read and draw TrueType fonts in          
any OpenGL application.                                                       
It supports bitmapped and anti-aliased font drawing as well as                
vectorized and polygonized drawing.                                           

%package devel
Summary:   Header files for gltt
Group:     Development/Libraries
Requires:  %{name} = %{version}

%description devel
This package contains the gltt header files required to develop gltt-based
applications.

%package static
Summary:   gltt - static library and header files
Group:     Development/Libraries
Requires:  %{name}-devel = %{version}

%description static
This package contains the gltt static libraries.

%prep
%setup -q

%build
CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=/usr
make

%install
rm -rf $RPM_BUILD_ROOT
make prefix=$RPM_BUILD_ROOT/usr install

strip $RPM_BUILD_ROOT/usr/lib/lib*.so.*.*

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%attr(755, root ,root) /usr/lib/lib*.so.*.*

%files devel
%defattr(644, root ,root, 755)
%dir /usr/include/gltt
/usr/include/gltt/*
/usr/lib/lib*.so

%files static
/usr/lib/lib*.a

%changelog
* Sun Sep  6 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [2.3-1]
- added static subpackage,
- changed permission on shared libraries to 755.

* Sun Jun 14 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [2.2-1]
- fixed typo in %defattr macro.

* Wed May  5 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [2.0-1]
- first release in rpm package,
- spec file contains construction wihch understand rpm >= 2.4.99.
