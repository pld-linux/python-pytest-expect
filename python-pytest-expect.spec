#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	py.test plugin to store test expectations and mark tests based on them
Summary(pl.UTF-8):	Wtyczka py.test do zapisywania oczekiwań testów oraz oznaczania testów w oparciu o nie
Name:		python-pytest-expect
Version:	1.1.0
Release:	4
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.python.org/simple/pytest-expect/
Source0:	https://files.pythonhosted.org/packages/source/p/pytest-expect/pytest-expect-%{version}.tar.gz
# Source0-md5:	f74155c66f255364bf523d29e9bffe3e
URL:		https://github.com/tholo/pytest-expect
%if %{with python2}
BuildRequires:	python-modules >= 1:2.6
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-pytest
BuildRequires:	python-six
BuildRequires:	python-u-msgpack
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-pytest
BuildRequires:	python3-six
BuildRequires:	python3-u-msgpack
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A py.test plugin that stores test expectations by saving the set of
failing tests, allowing them to be marked as xfail when running them
in future. The tests expectations are stored such that they can be
distributed alongside the tests.

%description -l pl.UTF-8
Wtyczka py.test zapisująca oczekiwania testów poprzez zapis zbioru
testów kończących się niepowodzeniem, pozwalając na zaznaczenie ich
jako xfail (spodziewane niepowodzenie) przy uruchamianiu w
przyszłości. Oczekiwania testów są zapisywane w taki sposób, że mogą
być rozprowadzane wraz z testami.

%package -n python3-pytest-expect
Summary:	py.test plugin to store test expectations and mark tests based on them
Summary(pl.UTF-8):	Wtyczka py.test do zapisywania oczekiwań testów oraz oznaczania testów w oparciu o nie
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.2

%description -n python3-pytest-expect
A py.test plugin that stores test expectations by saving the set of
failing tests, allowing them to be marked as xfail when running them
in future. The tests expectations are stored such that they can be
distributed alongside the tests.

%description -n python3-pytest-expect -l pl.UTF-8
Wtyczka py.test zapisująca oczekiwania testów poprzez zapis zbioru
testów kończących się niepowodzeniem, pozwalając na zaznaczenie ich
jako xfail (spodziewane niepowodzenie) przy uruchamianiu w
przyszłości. Oczekiwania testów są zapisywane w taki sposób, że mogą
być rozprowadzane wraz z testami.

%prep
%setup -q -n pytest-expect-%{version}

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc README.rst
%{py_sitescriptdir}/pytest_expect
%{py_sitescriptdir}/pytest_expect-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-pytest-expect
%defattr(644,root,root,755)
%doc README.rst
%{py3_sitescriptdir}/pytest_expect
%{py3_sitescriptdir}/pytest_expect-%{version}-py*.egg-info
%endif
