Summary: Histou
Name: histou
Version: 0.4.3
Release: 6.rgm
Source: %{name}.tar.gz
Group: Applications/System
License: GPL
Requires: influxdb, grafana
BuildRequires: rpm-macros-rgm

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


# appliance group and users
# /srv/rgm/rgmweb-1.0
%define	rgmdatadir	%{rgm_path}/%{name}-%{version}
%define rgmlinkdir  %{rgm_path}/%{name}

%description
Adds templates to Grafana in combination with nagflux

%prep
%setup -q -n %{name}

%build

%install
install -d -m0755 %{buildroot}%{rgmdatadir}
install -d -m0755 /usr/share/grafana/public/dashboards/

cp -afv ./* %{buildroot}%{rgmdatadir}
cp histou.js /usr/share/grafana/public/dashboards/


%post
ln -nsf %{rgmdatadir} %{rgmlinkdir}

%clean
rm -rf %{buildroot}

%files
%{rgmdatadir}

%changelog
* Thu Dec 28 2023 Vincent Fricou <vfricou@fr.scc.com> - 0.4.3-6.rgm
- Fix autoloader for php 8 compatibility

* Wed Jun 14 2023 Eric Belhomme <ebelhomme@fr.scc.com> - 0.4.3-5.rgm
- Fix binary absolute path

* Wed Mar 17 2021 Eric Belhomme <ebelhomme@fr.scc.com> - 0.4.3-4.rgm
- remove Apache config

* Tue Jun 3 2020 Michael Aubertin <maubertin@fr.scc.com> - 0.4.3-3.rgm
- Fix Apache config

* Tue Mar 27 2019 Michael Aubertin <maubertin@fr.scc.com> - 0.4.3-2.rgm
- Fix URL issue

* Tue Mar 12 2019 Michael Aubertin <maubertin@fr.scc.com> - 0.4.3-1.rgm
- Initial release

