%define buildgtkhtml 1
%define pygtk 2.4.0
%define gnomepython 2.10.0
%define oname gnome-python
%define build_gda 1

Summary: GNOME extra bindings for Python
Name: gnome-python-extras
Version: 2.14.3
Release: %mkrel 4
Source: ftp://ftp.gnome.org/pub/GNOME/sources/%name/%name-%{version}.tar.bz2
Patch: gnome-python-extras-2.14.1-firefox.patch
Patch1: gnome-python-extras-2.12.1-gksu.patch
URL: ftp://ftp.gnome.org/pub/GNOME/sources/gnome-python/
License: LGPL
Group: Development/GNOME and GTK+
BuildRoot: %{_tmppath}/%name-root
BuildRequires: pygtk2.0-devel >= %pygtk
BuildRequires: gnome-python >= %gnomepython
BuildRequires: python-devel >= 2.2
BuildRequires: libgnomeui2-devel >= 2.0.0
BuildRequires: gtksourceview-devel >= 1.1.0
BuildRequires: libexpat-devel
BuildRequires: avahi-glib-devel avahi-client-devel
Requires: gnome-python >= %gnomepython
Requires: gnome-python-gnomevfs >= %gnomepython

%if %{buildgtkhtml}
BuildRequires: libgtkhtml2-devel >= 1.99.9
%endif


%description
The gnome-python-extras package contains the additional Python
bindings for GNOME.


%if %build_gda
%package -n %oname-gda
Summary: Python bindings for GNU Data Access
Group: Development/GNOME and GTK+
Requires: %name = %version
BuildRequires: gda1.2-devel

%description -n %oname-gda
This module contains a wrapper that allows programs written in Python
to use GNU Data Access.

%package -n %oname-gda-devel
Summary: C header of the GNU Data Access Python bindings
Group: Development/C
Requires: %oname-gda = %version

%description -n %oname-gda-devel
This is a C header needed for building extensions to the GNU Data
Access Python bindings.
%endif

%package -n %oname-gksu
Summary: Python bindings for GKSu
Group: Development/GNOME and GTK+
Requires: %name = %version
BuildRequires: libgksu1.2-devel
BuildRequires: libgksuui-devel

%description -n %oname-gksu
This module contains a wrapper that allows programs written in Python
to use GKSu.

%package -n %oname-gdl
Summary: Python bindings for Gnome Devtool Libraries
Group: Development/GNOME and GTK+
Requires: %name = %version
BuildRequires: libgdl-devel

%description -n %oname-gdl
This module contains a wrapper that allows programs written in Python
to use Gnome Devtool Libraries.

%package -n %oname-gtkspell
Summary: Python bindings for gtkspell
Group: Development/GNOME and GTK+
Requires: %name = %version
BuildRequires: gtkspell-devel

%description -n %oname-gtkspell
This module contains a wrapper that allows gnome python apps to use
the gtkspell library.

%package -n %oname-gtkmozembed
Summary: Python bindings for mozilla
Group: Development/GNOME and GTK+
Requires: %name = %version
BuildRequires: mozilla-firefox-devel
%define firefox_version %(rpm -q mozilla-firefox --queryformat %{VERSION})
Requires: %mklibname mozilla-firefox %{firefox_version}

%description -n %oname-gtkmozembed
This module contains a wrapper that allows gnome python apps to embed
the mozilla browser.

%package -n %oname-gtkhtml2
Summary: Python bindings for interacting with gtkhtml2
Group: Development/GNOME and GTK+

%description -n %oname-gtkhtml2
This module contains a wrapper that allows the use of gtkhtml2 via
Python


%prep
%setup -q
%patch1 -p1 -b .gtksu
%if %mdkversion <= 200700
%patch -p1 -b .firefox
autoconf
%endif

%build
./configure --prefix=%_prefix --libdir=%_libdir

%make GNOME_PYTHON_DEFSDIR=`pkg-config --variable=defsdir gnome-python-2.0`

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall
find $RPM_BUILD_ROOT -name '*.la' -exec rm {} \;

%clean
rm -rf %buildroot

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog
%defattr(755,root,root,755)
%dir %{_datadir}/pygtk/2.0/defs
%{_datadir}/pygtk/2.0/defs/*.defs
%_libdir/pkgconfig/%name-2.0.pc
%_libdir/python%pyver/site-packages/gtk-2.0/egg/
%doc examples/egg/

%files -n %oname-gksu
%defattr(755,root,root,755)
%_libdir/python%pyver/site-packages/gtk-2.0/gksu/


%if %build_gda
%files -n %oname-gda
%defattr(755,root,root,755)
%{_libdir}/python%pyver/site-packages/gtk-2.0/gda.so

%files -n %oname-gda-devel
%defattr(755,root,root,755)
%_libdir/pkgconfig/pygda-1.2.pc
%_includedir/pygda-1.2/
%endif

%files -n %oname-gdl
%defattr(755,root,root,755)
%{_libdir}/python%pyver/site-packages/gtk-2.0/gdl.so
%doc examples/gdl

%files -n %oname-gtkspell
%defattr(755,root,root,755)
%{_libdir}/python%pyver/site-packages/gtk-2.0/gtkspell.so
%doc examples/gtkspell
%doc %_datadir/gtk-doc/html/pygtkspell

%files -n %oname-gtkmozembed
%defattr(755,root,root,755)
%{_libdir}/python%pyver/site-packages/gtk-2.0/gtkmozembed.so
%doc %_datadir/gtk-doc/html/pygtkmozembed

%if %{buildgtkhtml}
%files -n %oname-gtkhtml2
%defattr(755,root,root,755)
%{_libdir}/python%pyver/site-packages/gtk-2.0/gtkhtml2.so
%defattr(644,root,root,755)
%doc examples/gtkhtml2
%endif


