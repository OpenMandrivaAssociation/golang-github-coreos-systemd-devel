%global goipath github.com/coreos/go-systemd

Name:		golang-github-coreos-systemd-devel
Version:	22.5.0
Release:	1
Summary:	Go bindings to systemd
Group:		Development/Go
License:	Apache-2.0
URL:		https://github.com/coreos/go-systemd
Source0:	https://github.com/coreos/go-systemd/archive/refs/tags/v%{version}.tar.gz
BuildRequires:	compiler(golang)
Requires:	golang
BuildArch:	noarch

%description
Go bindings to systemd

%prep
%autosetup -p1 -n go-systemd-%{version}

%build

%install
%goinstall

%files
%{_datadir}/gocode/src/%{goipath}
