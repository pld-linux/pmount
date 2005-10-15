Summary:	Programs for mounting and unmounting filesystems as normal user
Summary(pl):	Programy do montowania i odmontowywania systemów plików jako zwyk³y u¿ytkownik
Name:		pmount
Version:	0.9.4
Release:	1
License:	GPL v2
Group:		Applications
Source0:	http://www.piware.de/projects/%{name}-%{version}.tar.gz
# Source0-md5:	249d016d7e863e8cec4a45267c4f4af9
Patch0:		%{name}-build_fixes.patch
URL:		http://www.piware.de/projects.shtml
BuildRequires:	gettext-devel
BuildRequires:	hal-devel >= 0.5.3
BuildRequires:	pkgconfig
BuildRequires:	sysfsutils-devel
Requires:	hal >= 0.5.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pmount is a wrapper around the standard mount program which permits
normal users to mount/umount removable devices without a matching
/etc/fstab entry.

%description -l pl
pmount jest wrapperem standardowego programu mount, który pozwala
zwyk³emu u¿ytkownikowi na montowanie/odmontowywanie urz±dzeñ
wymiennych nie posiadaj±cych wpisu w /etc/fstab.

%prep
%setup -q
%patch0 -p1

%build
%{__make} \
	OPTFLAGS="%{rpmcflags}" \
	CC="%{__cc}" \
	bindir=%{_bindir} \
	datadir=%{_datadir} \
	sysconfdir=%{_sysconfdir}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	bindir=%{_bindir} \
	datadir=%{_datadir} \
	sysconfdir=%{_sysconfdir}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS CHANGES TODO
%config(noreplace) %verify(not md5 mtime size) /etc/pmount.allow
%attr(4755,root,root) %{_bindir}/pmount
%attr(4755,root,root) %{_bindir}/pumount
%attr(755,root,root) %{_bindir}/pmount-hal
%{_mandir}/man1/*
