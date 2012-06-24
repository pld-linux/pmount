Summary:	Programs for mounting and unmounting filesystems as normal user
Summary(pl):	Programy do montowania i odmontowywania system�w plik�w jako zwyk�y u�ytkownik
Name:		pmount
Version:	0.9.7
Release:	1
License:	GPL v2
Group:		Applications
Source0:	http://www.piware.de/projects/%{name}-%{version}.tar.gz
# Source0-md5:	29c955ff520cea32ab3e0316306d0ac1
Patch0:		%{name}-build_fixes.patch
URL:		http://www.piware.de/projects.shtml
BuildRequires:	autoconf
BuildRequires:	automake >= 2.52
BuildRequires:	gettext-devel
BuildRequires:	hal-devel >= 0.5.2
BuildRequires:	intltool >= 0.21
BuildRequires:	pkgconfig
BuildRequires:	sysfsutils-devel >= 1.3.0-3
Requires:	hal >= 0.5.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pmount is a wrapper around the standard mount program which permits
normal users to mount/umount removable devices without a matching
/etc/fstab entry.

%description -l pl
pmount jest wrapperem standardowego programu mount, kt�ry pozwala
zwyk�emu u�ytkownikowi na montowanie/odmontowywanie urz�dze�
wymiennych nie posiadaj�cych wpisu w /etc/fstab.

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
