Summary:	gltt - library that allows use TrueType fonts in OpenGL application
Summary(pl):	gltt - biblioteka pozwalaj±ca na uøycie fontÛw TrueType w aplikacjach OpenGL
Name:		gltt
Version:	2.4
Release:	1
License:	LGPL
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Group(pt_BR):	Bibliotecas
Group(ru):	‚…¬Ã…œ‘≈À…
Group(uk):	‚¶¬Ã¶œ‘≈À…
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
Gltt jest bibliotek± pozwalajac± odczytywaÊ i rysowaÊ czcionki True
Type w aplikacjach OpenGL. Obs≥uguje bitmapowe i wyg≥adzane rysowanie
fontÛw, jak rÛwnieø rysowanie wektoryzowane i wieloboczne.

%package devel
Summary:	Header files for gltt
Summary(pl):	Pliki nag≥Ûwkowe gltt
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
This package contains the gltt header files required to develop
gltt-based applications.

%description devel -l pl
Pliki nag≥Ûwkowe potrzebne do kompilacji programÛw korzystaj±cych z
gltt.

%package static
Summary:	gltt - static library
Summary(pl):	Biblioteka statyczna gltt
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
This package contains the gltt static libraries.

%description static -l pl
Statyczna biblioteka gltt.

%prep
%setup -q

%build
CFLAGS="%{rpmcflags}" CXXFLAGS="%{rpmcflags}" \
./configure %{_target_platform} \
	--prefix=%{_prefix}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} prefix=$RPM_BUILD_ROOT%{_prefix} install

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
