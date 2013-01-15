%define pygtk 2.4.0
%define gnomepython 2.10.0
%define oname gnome-python
%define gdaapi 4.0
%define build_gda 1
%define build_gtkhtml 1
%define build_gksu 0
%define build_gksu2 0
# Deprecated and already obsolete in new xulrunner
%define build_gtkmozembed 0

Summary:	GNOME extra bindings for Python
Name:		gnome-python-extras
Version:	2.25.3
Release:	26
License:	GPLv2+ and LGPLv2+
Group:		Development/GNOME and GTK+
URL:		ftp://ftp.gnome.org/pub/GNOME/sources/gnome-python-extras
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.bz2
Patch2:		gnome-python-extras-automake-1.13.patch
Patch3:		gnome-python-extras-2.25.1-linkage.patch
Patch4:		gnome-python-extras-2.25.3-drop-private-gdl-types.patch

BuildRequires:	pygtk2.0-devel >= %{pygtk}
BuildRequires:	gnome-python >= %{gnomepython}
BuildRequires:	python-devel >= 2.2
BuildRequires:	pkgconfig(libgnomeui-2.0)
#gw, hmm, it still needs gtksourceview-1.0
BuildRequires:	pkgconfig(gtksourceview-1.0)
BuildRequires:	pkgconfig(expat)
BuildRequires:	pkgconfig(avahi-glib)
BuildRequires:	pkgconfig(avahi-client)
BuildRequires:	pkgconfig(pygobject-2.0)
BuildRequires:	gtk-doc
BuildRequires:	docbook-dtd412-xml
# gstreamer suggests codeine, codeine requires gnome-python-gtkmozembed
# which means gnome-python-extras requires itslef to build.
# To fix this problem, we need to conflicts with gtkmozbembed, until
# iurt uses '--no-suggests' by default.
BuildConflicts:	gnome-python-gtkmozembed
Requires:	gnome-python >= %{gnomepython}
Requires:	gnome-python-gnomevfs >= %{gnomepython}

%if %{build_gtkhtml}
BuildRequires:	pkgconfig(libgtkhtml-2.0)
%endif


%description
The gnome-python-extras package contains the additional Python
bindings for GNOME.

%if %{build_gda}
%package -n %{oname}-gda
Summary:	Python bindings for GNU Data Access
Group:		Development/GNOME and GTK+
Requires:	%{name} = %{version}-%{release}
BuildRequires:	pkgconfig(libgda-%{gdaapi})

%description -n %{oname}-gda
This module contains a wrapper that allows programs written in Python
to use GNU Data Access.

%package -n %{oname}-gda-devel
Summary:	C header of the GNU Data Access Python bindings
Group:		Development/C
Requires:	%{oname}-gda = %{version}-%{release}

%description -n %{oname}-gda-devel
This is a C header needed for building extensions to the GNU Data
Access Python bindings.
%endif

%if %{build_gksu}
%package -n %{oname}-gksu
Summary:	Python bindings for GKSu
Group:		Development/GNOME and GTK+
Requires:	%{name} = %{version}-%{release}
BuildRequires:	libgksu1.2-devel
BuildRequires:	libgksuui-devel

%description -n %{oname}-gksu
This module contains a wrapper that allows programs written in Python
to use GKSu.
%endif

%if %{build_gksu2}
%package -n %{oname}-gksu2
Summary:	Python bindings for GKSu2
Group:		Development/GNOME and GTK+
Requires:	%{name} = %{version}-%{release}
BuildRequires:	libgksu2-devel

%description -n %{oname}-gksu2
This module contains a wrapper that allows programs written in Python
to use GKSu.
%endif

%package -n %{oname}-gdl
Summary:	Python bindings for Gnome Devtool Libraries
Group:		Development/GNOME and GTK+
Requires:	%{name} = %{version}-%{release}
BuildRequires:	libgdl-devel

%description -n %{oname}-gdl
This module contains a wrapper that allows programs written in Python
to use Gnome Devtool Libraries.

%package -n %{oname}-gtkspell
Summary:	Python bindings for gtkspell
Group:		Development/GNOME and GTK+
Requires:	%{name} = %{version}-%{release}
BuildRequires:	gtkspell-devel

