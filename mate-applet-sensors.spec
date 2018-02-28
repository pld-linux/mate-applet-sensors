#
# Conditional build:
%bcond_without	nvidia	# NVidia sensors
%bcond_with	ati	# ATI sensors (requires fglrx driver)

%ifnarch %{ix86} %{x8664}
%undefine	with_ati
%undefine	with_nvidia
%endif
Summary:	MATE Sensors Applet
Summary(pl.UTF-8):	MATE Sensors Applet - aplet z czujnikami dla środowiska MATE
Name:		mate-applet-sensors
Version:	1.20.1
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://pub.mate-desktop.org/releases/1.20/mate-sensors-applet-%{version}.tar.xz
# Source0-md5:	d62a8a007cc4ee1d318be6e95c298081
URL:		https://github.com/mate-desktop/mate-sensors-applet
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake >= 1:1.9
BuildRequires:	cairo-devel >= 1.0.4
BuildRequires:	dbus-glib-devel >= 0.80
BuildRequires:	gettext-tools >= 0.10.40
BuildRequires:	glib2-devel >= 1:2.50.0
BuildRequires:	gtk+3-devel >= 3.22
BuildRequires:	intltool >= 0.50.1
%{?with_nvidia:BuildRequires:	libXNVCtrl-devel >= 256.25}
BuildRequires:	libatasmart-devel >= 0.16
BuildRequires:	libnotify-devel >= 0.7.0
BuildRequires:	libtool >= 1:1.4.3
BuildRequires:	libxslt-progs
BuildRequires:	lm_sensors-devel
BuildRequires:	mate-common
BuildRequires:	mate-panel-devel >= 1.17.0
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	rpmbuild(find_lang) >= 1.36
BuildRequires:	rpmbuild(macros) >= 1.592
BuildRequires:	tar >= 1:1.22
%{?with_nvidia:BuildRequires:	xorg-lib-libX11-devel}
%{?with_nvidia:BuildRequires:	xorg-lib-libXext-devel}
BuildRequires:	xz
BuildRequires:	yelp-tools
Requires(post,postun):	gtk-update-icon-cache
Requires:	%{name}-libs = %{version}-%{release}
Requires:	cairo >= 1.0.4
Requires:	gtk+3 >= 3.22
Requires:	hicolor-icon-theme
Requires:	libnotify >= 0.7.0
Requires:	mate-panel >= 1.17.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# plugin_name symbol comes from plugins
%define		skip_post_check_so	libmate-sensors-applet-plugin.so.*

%define		_libexecdir	%{_libdir}/mate-panel

%description
MATE Sensors Applet is an applet for the MATE Panel to display
readings from hardware sensors, including CPU temperature, fan speeds
and voltage readings under Linux.

%description -l pl.UTF-8
MATE Sensors Applet to aplet panelu MATE wyświetlający odczyty z
czujników sprzętowych, w tym temperaturę procesora, prędkość
wiatraczków oraz odczyty napięcia pod Linuksem.

%package plugin-aticonfig
Summary:	MATE Sensors Applet plugin to show ATI GPUs temperature
Summary(pl.UTF-8):	Wtyczka apletu MATE Sensors do pokazywania temperatury GPU ATI
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	/usr/bin/aticonfig

%description plugin-aticonfig
MATE Sensors Applet plugin to show ATI GPUs temperature.

%description plugin-aticonfig -l pl.UTF-8
Wtyczka apletu MATE Sensors do pokazywania temperatury GPU ATI.

%package plugin-hddtemp
Summary:	MATE Sensors Applet plugin to show disk temperatures via hddtemp
Summary(pl.UTF-8):	Wtyczka apletu MATE Sensors do pokazywania temperatury dysków poprzez hddtemp
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	hddtemp-hddtempd

%description plugin-hddtemp
MATE Sensors Applet plugin to show disk temperatures from ATA
S.M.A.R.T. read via hddtemp server.

%description plugin-hddtemp -l pl.UTF-8
Wtyczka apletu MATE Sensors do pokazywania temperatury dysków
odczytanych z ATA S.M.A.R.T. poprzez serwer hddtemp.

%package plugin-libsensors
Summary:	MATE Sensors Applet plugin to show values read by lm_sensors
Summary(pl.UTF-8):	Aplet MATE Sensors do pokazywania wartości odczytanych przez lm_sensors
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description plugin-libsensors
MATE Sensors Applet plugin to show values read by lm_sensors:
temperatures, fan speeds and voltages.

%description plugin-libsensors -l pl.UTF-8
Aplet MATE Sensors do pokazywania wartości odczytanych przez
lm_sensors: temperatur, prędkości wiatraczków, napięć.

