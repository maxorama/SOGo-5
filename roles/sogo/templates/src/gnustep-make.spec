#
# This file is to be manually edited.  The current version is very
# old.  You probably want to install into the Linux FHS, which
# this doesn't do.
#
# This package is not relocatable
#
%define gs_version	2.7.0
%define gs_name         gnustep-make
%define gs_prefix 	/usr/GNUstep
%define gs_libcombo     gnu-gnu-gnu
#
Name: 		%{gs_name}
Version: 	%{gs_version}
Release: 	1
Source: 	ftp://ftp.gnustep.org/pub/gnustep/core/%{gs_name}-%{gs_version}.tar.gz
License: 	GPL
Group: 		System Environment/Base
Summary: 	GNUstep Makefile package
Packager:	GNUstep Development <bug-gnustep@gnu.org>
Vendor:		The GNUstep Project
URL:		http://www.gnustep.org/
BuildRoot: 	/var/tmp/build-%{gs_name}
#

%description
This package contains the basic scripts, makefiles and directory
layout needed to run and compile any GNUstep software.  This package
was configured for library combo %{gs_libcombo} using the standard
GNUstep filesystem layout based on %{gs_prefix}.

%prep
%setup -n %{gs_name}-%{gs_version}

%build
CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=%{gs_prefix} --with-library-combo=%{gs_libcombo} --with-layout=gnustep
make

%install
make install DESTDIR=${RPM_BUILD_ROOT}

%ifos Linux
mkdir -p ${RPM_BUILD_ROOT}/etc/profile.d

# Create profile files

echo "#!/bin/sh" > mygnustep.sh
echo ". %{gs_prefix}/System/Library/Makefiles/GNUstep.sh" >> mygnustep.sh

#echo "#!/bin/csh" > mygnustep.csh
#echo "source %{gs_prefix}/System/Library/Makefiles/GNUstep.csh" >> mygnustep.csh

chmod 755 mygnustep.*
mv mygnustep.sh $RPM_BUILD_ROOT/etc/profile.d/GNUstep.sh
#mv mygnustep.csh $RPM_BUILD_ROOT/etc/profile.d/GNUstep.csh
%endif # Linux

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, root)

# Well - this is the simplest trick you could think of.  We include in
# the package everything which was installed inside /usr/GNUstep/
%{gs_prefix}

# Also include the GNUstep config file
/etc/GNUstep/GNUstep.conf

# Add the profiles for linux as configuration files <FIXME gdomap etc>
%ifos Linux
%config /etc/profile.d/GNUstep.sh
#%config /etc/profile.d/GNUstep.csh
%endif # Linux

