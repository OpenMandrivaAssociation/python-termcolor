Name:		python-termcolor
Version:	3.3.0
Release:	2
Source0:	https://files.pythonhosted.org/packages/source/t/termcolor/termcolor-%{version}.tar.gz
Summary:	ANSI color formatting for output in terminal
URL:		https://pypi.org/project/termcolor/
License:	MIT
Group:		Development/Python
BuildSystem:	python
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(hatchling)
BuildRequires:	python%{pyver}dist(hatch-vcs)
BuildArch:	noarch

%description
ANSI color formatting for output in terminal

%build -p
# The sdist is not a git checkout, so the versioning backend needs the version.
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}

%files
%{py_sitedir}/termcolor
%{py_sitedir}/termcolor-*.*-info