%description -n %{oname}-gtkspell
This module contains a wrapper that allows gnome python apps to use
the gtkspell library.

%if %{build_gtkmozembed}
%package -n %{oname}-gtkmozembed
Summary:	Python bindings for mozilla
Group:		Development/GNOME and GTK+
Requires:	%{name} = %{version}-%{release}
BuildRequires:	xulrunner-devel

%description -n %{oname}-gtkmozembed
This module contains a wrapper that allows gnome python apps to embed
the mozilla browser.
%endif

%if %{build_gtkhtml}
%package -n %{oname}-gtkhtml2
Summary:	Python bindings for interacting with gtkhtml2
Group:		Development/GNOME and GTK+

%description -n %{oname}-gtkhtml2
This module contains a wrapper that allows the use of gtkhtml2 via
Python
%endif

%prep
%setup -q
%patch2 -p1 -b .automake113~
%patch3 -p1 -b .linkage
%patch4 -p0 -b .gdl
autoreconf -fi

%build
%configure2_5x --with-gtkmozembed=mozilla --enable-docs
%make


%install
%makeinstall_std

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog
%defattr(755,root,root,755)
%dir %{_datadir}/pygtk/2.0/defs
%{_datadir}/pygtk/2.0/defs/*.defs
%{_libdir}/pkgconfig/%{name}-2.0.pc
%{_libdir}/python%{py_ver}/site-packages/gtk-2.0/egg/
%doc examples/egg/

%if %{build_gksu}
%files -n %{oname}-gksu
%defattr(755,root,root,755)
%{_libdir}/python%{py_ver}/site-packages/gtk-2.0/gksu/
%endif

%if %{build_gksu2}
%files -n %{oname}-gksu2
%defattr(755,root,root,755)
%{_libdir}/python%{py_ver}/site-packages/gtk-2.0/gksu2/
%endif

%if %{build_gda}
%files -n %{oname}-gda
%defattr(755,root,root,755)
%{_datadir}/pygtk/2.0/argtypes/gda-*
%{_libdir}/python%{py_ver}/site-packages/gtk-2.0/gda.so

%files -n %{oname}-gda-devel
%defattr(755,root,root,755)
%{_libdir}/pkgconfig/pygda-%{gdaapi}.pc
%{_includedir}/pygda-%{gdaapi}/
%endif

%files -n %{oname}-gdl
%defattr(755,root,root,755)
%{_libdir}/python%{py_ver}/site-packages/gtk-2.0/gdl.so
%doc examples/gdl

%files -n %{oname}-gtkspell
%defattr(755,root,root,755)
%{_libdir}/python%{py_ver}/site-packages/gtk-2.0/gtkspell.so
%doc examples/gtkspell
%doc %{_datadir}/gtk-doc/html/pygtkspell

%if %{build_gtkmozembed}
%files -n %{oname}-gtkmozembed
%defattr(755,root,root,755)
%{_libdir}/python%{py_ver}/site-packages/gtk-2.0/gtkmozembed.so
%doc %{_datadir}/gtk-doc/html/pygtkmozembed
%endif

%if %{build_gtkhtml}
%files -n %{oname}-gtkhtml2
%defattr(755,root,root,755)
%{_libdir}/python%{py_ver}/site-packages/gtk-2.0/gtkhtml2.so
%defattr(644,root,root,755)
%doc examples/gtkhtml2
%endif


%changelog
* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 2.25.3-24mdv2011.0
+ Revision: 664882
- mass rebuild

* Tue Mar 22 2011 Funda Wang <fwang@mandriva.org> 2.25.3-23
+ Revision: 647460
- more gdl fixes

* Mon Mar 21 2011 Funda Wang <fwang@mandriva.org> 2.25.3-22
+ Revision: 647378
- add more BR
- add dtd as br

* Mon Nov 01 2010 Funda Wang <fwang@mandriva.org> 2.25.3-21mdv2011.0
+ Revision: 591319
- rebuild for py 2.7

* Wed Sep 08 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 2.25.3-20mdv2011.0
+ Revision: 576817
- rebuild for new xulrunner 2.0b5

* Sun Aug 08 2010 Funda Wang <fwang@mandriva.org> 2.25.3-19mdv2011.0
+ Revision: 567674
- rebuild for new xulrunner

* Mon Jun 28 2010 Frederic Crozat <fcrozat@mandriva.com> 2.25.3-18mdv2010.1
+ Revision: 549368
- rebuild with latest xulrunner

* Sun Apr 04 2010 Funda Wang <fwang@mandriva.org> 2.25.3-17mdv2010.1
+ Revision: 531037
- rebuild for new xulrunner

* Wed Mar 24 2010 Funda Wang <fwang@mandriva.org> 2.25.3-16mdv2010.1
+ Revision: 526984
- rebuild for new xulrunner

* Fri Jan 22 2010 Funda Wang <fwang@mandriva.org> 2.25.3-15mdv2010.1
+ Revision: 494788
- rebuild for new xulrunner

* Sun Jan 10 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.25.3-14mdv2010.1
+ Revision: 488681
- rebuild for new xulrunner

* Wed Dec 16 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.25.3-13mdv2010.1
+ Revision: 479457
- rebuild for new xulrunner

* Wed Dec 16 2009 Funda Wang <fwang@mandriva.org> 2.25.3-12mdv2010.1
+ Revision: 479147
- rebuild for new xulrunner

* Fri Nov 06 2009 Funda Wang <fwang@mandriva.org> 2.25.3-11mdv2010.1
+ Revision: 460601
- rebuild for new xulrunner

* Mon Sep 21 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.25.3-10mdv2010.0
+ Revision: 447014
- rebuild for new libgdl

* Mon Sep 14 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.25.3-9mdv2010.0
+ Revision: 439609
- rebuild for new xulrunner

* Tue Aug 18 2009 Funda Wang <fwang@mandriva.org> 2.25.3-8mdv2010.0
+ Revision: 417757
- rebuild for xulrunner 1.9.1.2

* Tue Aug 04 2009 Eugeni Dodonov <eugeni@mandriva.com> 2.25.3-7mdv2010.0
+ Revision: 409307
- Rebuild for new xulrunner.

* Fri Jul 24 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.25.3-6mdv2010.0
+ Revision: 399187
- rebuild for new xulrunner

* Sat Jun 13 2009 Funda Wang <fwang@mandriva.org> 2.25.3-5mdv2010.0
+ Revision: 385713
- drop gdl private APIs as suggestsed by gdl 2.27
- buildconflicts with it self
- rebuild for new xulrunner

* Fri May 01 2009 Funda Wang <fwang@mandriva.org> 2.25.3-4mdv2010.0
+ Revision: 369524
- rebuild for new xulrunner

* Sat Mar 28 2009 Gustavo De Nardin <gustavodn@mandriva.com> 2.25.3-3mdv2009.1
+ Revision: 361842
- rebuild for xulrunner 1.9.0.8

* Thu Mar 12 2009 Funda Wang <fwang@mandriva.org> 2.25.3-2mdv2009.1
+ Revision: 354091
- rebuild for new xulrunner

* Sun Feb 15 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.25.3-1mdv2009.1
+ Revision: 340680
- update to new version 2.25.3

* Tue Feb 03 2009 Funda Wang <fwang@mandriva.org> 2.25.2-2mdv2009.1
+ Revision: 337036
- rebuild for new xulrunner

* Fri Jan 30 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.25.2-1mdv2009.1
+ Revision: 335548
- new version
- drop patches 0,1,2
- rediff patch 3
- build pygda 4.0
- enable docs

  + Funda Wang <fwang@mandriva.org>
    - fix url

* Sun Jan 25 2009 Funda Wang <fwang@mandriva.org> 2.19.1-24mdv2009.1
+ Revision: 333368
- fix linkage

* Thu Dec 25 2008 Funda Wang <fwang@mandriva.org> 2.19.1-23mdv2009.1
+ Revision: 318839
- rebuild for new python

* Tue Dec 23 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 2.19.1-22mdv2009.1
+ Revision: 317736
- rebuild for new xulrunner-1.9.0.5

* Fri Nov 14 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.19.1-21mdv2009.1
+ Revision: 303094
- rebuild for new xulrunner

* Mon Sep 29 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.19.1-20mdv2009.0
+ Revision: 289232
- rebuild with new xulrunner

* Fri Sep 26 2008 Tiago Salem <salem@mandriva.com.br> 2.19.1-19mdv2009.0
+ Revision: 288720
- add strict version requires to xulrunner

* Tue Sep 23 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.19.1-18mdv2009.0
+ Revision: 287562
- build with new gdl

* Wed Aug 06 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.19.1-17mdv2009.0
+ Revision: 264281
- rebuild

* Wed Jul 30 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.19.1-13mdv2009.0
+ Revision: 255006
- disable gksu
- fix typo
- build with xulrunner
- update license

* Wed Jul 16 2008 Oden Eriksson <oeriksson@mandriva.com> 2.19.1-12mdv2009.0
+ Revision: 236375
- rebuilt for mozilla-firefox-2.0.0.16

* Thu Jul 03 2008 Tiago Salem <salem@mandriva.com.br> 2.19.1-11mdv2009.0
+ Revision: 231249
- Rebuild for firefox 2.0.0.15

* Wed Mar 26 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.19.1-10mdv2008.1
+ Revision: 190442
- rebuild for firefox 2.0.0.13

* Sat Feb 09 2008 Funda Wang <fwang@mandriva.org> 2.19.1-9mdv2008.1
+ Revision: 164661
- rebuild for new FF

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Dec 12 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.19.1-8mdv2008.1
+ Revision: 117686
- rebuild for new firefox

* Wed Dec 05 2007 Thierry Vignaud <tv@mandriva.org> 2.19.1-7mdv2008.1
+ Revision: 115685
- rebuild so that gnome-python-gtkmozembed got linked with latest firefox library

* Mon Nov 05 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.19.1-6mdv2008.1
+ Revision: 106066
- rebuild for new firefox

* Fri Oct 19 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.19.1-5mdv2008.1
+ Revision: 100431
- rebuild for new firefox

* Tue Jul 31 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.19.1-4mdv2008.0
+ Revision: 57228
- fix buildrequires

* Fri Jun 15 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.19.1-3mdv2008.0
+ Revision: 39892
- rebuild for new ff
- fix buildrequires
- new version
- update file list

  + Anssi Hannula <anssi@mandriva.org>
    - rebuild with correct optflags


* Fri Mar 23 2007 Frederic Crozat <fcrozat@mandriva.com> 2.14.3-4mdv2007.1
+ Revision: 148588
- Build with correct firefox

* Fri Mar 23 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.14.3-3mdv2007.1
+ Revision: 148366
- rebuild for new firefox

* Thu Mar 15 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.14.3-2mdv2007.1
+ Revision: 144443
- create devel package

* Wed Feb 28 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.14.3-1mdv2007.1
+ Revision: 126972
- new version
- build with libgksu1.2 again

* Mon Jan 08 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.14.2-13mdv2007.1
+ Revision: 106105
- rebuild

  + Emmanuel Andry <eandry@mandriva.org>
    - rebuild for new libgksu2

* Fri Jan 05 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.14.2-11mdv2007.1
+ Revision: 104392
- reenable gda module

* Thu Dec 07 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.14.2-10mdv2007.1
+ Revision: 92047
- fix firefox detection

* Tue Nov 28 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.14.2-9mdv2007.1
+ Revision: 88245
- fix buildrequires
- rebuild

* Thu Nov 09 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.14.2-7mdv2007.1
+ Revision: 79221
- Import gnome-python-extras

* Thu Nov 09 2006 Götz Waschk <waschk@mandriva.org> 2.14.2-7mdv2007.1
- unpack patches
- rebuild for new firefox

* Sat Sep 16 2006 Frederic Crozat <fcrozat@mandriva.com> 2.14.2-6mdv2007.0
- Rebuild for new firefox

* Tue Aug 08 2006 Götz Waschk <waschk@mandriva.org> 2.14.2-5mdv2007.0
- fix buildrequires

* Fri Aug 04 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.14.2-1mdv2007.0
- rebuild for new firefox

* Thu Aug 03 2006 Frederic Crozat <fcrozat@mandriva.com> 2.14.2-3mdv2007.0
- Rebuild with latest dbus

* Tue Aug 01 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.14.2-1mdv2007.0
- rebuild for new firefox

* Thu Jul 13 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.14.2-1mdv2007.0
- New release 2.14.2

* Wed Jul 12 2006 Götz Waschk <waschk@mandriva.org> 2.14.1-1mdv2007.0
- update patch 0
- New release 2.14.1

* Sun Jun 18 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.14.0-1mdv2007.0
- rebuild for new libpng

* Wed May 10 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.14.0-3mdk
- rebuild for new firefox

* Tue Apr 25 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.14.0-2mdk
- rebuild for new firefox

* Tue Apr 11 2006 Götz Waschk <waschk@mandriva.org> 2.14.0-1mdk
- new version
- drop the packages that were moved to gnome-python-desktop

* Thu Apr 06 2006 Götz Waschk <waschk@mandriva.org> 2.12.1-7mdk
- fix mozilla-firefox dep

* Sat Mar 11 2006 Götz Waschk <waschk@mandriva.org> 2.12.1-6mdk
- fix deps (bug 21563)

* Thu Feb 16 2006 Götz Waschk <waschk@mandriva.org> 2.12.1-5mdk
- drop gda

* Thu Dec 29 2005 Götz Waschk <waschk@mandriva.org> 2.12.1-4mdk
- add gksu support
- fix buildrequires

* Mon Dec 19 2005 Götz Waschk <waschk@mandriva.org> 2.12.1-3mdk
- fix gtksourceview deps (bug 18777)

* Sun Nov 20 2005 GÃ¶tz Waschk <waschk@mandriva.org> 2.12.1-2mdk
- rebuild for new openssl

* Mon Oct 31 2005 GÃ¶tz Waschk <waschk@mandriva.org> 2.12.1-1mdk
- New release 2.12.1

* Wed Oct 12 2005 Götz Waschk <waschk@mandriva.org> 2.12.0-1mdk
- New release 2.12.0
- add mediaprofiles package
- update file list
- requires new nautilus-burn
- regenerate configure
- rediff the patch
- enable gdl wrapper
- add pygda

* Mon May 30 2005 Götz Waschk <waschk@mandriva.org> 2.10.2-1mdk
- rediff patches
- New release 2.10.2

* Wed May 18 2005 Götz Waschk <waschk@mandriva.org> 2.10.1-2mdk
- add gdl bindings
- patch for gcc4

* Sun Apr 24 2005 Götz Waschk <waschk@mandriva.org> 2.10.1-1mdk
- initial mdk version

* Tue Apr 12 2005 Götz Waschk <waschk@linux-mandrake.com> 2.10.1-0.1gpw
- patch configure, regeneration didn't work
- fix build
- New release 2.10.1

* Tue Mar 08 2005 Götz Waschk <waschk@linux-mandrake.com> 2.10.0-0.1gpw
- bump deps
- fix build for firefox
- New release 2.10.0

* Wed Feb 16 2005 Götz Waschk <waschk@linux-mandrake.com> 2.9.4-0.1gpw
- New release 2.9.4

* Wed Jan 26 2005 Götz Waschk <waschk@linux-mandrake.com> 2.9.3-0.2gpw
- add bindings for gtop, nautilus-burn and totem-plparser
- New release 2.9.3

* Sat Jan 08 2005 Götz Waschk <waschk@linux-mandrake.com> 2.9.2-0.2gpw
- rebuild for new howl

* Mon Jan 03 2005 Götz Waschk <waschk@linux-mandrake.com> 2.9.2-0.1gpw
- add mozembed and gtkspell modules
- New release 2.9.2

* Mon Dec 06 2004 Götz Waschk <waschk@linux-mandrake.com> 2.9.1-0.2gpw
- rebuild for new python

* Tue Nov 30 2004 Götz Waschk <waschk@linux-mandrake.com> 2.9.1-0.1gpw
- update file list

* Tue Nov 30 2004 Goetz Waschk <waschk@linux-mandrake.com> 2.9.1-1mdk
- New release 2.9.1

* Mon Nov 22 2004 Götz Waschk <waschk@linux-mandrake.com> 2.9.0-0.1gpw
- initial package

