Summary:	Gltt - library that allows use TrueType fonts in OpenGL application
Name:		gltt
Version:	2.4
Release:	1
License:	LGPL
Group:		Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
Source0:	http://home.worldnet.fr/~rehel/gltt/%{name}-%{version}.tar.gz
URL:		http://home.worldnet.fr/~rehel/gltt/gltt.html
BuildRequires:	OpenGL-devel
Requires:	OpenGL
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_noautoreqdep	libGL.so.1 libGLU.so.1

%description
Gltt is a library that allows you to read and draw TrueType fonts in
any OpenGL application. It supports bitmapped and anti-aliased font
drawing as well as vectorized and polygonized drawing.

%description -l pl
Gltt jest bibliotek± pozwalajac± odczytywaæ i rysowaæ czcionki True
Type w aplikacjach OpenGL. Obs³uguje bitmapowe i wyg³adzane rysowanie
fontów, jak równie¿ rysowanie wektoryzowane i wieloboczne.

%package devel
Summary:	Header files for gltt
Group:		Development/Libraries
Group(fr):	Development/Librairies
Requires:	%{name} = %{version}

%description devel
This package contains the gltt header files required to develop
gltt-based applications.

%package static
Summary:	gltt - static library and header files
Group:		Development/Libraries
Group(fr):	Development/Librairies
Requires:	%{name}-devel = %{version}

%description static
This package contains the gltt static libraries.

%prep
%setup -q

%build
CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS" \
./configure %{_target_platform} \
	--prefix=%{_prefix}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} prefix=$RPM_BUILD_ROOT%{_prefix} install

strip $RPM_BUILD_ROOT%{_libdir}/lib*.so.*.*

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/gltt

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
