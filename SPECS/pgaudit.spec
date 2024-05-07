Name:		pgaudit
Version:	1.7.0
Release:	1%{?dist}
Summary:	PostgreSQL Audit Extension

License:	PostgreSQL
URL:		http://pgaudit.org

Source0:	https://github.com/%{name}/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires: gcc
BuildRequires: make
BuildRequires: postgresql-server-devel >= 15
BuildRequires: openssl-devel

%{?postgresql_module_requires}

%description
The PostgreSQL Audit extension (pgaudit) provides detailed session
and/or object audit logging via the standard PostgreSQL logging
facility.

The goal of the PostgreSQL Audit extension (pgaudit) is to provide
PostgreSQL users with capability to produce audit logs often required to
comply with government, financial, or ISO certifications.

An audit is an official inspection of an individual's or organization's
accounts, typically by an independent body. The information gathered by
the PostgreSQL Audit extension (pgaudit) is properly called an audit
trail or audit log. The term audit log is used in this documentation.


%prep
%setup -q -n %{name}-%{version}


%build
%make_build USE_PGXS=1 PG_CONFIG=/usr/bin/pg_server_config

%install
%make_install USE_PGXS=1 PG_CONFIG=/usr/bin/pg_server_config

%files
%doc README.md
%license LICENSE
%{_libdir}/pgsql/%{name}.so
%{_datadir}/pgsql/extension/%{name}--1*.sql
%{_datadir}/pgsql/extension/%{name}.control


%changelog
* Wed Oct 19 2022 Filip Janus <fjanus@redhat.com> - 1.7.0-1
- Update to 1.7.0
- Support postgresql 15
- Related: #2128241

* Wed Nov 18 2020 Honza Horak <hhorak@redhat.com> - 1.5.0-1
- Update to version 1.5.0
  Related: #1855776

* Wed Nov 20 2019 Patrik Novotný <panovotn@redhat.com> - 1.4.0-4
- Bump release for rebuild against libpq-12.1-3

* Tue Nov 12 2019 Patrik Novotný <panovotn@redhat.com> - 1.4.0-3
- BuildRequires libpq-devel

* Tue Nov 12 2019 Patrik Novotný <panovotn@redhat.com> - 1.4.0-2
- BuildRequires postgresql-server-devel

* Wed Oct 02 2019 Patrik Novotný <panovotn@redhat.com> - 1.4.0-1
- Update to 1.4.0

* Sat Jul 27 2019 Honza Horak <hhorak@redhat.com> - 1.3.1-1
- Update to 1.3.1 and apply patch for pgsql v12 compatibility

* Thu Jul 25 2019 Honza Horak <hhorak@redhat.com> - 1.2.0-4
- SCLize the SPEC

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Dec 20 2017 - Filip Čáp <ficap@redhat.com> 1.2.0-1
- Initial RPM packaging for Fedora
- Based on Devrim Gündüz's packaging for PostgreSQL RPM Repo

* Thu Oct 27 2016 - Devrim Gündüz <devrim@gunduz.org> 1.0.0-1
- Update to 1.0.0

* Fri Oct 21 2016 - Devrim Gündüz <devrim@gunduz.org> 0.0.4-1
- Initial RPM packaging for PostgreSQL RPM Repository
