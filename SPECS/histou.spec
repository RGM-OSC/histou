Summary: Histou 
Name: histou
Version: 0.4.3
Release: 2.rgm
Source: %{name}-%{version}.tar.gz
Group: Applications/System
License: GPL
Requires: influxdb, grafana
BuildRequires: rpm-macros-rgm

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Source1: histou.conf

# appliance group and users
# /srv/rgm/rgmweb-1.0
%define	rgmdatadir	%{rgm_path}/%{name}-%{version}
%define rgmlinkdir  %{rgm_path}/%{name}

%description
Adds templates to Grafana in combination with nagflux

%prep
%setup -q

%build

%install
install -d -m0755 %{buildroot}%{rgmdatadir}
install -d -m0755 %{buildroot}%{_sysconfdir}/httpd/conf.d/
install -d -m0755 /usr/share/grafana/public/dashboards/

cp -afv ./* %{buildroot}%{rgmdatadir}
cp %{SOURCE1} %{buildroot}%{_sysconfdir}/httpd/conf.d/
cp histou.js /usr/share/grafana/public/dashboards/


%post
ln -nsf %{rgmdatadir} %{rgmlinkdir}

%clean
rm -rf %{buildroot}

%files
%{rgmdatadir}
%{_sysconfdir}/httpd/conf.d/

%changelog
* Tue Mar 27 2019 Michael Aubertin <maubertin@fr.scc.com> - 0.4.3-2.rgm
- Fix URL issue
* Tue Mar 12 2019 Michael Aubertin <maubertin@fr.scc.com> - 0.4.3-1.rgm
- Initial release

