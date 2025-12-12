Name:		python-jaraco.classes
Version:	3.4.0
Release:	2
Source0:	https://files.pythonhosted.org/packages/source/j/jaraco.classes/jaraco.classes-%{version}.tar.gz
Summary:	Utility functions for Python class constructs
URL:		https://pypi.org/project/jaraco.classes/
License:	GPL
Group:		Development/Python
BuildRequires:	python%{pyver}dist(pip)
BuildArch:	noarch

%description
Utility functions for Python class constructs

%prep
%autosetup -p1 -n jaraco.classes-%{version}

%build
%py_build

%install
%py_install

%files
%{py_sitedir}/jaraco
%{py_sitedir}/jaraco.classes-*.*-info
