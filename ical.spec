Summary: An X Window System-based calendar program.
Name: ical 
Version: 2.2
Release: 9
Source: http://www.research.digial.com/SRC/personal/Sanjay_Ghemawat/ical/icalbins/ical-%{PACKAGE_VERSION}.tar.gz
Source1: ical.wmconfig
Patch0: ical-2.2-newtcl.patch
Url: http://www.research.digital.com/SRC/personal/Sanjay_Ghemawat/ical/home.html
Copyright: distributable
Group: Applications/Productivity
BuildRoot: /var/tmp/ical-root

%description
Ical is an X Window System based calendar program.  Ical will easily
create/edit/delete entries, create repeating entries, remind you about
upcoming appointments, print and list item occurrences, and allow
shared calendars between different users.

Install ical if you need a calendar program to track your schedule.  You'll
need to have the X Window System installed in order to use ical.

%prep
%setup -q
%patch0 -p1

%build
autoconf
CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=/usr
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/etc/X11/wmconfig
mkdir -p $RPM_BUILD_ROOT/usr/{bin,lib,man/man1}
make prefix=$RPM_BUILD_ROOT/usr install
strip $RPM_BUILD_ROOT/usr/bin/ical-%{PACKAGE_VERSION}
install -m 644 $RPM_SOURCE_DIR/ical.wmconfig $RPM_BUILD_ROOT/etc/X11/wmconfig/ical

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc doc/ical.html doc/ical.doc 
%doc doc/interface.html doc/interface.doc
/usr/bin/ical-%{PACKAGE_VERSION}
/usr/bin/ical
/usr/man/man1/ical.1
/usr/lib/ical
/etc/X11/wmconfig/ical
