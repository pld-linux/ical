Summary:	An X Window System-based calendar program
Name:		ical 
Version:	2.2
Release:	18
Source0:	http://www.research.digial.com/SRC/personal/Sanjay_Ghemawat/ical/icalbins/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Patch0:		%{name}-newtcl.patch
Patch1:		%{name}-tcl823.patch
Patch2:		%{name}-hack.patch
Patch3:		%{name}-DESTDIR.patch
Patch4:		%{name}-OPTF.patch
URL:		http://www.research.digital.com/SRC/personal/Sanjay_Ghemawat/ical/home.html
Copyright:	distributable
Group:		X11/Applications
Group(pl):	X11/Aplikacje
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

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p0
%patch4 -p1

%build
autoconf
%configure
%{__make} OPTF="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_applnkdir}/Applications
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir},%{_mandir}/man1}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

strip --strip-unneeded $RPM_BUILD_ROOT%{_bindir}/ical

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Applications

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/ical.1 \
	doc/ical.doc doc/interface.doc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/ical.html doc/ical.doc.gz
%doc doc/interface.html doc/interface.doc.gz
%attr(755,root,root) %{_bindir}/ical
%{_mandir}/man1/ical.1.gz
%{_libdir}/ical
%{_applnkdir}/Applications/ical.desktop
