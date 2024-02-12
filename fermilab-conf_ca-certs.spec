Name:		fermilab-conf_ca-certs
Version:	2019.01
Release:	3
Summary:	List of Fermilab Certificate Authorities

Group:		Fermilab
License:	MIT
URL:		https://authentication.fnal.gov/certs/

Source0:	%{name}.tar.gz

# Old package, can drop with SL8 release, leaving in for SL7 for now
Obsoletes:	zz_cacerts_for_slf

BuildArch:	noarch
BuildRequires:	bash coreutils findutils openssl
Requires:	ca-certificates >= 2018.1

%description
Authentication Services operates a non-accredited CA that is
integrated with the FERMI and SERVICES domains.

%package trust
Summary:        Trust the List of Fermilab Certificate Authorities

Requires(post): /bin/bash coreutils ca-certificates
Requires(postun): /bin/bash coreutils ca-certificates

%description trust
Authentication Services operates a non-accredited CA that is
integrated with the FERMI and SERVICES domains.

These will be added to your CA trust store.

%prep
%setup -q -n %{name}


%build


%install
%{__rm} -rf %{buildroot}
%{__mkdir_p} %{buildroot}%{_datadir}/pki/ca-trust-source/anchors/
%{__cp} *.pem %{buildroot}%{_datadir}/pki/ca-trust-source/anchors/

%{__mkdir_p} %{buildroot}%{_datadir}/fermilab-conf_ca-certs/
%{__cp} *.pem %{buildroot}%{_datadir}/fermilab-conf_ca-certs/


%files
%attr(0644,root,root) %{_datadir}/fermilab-conf_ca-certs/*

%files trust
%attr(0644,root,root) %{_datadir}/pki/ca-trust-source/anchors/*


%post trust -p /bin/bash
update-ca-trust >/dev/null
exit 0


%postun trust -p /bin/bash
update-ca-trust >/dev/null
exit 0


%changelog
* Mon Feb 12 2024 Pat Riehecky <riehecky@fnal.gov> 2019.01-3
- Seperate trust from just local deployment

* Fri Jan 11 2019 Olga Terlyga <terlyga@fnal.gov> 2019.01-2
- Initial Build
