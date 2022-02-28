Name:		fermilab-conf_ca-certs
Version:	2019.01
Release:	2
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

Requires(post): /bin/bash coreutils ca-certificates
Requires(postun): /bin/bash coreutils ca-certificates

%description
Authentication Services operates a non-accredited CA that is
integrated with the FERMI and SERVICES domains.

%prep
%setup -q -n %{name}


%build


%install
%{__rm} -rf %{buildroot}
%{__mkdir_p} %{buildroot}%{_datadir}/pki/ca-trust-source/anchors/
%{__mv} *.pem %{buildroot}%{_datadir}/pki/ca-trust-source/anchors/


%files
%attr(0644,root,root) %{_datadir}/pki/ca-trust-source/anchors/*


%post -p /bin/bash
update-ca-trust >/dev/null
exit 0


%postun -p /bin/bash
update-ca-trust >/dev/null
exit 0


%changelog
* Fri Jan 11 2019 Olga Terlyga <terlyga@fnal.gov> 2019.01-2
- Initial Build
