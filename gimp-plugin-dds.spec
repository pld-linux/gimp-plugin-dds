Summary:	DDS plugin
Summary(pl):	Wtyczka DDS
Name:		gimp-plugin-dds
Version:	1.0.1
Release:	1
License:	GPL
Group:		X11/Applications/Graphics
Source0:	http://nifelheim.dyndns.org/~cocidius/files/gimp-dds-%{version}.tar.bz2
# Source0-md5:	afa9a8823e4fbdc107014250ebd6fd29
URL:		http://nifelheim.dyndns.org/~cocidius/dds/
BuildRequires:	gimp-devel >= 1:2.0.0
BuildRequires:	glew
BuildRequires:	glut
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

%description -l pl
Wtyczka pozwalaj�ca wczytywa� i zapisywa� obrazy w formacie Direct
Draw Surface (DDS).

- Odczyt/zapis plik�w DDS, opcjonalna kompresja tekstur DXT,
- Opcjonalna automatyczna generacja mipmap podczas zapisu,
- �adowanie mipmap do osobnych warstw,
- �adowanie �cian cube mapy i przekroj�w volume mapy do osobnych
  warstw,
- Zapisywanie cube map i volume map z automatyczn� generacj� mipmap,
- Zapisywanie obraz�w z w�asnym formatem pikseli,
- �adowanie i zapisywanie obraz�w o wymiarach r�nych od pot�g
  dw�jki z automatyczn� generacj� mipmap.

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

install dds		$RPM_BUILD_ROOT%{_plugindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_plugindir}/*
