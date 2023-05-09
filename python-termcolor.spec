Name:		python-termcolor
Version:	2.3.0
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/t/termcolor/termcolor-%{version}.tar.gz
Summary:	ANSI color formatting for output in terminal
URL:		https://pypi.org/project/termcolor/
License:	MIT
Group:		Development/Python
BuildRequires:	python%{pyver}dist(pip)
BuildArch:	noarch

%description
ANSI color formatting for output in terminal

%prep
%autosetup -p1 -n termcolor-%{version}

%build
%py_build

%install
%py_install

%files
%{py_sitedir}/termcolor
%{py_sitedir}/termcolor-*.*-info
