Summary:	DDS plugin
Summary(pl):	Wtyczka DDS
Name:		gimp-plugin-dds
Version:	0.3
Release:	1
License:	GPL
Group:		X11/Applications/Graphics
Source0:	http://nifelheim.dyndns.org/~cocidius/files/gimp-dds-%{version}.tar.bz2
# Source0-md5:	be9dc555b94a91ccea0b91ca26edd641
URL:		http://nifelheim.dyndns.org/~cocidius/dds/
BuildRequires:	gimp-devel >= 1:2.0.0
BuildRequires:	glut
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_plugindir	%(gimptool --gimpplugindir)/plug-ins

%description
Plugin allowing to load and save images in Direct Draw Surface (DDS)
format.

- Load/save DDS files, optionally using DXT texture compression,
- Optional automatic mipmap generation when saving,
- Load mipmaps into separate layers,
- Load cube map faces and volume map slices into separate layers.

%description -l pl
Wtyczka pozwalaj±ca wczytywaæ i zapisywaæ obrazy w formacie Direct
Draw Surface (DDS).

- Odczyt/zapis plików DDS, opcjonalna kompresja tekstur DXT,
- Opcjonalna automatyczna generacja mipmap podczas zapisu,
- £adowanie mipmap do osobnych warstw,
- £adowanie ¶cian cube mapy i przekrojów volume mapy do osobnych
  warstw.

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
