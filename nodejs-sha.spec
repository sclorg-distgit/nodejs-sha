%{?scl:%scl_package nodejs-sha}
%{!?scl:%global pkg_name %{name}}

%{?nodejs_find_provides_and_requires}

%global commit 07d43b5ebf7b7ddb83e44b594005097e21e43702
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           %{?scl_prefix}nodejs-sha
Version:        2.0.1
Release:        2.1%{?dist}
Summary:        Check and get file hashes
BuildArch:      noarch
ExclusiveArch: %{nodejs_arches} noarch

Group:          Development/Libraries
License:        BSD or MIT
URL:            https://github.com/ForbesLindesay/sha
Source0:        http://registry.npmjs.org/sha/-/sha-%{version}.tgz
# the npm tarball doesn't contain the tests, so we grab it from github instead
# oh, and now it seems to be a version behind npm.  swell.
Source1:        https://github.com/ForbesLindesay/sha/archive/%{commit}/sha-%{version}-%{shortcommit}.tar.gz
BuildRoot:      %{_tmppath}/%{pkg_name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  %{?scl_prefix}nodejs-devel

#for tests
#BuildRequires:  %{?scl_prefix}npm(mocha)
#BuildRequires:  %{?scl_prefix}npm(graceful-fs)

%description
Check and get file hashes using MD5, SHA1, or any other algorithm supported by
OpenSSL.

%prep
%setup -q -n package -a1

#move tests into regular directory
mv sha-%{commit}/test .
rm -rf sha-%{commit}

#fix EOL encodings
sed -i 's/\r//g' README.md

#we don't currently support optionalDependencies properly so make it mandatory
#we don't need this in scl since user install whole collection at once
#%nodejs_fixdep graceful-fs '2' 

%build
#nothing to do

%install
rm -rf %buildroot

mkdir -p %{buildroot}%{nodejs_sitelib}/sha
cp -pr index.js package.json %{buildroot}%{nodejs_sitelib}/sha

%nodejs_symlink_deps

%check
#%nodejs_symlink_deps --check
#mocha -R list

%clean
rm -rf %buildroot

%files
%defattr(-,root,root,-)
%{nodejs_sitelib}/sha
%doc README.md LICENSE

%changelog
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
