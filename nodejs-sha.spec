%{?scl:%scl_package nodejs-sha}
%{!?scl:%global pkg_name %{name}}

%{?nodejs_find_provides_and_requires}

Name:           %{?scl_prefix}nodejs-sha
Version:        2.0.1
Release:        3.1%{?dist}
Summary:        Check and get file hashes
BuildArch:      noarch
ExclusiveArch: %{nodejs_arches} noarch

License:        BSD or MIT
URL:            https://github.com/ForbesLindesay/sha
Source0:        http://registry.npmjs.org/sha/-/sha-%{version}.tgz
BuildRequires:  %{?scl_prefix}nodejs-devel

%description
Check and get file hashes using MD5, SHA1, or any other algorithm supported by
OpenSSL.

%prep
%setup -q -n package

#move tests into regular directory
#mv sha-%{commit}/test .
#rm -rf sha-%{commit}

#fix EOL encodings
sed -i 's/\r//g' README.md

%build
#nothing to do

%install

mkdir -p %{buildroot}%{nodejs_sitelib}/sha
cp -pr index.js package.json %{buildroot}%{nodejs_sitelib}/sha

%nodejs_symlink_deps

#%check
#%nodejs_symlink_deps --check
#mocha -R list


%files
%{nodejs_sitelib}/sha
%doc README.md LICENSE

%changelog
* Sun Feb 14 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 2.0.1-3.1
- rebuilt

* Fri Nov 27 2015 Tomas Hrcka <thrcka@redhat.com> - 2.0.1-2.1
- Rebase to latest upstream

* Fri Nov 08 2013 Tomas Hrcka <thrcka@redhat.com> - 1.2.1-1.1
- Software collections support

* Tue Jul 30 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.2.1-1
- new upstream release 1.2.1

* Fri Jul 12 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.0.1-4
- fix graceful-fs dep

* Sat Jun 22 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.0.1-3
- restrict to compatible arches

* Thu May 30 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.0.1-2
- use github tarball instead so we get tests and LICENSE file

* Thu May 30 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.0.1-1
- initial package
