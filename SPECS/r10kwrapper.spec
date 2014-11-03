%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

%define module_name r10kwrapper
%define _unpackaged_files_terminate_build 0 
%define _missing_doc_files_terminate_build 0

Name:           %{module_name}
Version:        0.2.1
Release:        1
Summary:        r10kwrapper - A tool that does a bit of automation and management around the use of the r10k command.

License:        The FreeBSD Copyright
URL:            https://github.com/jonkelleyatrackspace/r10kwrapper
Source0:        %{module_name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python-setuptools
Requires: python-setuptools

%description

%prep
%setup -q -n %{module_name}-%{version}


%build


%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install --root $RPM_BUILD_ROOT

%files
#%doc README.md
%{python_sitelib}/*
%attr(0755,-,-) %{_bindir}/r10kwrapper

%changelog
* Thu Nov 3 2014 Jonathan Kelley <jon.kelley@rackspace.com> - 0.2.1
- Fixing by adding python-setuptools dependecy
* Thu Oct 2 2014 Jonathan Kelley <jon.kelley@rackspace.com> - 0.1.2
- Initial spec
