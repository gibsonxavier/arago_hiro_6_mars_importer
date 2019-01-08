%define name put_mars_nodes
%define version 1.0.0
%define unmangled_version 1.0.0
%define unmangled_version 1.0.0
%define release 1
%define source_dir /Users/gxavier/git/arago_hiro_6_mars_importer
Summary: Inject MARS files into HIRO graph
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{unmangled_version}.tar.bz2
License: MIT
Group: Development/Libraries
BuildRoot: %{source_dir}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Gibson Xavier <gxavier@arago.de>
Packager: Gibson Xavier <gxavier@arago.de>
Requires: python-docopt python-lxml python-requests python-gevent python-jsonschema
Url: https://github.com/gibsonxavier/mars_importer

%description
Tool to import MARS model data created by the Java Excel to MARS utility for HIRO 6

%prep
%setup -n %{name}-%{unmangled_version} -n %{name}-%{unmangled_version}

%build
python3 setup.py build

%install
python3 setup.py install --single-version-externally-managed -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%post
#!/bin/bash


DEFAULT_DIRECTORY='/usr/local/etc/mars_importer/'
CURRENT_DIRECTORY=$PWD

if [ ! -d "$DIRECTORY" ]; then
  mkdir -p $DIRECTORY
fi

if [ -d "$DIRECTORY" ]; then
  mv $CURRENT_DIRECTORY/graphit.conf $DEFAULT_DIRECTORY
  mv $CURRENT_DIRECTORY/put_mars_node.py $DEFAULT_DIRECTORY
  mv $CURRENT_DIRECTORY/helper.py $DEFAULT_DIRECTORY
  chmod -R 755 $DEFAULT_DIRECTORY/put_mars_node.py
  chmod -R 755 $DEFAULT_DIRECTORY/helper.py
  chmod -R 644 $DEFAULT_DIRECTORY/graphit.conf
fi

if [  -f $DEFAULT_DIRECTORY/put_mars_node.py ]; then
    ln -s $CURRENT_DIRECTORY/put_mars_node.py /usr/local/bin/put_mars_nodes
fi


%files -f INSTALLED_FILES
%defattr(-,root,root)