%package plugin-nvidia
Summary:	MATE Sensors Applet plugin to show NVidia GPUs temperature
Summary(pl.UTF-8):	Wtyczka apletu MATE Sensors do pokazywania temperatury GPU NVidia
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description plugin-nvidia
MATE Sensors Applet plugin to show NVidia GPUs temperature.

%description plugin-nvidia -l pl.UTF-8
Wtyczka apletu MATE Sensors do pokazywania temperatury GPU NVidia.

%package plugin-udisks
Summary:	MATE Sensors Applet plugin to show disk temperatures via UDisks
Summary(pl.UTF-8):	Wtyczka apletu MATE Sensors do pokazywania temperatury dysków poprzez UDisks
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	dbus-glib >= 0.80
Requires:	libatasmart >= 0.16
Requires:	udisks2

%description plugin-udisks
MATE Sensors Applet plugin to show disk temperatures from ATA
S.M.A.R.T. read via UDisks.

%description plugin-udisks -l pl.UTF-8
Wtyczka apletu MATE Sensors do pokazywania temperatury dysków
odczytanych z ATA S.M.A.R.T. poprzez UDisks.

%package libs
Summary:	MATE Sensors Applet library
Summary(pl.UTF-8):	Biblioteka MATE Sensors Applet
Group:		Libraries
Requires:	glib2 >= 1:2.50.0

%description libs
MATE Sensors Applet library.

%description libs -l pl.UTF-8
Biblioteka MATE Sensors Applet.

%package devel
Summary:	Header files for MATE Sensors Applet plugins development
Summary(pl.UTF-8):	Pliki nagłówkowe do tworzenia wtyczek apletu MATE Sensors
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	glib2-devel >= 1:2.50.0

%description devel
Header files for MATE Sensors Applet plugins development.

%description devel -l pl.UTF-8
Pliki nagłówkowe do tworzenia wtyczek apletu MATE Sensors.

%prep
%setup -q -n mate-sensors-applet-%{version}

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
	--disable-static \
	%{?with_ati:--with-aticonfig=/usr/bin/aticonfig} \
	%{!?with_nvidia:--without-nvidia}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/lib*.la
%{__rm} $RPM_BUILD_ROOT%{_libdir}/mate-sensors-applet/plugins/*.la
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/{frp,ku_IQ,jv,pms}

%find_lang mate-sensors-applet --with-mate

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas
%update_icon_cache hicolor

%postun
%glib_compile_schemas
%update_icon_cache hicolor

%files -f mate-sensors-applet.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libexecdir}/mate-sensors-applet
%dir %{_libdir}/mate-sensors-applet
%dir %{_libdir}/mate-sensors-applet/plugins
%attr(755,root,root) %{_libdir}/mate-sensors-applet/plugins/libacpi.so
%attr(755,root,root) %{_libdir}/mate-sensors-applet/plugins/libi8k.so
%attr(755,root,root) %{_libdir}/mate-sensors-applet/plugins/libibm-acpi.so
%attr(755,root,root) %{_libdir}/mate-sensors-applet/plugins/libmbmon.so
%attr(755,root,root) %{_libdir}/mate-sensors-applet/plugins/libomnibook.so
%attr(755,root,root) %{_libdir}/mate-sensors-applet/plugins/libpmu-sys.so
%attr(755,root,root) %{_libdir}/mate-sensors-applet/plugins/libsmu-sys.so
%attr(755,root,root) %{_libdir}/mate-sensors-applet/plugins/libsonypi.so
%{_datadir}/dbus-1/services/org.mate.panel.applet.SensorsAppletFactory.service
%{_datadir}/glib-2.0/schemas/org.mate.sensors-applet.gschema.xml
%{_datadir}/glib-2.0/schemas/org.mate.sensors-applet.sensor.gschema.xml
%{_datadir}/mate-panel/applets/org.mate.applets.SensorsApplet.mate-panel-applet
%{_datadir}/mate-sensors-applet
%{_iconsdir}/hicolor/48x48/apps/mate-sensors-applet.png
%{_iconsdir}/hicolor/*x*/devices/mate-sensors-applet-*.png
%{_pixmapsdir}/mate-sensors-applet

%if %{with ati}
%files plugin-aticonfig
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/mate-sensors-applet/plugins/libaticonfig.so
%endif

%files plugin-hddtemp
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/mate-sensors-applet/plugins/libhddtemp.so

%files plugin-libsensors
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/mate-sensors-applet/plugins/liblibsensors.so

%if %{with nvidia}
%files plugin-nvidia
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/mate-sensors-applet/plugins/libnvidia.so
%endif

%files plugin-udisks
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/mate-sensors-applet/plugins/libudisks2.so

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmate-sensors-applet-plugin.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libmate-sensors-applet-plugin.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmate-sensors-applet-plugin.so
%{_includedir}/mate-sensors-applet
