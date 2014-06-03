Summary:	An X Window System-based calendar program
Summary(pl.UTF-8):	Kalendarz działający pod X Window System
Name:		ical
Version:	2.2
Release:	25
License:	distributable
Group:		X11/Applications
Source0:	http://www.research.digial.com/SRC/personal/Sanjay_Ghemawat/ical/icalbins/%{name}-%{version}.tar.gz
# Source0-md5:	6bb0d0ce76bb31570c2c99d8da70a58b
Source1:	%{name}.desktop
Patch0:		%{name}-newtcl.patch
Patch1:		%{name}-tcl823.patch
Patch2:		%{name}-hack.patch
Patch3:		%{name}-DESTDIR.patch
Patch4:		%{name}-OPTF.patch
Patch5:		%{name}-protos.patch
Patch6:		%{name}-tcl84.patch
Patch7:		%{name}-prototypes.patch
Patch8:		%{name}-build.patch
URL:		http://www.research.digital.com/SRC/personal/Sanjay_Ghemawat/ical/home.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	perl-base
BuildRequires:	tk-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ical is an X Window System based calendar program. Ical will easily
create/edit/delete entries, create repeating entries, remind you about
upcoming appointments, print and list item occurrences, and allow
shared calendars between different users.

Install ical if you need a calendar program to track your schedule.
You'll need to have the X Window System installed in order to use
ical.

%description -l pl.UTF-8
ical to kalendarz/terminarz pod X Window System. Może łatwo tworzyć,
modyfikować, usuwać wpisy, tworzyć powtarzające się wpisy, przypominać
o zbliżających się spotkaniach, wyświetlać wystąpienia wpisu; pozwala
dzielić kalendarze pomiędzy różnymi użytkownikami.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p0
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1

%{__perl} -pi -e 's@/lib(.*T.*_LIB_FILE)@/%{_lib}$1@' configure.in

%build
cd types
%{__aclocal}
%{__autoconf}
cd ..
%{__aclocal}
%{__autoconf}
%configure \
	--with-tclsh=/usr/bin/tclsh

%{__make} \
	OPTF="%{rpmcflags} %{rpmcppflags} -DUSE_INTERP_RESULT"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir},%{_mandir}/man1,%{_desktopdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	MANDIR=%{_mandir}

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/ical.html doc/ical.doc doc/interface.html doc/interface.doc
%attr(755,root,root) %{_bindir}/ical
%{_mandir}/man1/ical.1*
%{_prefix}/lib/ical
%{_desktopdir}/ical.desktop
