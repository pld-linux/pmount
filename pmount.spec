Summary:	Programs for mounting and unmounting filesystems as normal user
Summary(pl.UTF-8):	Programy do montowania i odmontowywania systemów plików jako zwykły użytkownik
Name:		pmount
Version:	0.9.13
Release:	1
License:	GPL v2
Group:		Applications
Source0:	http://www.piware.de/projects/%{name}-%{version}.tar.gz
# Source0-md5:	978d1c996fb7f74e8bb953d5674ab691
Patch0:		%{name}-build_fixes.patch
URL:		http://www.piware.de/projects.shtml
BuildRequires:	autoconf
BuildRequires:	automake >= 2.52
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel
BuildRequires:	hal-devel >= 0.5.2
BuildRequires:	intltool >= 0.21
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	sysfsutils-devel >= 1.3.0-3
Requires:	hal >= 0.5.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pmount is a wrapper around the standard mount program which permits
normal users to mount/umount removable devices without a matching
/etc/fstab entry.

%description -l pl.UTF-8
pmount jest wrapperem standardowego programu mount, który pozwala
zwykłemu użytkownikowi na montowanie/odmontowywanie urządzeń
wymiennych nie posiadających wpisu w /etc/fstab.

%prep
%setup -q
%patch0 -p1

%build
%{__intltoolize}
%{__aclocal}
%{__automake}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog TODO
%config(noreplace) %verify(not md5 mtime size) /etc/pmount.allow
%attr(4755,root,root) %{_bindir}/pmount
%attr(4755,root,root) %{_bindir}/pumount
%attr(755,root,root) %{_bindir}/pmount-hal
%{_mandir}/man1/*
