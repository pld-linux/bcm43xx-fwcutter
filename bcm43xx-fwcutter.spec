Summary:	Utility for extracting Broadcom 43xx firmware
Summary(pl.UTF-8):	Narzędzie do wyciągania firmware'u dla układów Broadcom 43xx
Name:		bcm43xx-fwcutter
Version:	20071026
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://linuxwireless.org/download/bcm43xx/fwcutter/%{name}.tar.bz2
# Source0-md5:	a9baae864957c19d4d9947a4ed72188a
URL:		http://linuxwireless.org/en/users/Drivers/b43#devicefirmware
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
fwcutter is a tool which can extract firmware from various source
files. It's written for bcm43xx driver.

%description -l pl.UTF-8
fwcutter to narzędzie potrafiące wyciągać firmware z różnych plików
źródłowych. To narzędzie zostało napisane dla sterownika bcm43xx.

%prep
%setup -q -n %{name}

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -D_BSD_SOURCE"

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install bcm43xx-fwcutter $RPM_BUILD_ROOT%{_bindir}
install bcm43xx-fwcutter.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/bcm43xx-fwcutter
%{_mandir}/man1/bcm43xx-fwcutter.1*
