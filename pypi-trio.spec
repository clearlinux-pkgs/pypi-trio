#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-trio
Version  : 0.21.0
Release  : 5
URL      : https://files.pythonhosted.org/packages/0b/81/47c8b8fc5303bed06d284a49a114e10032d2cbfa1ac51bef15949abf1b54/trio-0.21.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/0b/81/47c8b8fc5303bed06d284a49a114e10032d2cbfa1ac51bef15949abf1b54/trio-0.21.0.tar.gz
Summary  : A friendly Python library for async concurrency and I/O
Group    : Development/Tools
License  : Apache-2.0 MIT
Requires: pypi-trio-license = %{version}-%{release}
Requires: pypi-trio-python = %{version}-%{release}
Requires: pypi-trio-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(async_generator)
BuildRequires : pypi(attrs)
BuildRequires : pypi(idna)
BuildRequires : pypi(outcome)
BuildRequires : pypi(sniffio)
BuildRequires : pypi(sortedcontainers)

%description
.. image:: https://img.shields.io/badge/chat-join%20now-blue.svg
:target: https://gitter.im/python-trio/general
:alt: Join chatroom

%package license
Summary: license components for the pypi-trio package.
Group: Default

%description license
license components for the pypi-trio package.


%package python
Summary: python components for the pypi-trio package.
Group: Default
Requires: pypi-trio-python3 = %{version}-%{release}

%description python
python components for the pypi-trio package.


%package python3
Summary: python3 components for the pypi-trio package.
Group: Default
Requires: python3-core
Provides: pypi(trio)
Requires: pypi(async_generator)
Requires: pypi(attrs)
Requires: pypi(idna)
Requires: pypi(outcome)
Requires: pypi(sniffio)
Requires: pypi(sortedcontainers)

%description python3
python3 components for the pypi-trio package.


%prep
%setup -q -n trio-0.21.0
cd %{_builddir}/trio-0.21.0
pushd ..
cp -a trio-0.21.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656367081
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-trio
cp %{_builddir}/trio-0.21.0/LICENSE.APACHE2 %{buildroot}/usr/share/package-licenses/pypi-trio/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/trio-0.21.0/LICENSE.MIT %{buildroot}/usr/share/package-licenses/pypi-trio/078fcfe40c1993810743750c91b85e5e5022b28c
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-trio/078fcfe40c1993810743750c91b85e5e5022b28c
/usr/share/package-licenses/pypi-trio/2b8b815229aa8a61e483fb4ba0588b8b6c491890

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
