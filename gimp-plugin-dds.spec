Summary:	DDS (Direct Draw Surface file format) plugin for GIMP
Summary(pl.UTF-8):	Wtyczka DDS (obsługująca format Direct Draw Surface) dla GIMP-a
Name:		gimp-plugin-dds
Version:	1.0.1
Release:	4
License:	GPL
Group:		X11/Applications/Graphics
Source0:	http://nifelheim.dyndns.org/~cocidius/files/gimp-dds-%{version}.tar.bz2
# Source0-md5:	afa9a8823e4fbdc107014250ebd6fd29
URL:		http://nifelheim.dyndns.org/~cocidius/dds/
BuildRequires:	OpenGL-glut-devel
BuildRequires:	gimp-devel >= 1:2.0.0
BuildRequires:	glew-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_plugindir	%(gimptool --gimpplugindir)/plug-ins

%description
Plugin allowing to load and save images in Direct Draw Surface (DDS)
format.

- Load/save DDS files, optionally using DXT texture compression,
- Optional automatic mipmap generation when saving,
- Load mipmaps into separate layers,
- Load cube map faces and volume map slices into separate layers,
- Save cube maps and volume maps with automatic mipmap generation
  support,
- Save image with a custom pixel format,
- Non-power-of-two image loading and saving support with automatic
  mipmap generation support.

%description -l pl.UTF-8
Wtyczka pozwalająca wczytywać i zapisywać obrazy w formacie Direct
Draw Surface (DDS).

- Odczyt/zapis plików DDS, opcjonalna kompresja tekstur DXT,
- Opcjonalna automatyczna generacja mipmap podczas zapisu,
- Ładowanie mipmap do osobnych warstw,
- Ładowanie ścian cube mapy i przekrojów volume mapy do osobnych
  warstw,
- Zapisywanie cube map i volume map z automatyczną generacją mipmap,
- Zapisywanie obrazów z własnym formatem pikseli,
- Ładowanie i zapisywanie obrazów o wymiarach różnych od potęg
  dwójki z automatyczną generacją mipmap.

%prep
%setup -q -n gimp-dds

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} `gimptool --cflags` -DGETTEXT_PACKAGE" \
	GIMPTOOL="gimptool"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_plugindir}

install dds $RPM_BUILD_ROOT%{_plugindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_plugindir}/*
