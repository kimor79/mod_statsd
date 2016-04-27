%define debug_package %{nil}
%define _unpackaged_files_terminate_build 0

Name:           mod_statsd
Version:        0.0.1
Release:        1
License:        GPL 
URL:            https://github.com/andremichi/mod_statsd/
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  gcc make libffi-devel httpd-devel
Source0:	https://github.com/andremichi/mod_statsd/%{name}.tar.bz2
Summary:        An interpreter of object-oriented scripting language
Group:          Development/Languages

%description
mod_statsd

%prep
%setup -n mod_statsd

%build
export CFLAGS="$RPM_OPT_FLAGS -Wall -fno-strict-aliasing"
mkdir -p $RPM_BUILD_DIR/usr/lib64/httpd/modules
make %{?_smp_mflags}
/usr/lib64/apr-1/build/libtool --silent --mode=link gcc -std=gnu99 -Wl,-z,relro,-z,now   -o mod_statsd.la -Wall -lm  -rpath $RPM_BUILD_DIR/usr/lib64/httpd/modules -module -avoid-version    mod_statsd.lo
/usr/lib64/httpd/build/instdso.sh SH_LIBTOOL='/usr/lib64/apr-1/build/libtool' mod_statsd.la $RPM_BUILD_DIR/usr/lib64/httpd/modules
/usr/lib64/apr-1/build/libtool --mode=install install mod_statsd.la $RPM_BUILD_DIR/usr/lib64/httpd/modules/

%install
mkdir -p $RPM_BUILD_ROOT/usr/lib64/httpd/modules
mkdir -p $RPM_BUILD_ROOT/etc/httpd/conf.modules.d

# installing binaries ...

cp -a $RPM_BUILD_DIR/statsd.load $RPM_BUILD_ROOT/etc/httpd/conf.modules.d/statsd.conf
cp -a $RPM_BUILD_DIR/usr/lib64/httpd/modules/* $RPM_BUILD_ROOT/usr/lib64/httpd/modules/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
/usr/lib64/httpd/modules/
/etc/httpd/conf.modules.d/

%post
systemctl reload httpd || true

%preun

%changelog
