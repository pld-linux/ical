Summary:	An X Window System-based calendar program
Summary(pl):	Kalendarz dzia³aj±cy pod X Window System
Name:		ical 
Version:	2.2
Release:	20
License:	distributable
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(es):	X11/Aplicaciones
Group(pl):	X11/Aplikacje
Group(pt_BR):	X11/Aplicações
Group(pt):	X11/Aplicações
Source0:	http://www.research.digial.com/SRC/personal/Sanjay_Ghemawat/ical/icalbins/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Patch0:		%{name}-newtcl.patch
Patch1:		%{name}-tcl823.patch
Patch2:		%{name}-hack.patch
Patch3:		%{name}-DESTDIR.patch
Patch4:		%{name}-OPTF.patch
URL:		http://www.research.digital.com/SRC/personal/Sanjay_Ghemawat/ical/home.html
BuildRequires:	automake
BuildRequires:	autoconf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Ical is an X Window System based calendar program. Ical will easily
create/edit/delete entries, create repeating entries, remind you about
upcoming appointments, print and list item occurrences, and allow
shared calendars between different users.

Install ical if you need a calendar program to track your schedule.
You'll need to have the X Window System installed in order to use
ical.

%description -l pl
ical to kalendarz/terminarz pod X Window System. Mo¿e ³atwo tworzyæ,
modyfikowaæ, usuwaæ wpisy, tworzyæ powtarzaj±ce siê wpisy, przypominaæ
o zbli¿aj±cych siê spotkaniach, wy¶wietlaæ wyst±pienia wpisu; pozwala
dzieliæ kalendarze pomiêdzy ró¿nymi u¿ytkownikami.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p0
%patch4 -p1

%build
cd types
	aclocal
	autoconf
cd ..
aclocal
autoconf
%configure \
	--with-tclsh=/usr/bin/tclsh

%{__make} OPTF="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_applnkdir}/Applications
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir},%{_mandir}/man1}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Applications

gzip -9nf doc/ical.doc doc/interface.doc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/ical.html doc/ical.doc.gz
%doc doc/interface.html doc/interface.doc.gz
%attr(755,root,root) %{_bindir}/ical
%{_mandir}/man1/ical.1*
%{_libdir}/ical
%{_applnkdir}/Applications/ical.desktop
