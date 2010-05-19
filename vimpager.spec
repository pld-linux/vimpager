Summary:	Use ViM as PAGER
Summary(hu.UTF-8):	ViM PAGER-ként
Name:		vimpager
Version:	1.3
Release:	0.1
License:	GPL
Group:		Applications/Text
Source0:	http://www.vim.org/scripts/download_script.php?src_id=13024
# Source0-md5:	2ace56c96fb47cd6f34e47b2d6707729
URL:		http://www.vim.org/scripts/script.php?script_id=1723
Requires:	procps
Requires:	vim
Source1:	README
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A slightly more sophisticated replacement for less.sh that also
supports being set as the PAGER environment variable. Displays man
pages, perldocs and python documentation properly.

%description -l hu.UTF-8
Egy csere a less.sh-ra. Manual oldalakat, perldocs-t és python
dokumentácikókat helyesen megjelenít.

%prep

%build

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_bindir}
install %{SOURCE0} $RPM_BUILD_ROOT%{_bindir}/%{name}

install -d $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
install %{SOURCE1} $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_docdir}/%{name}-%{version}
%attr(755,root,root) %{_bindir}/%{name}
