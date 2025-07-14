Summary:	gltt - library that allows use TrueType fonts in OpenGL application
Summary(pl.UTF-8):	gltt - biblioteka pozwalająca na użycie fontów TrueType w aplikacjach OpenGL
Name:		gltt
Version:	2.4
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://home.worldnet.fr/~rehel/gltt/%{name}-%{version}.tar.gz
# Source0-md5:	2d367294d6efa943f9287fe88089af76
Patch0:		%{name}-cpp.patch
URL:		http://home.worldnet.fr/~rehel/gltt/gltt.html
BuildRequires:	OpenGL-devel
Requires:	OpenGL
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_noautoreqdep	libGL.so.1 libGLU.so.1

%description
Gltt is a library that allows you to read and draw TrueType fonts in
any OpenGL application. It supports bitmapped and anti-aliased font
drawing as well as vectorized and polygonized drawing.

%description -l pl.UTF-8
Gltt jest biblioteką pozwalającą odczytywać i rysować czcionki True
Type w aplikacjach OpenGL. Obsługuje bitmapowe i wygładzane rysowanie
fontów, jak również rysowanie wektoryzowane i wieloboczne.

%package devel
Summary:	Header files for gltt
Summary(pl.UTF-8):	Pliki nagłówkowe gltt
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This package contains the gltt header files required to develop
gltt-based applications.

%description devel -l pl.UTF-8
Pliki nagłówkowe potrzebne do kompilacji programów korzystających z
gltt.

%package static
Summary:	gltt - static library
Summary(pl.UTF-8):	Biblioteka statyczna gltt
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
This package contains the gltt static libraries.

%description static -l pl.UTF-8
Statyczna biblioteka gltt.

%prep
%setup -q
%patch -P0 -p1

%build
%configure2_13

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	libdir=$RPM_BUILD_ROOT%{_libdir} \
	includedir=$RPM_BUILD_ROOT%{_includedir}/gltt

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/gltt

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
