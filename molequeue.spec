Name:		molequeue
Version:	0.9.0
Release:	2
Summary:	Desktop integration of high performance computing resources
License:	BSD
Group:		Sciences/Chemistry
Url:		http://openchemistry.org/molequeue
Source0:	https://github.com/OpenChemistry/molequeue/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:	cmake ninja
BuildRequires:	cmake(ECM)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5Network)
BuildRequires:	pkgconfig(Qt5Widgets)

%description
MoleQueue is an open-source, cross-platform, system-tray resident desktop
application for abstracting, managing, and coordinating the execution of
tasks both locally and on remote computational resources. Users can set
up local and remote queues that describe where the task will be executed.
Each queue can have programs, with templates to facilitate the execution
of the program. Input files can be staged, and output files collected
using a standard interface. Some highlights:

  * Open source distributed under the liberal 3-clause BSD license
  * Cross platform with nightly builds on Linux, Mac OS X and Windows
  * Intuitive interface designed to be useful to whole community
  * Support for local executation and remote schedulers (SGE, PBS, SLURM)
  * System tray resident application managing queue of queues and job lifetime
  * Simple, lightweight JSON-RPC 2.0 based communication over local sockets
  * Qt 5 client library for simple integration in Qt applications

#----------------------------------------------------

%package	devel
Summary:	Development files for %{name}
Group:		Development/Other
Requires:	%{name} >= %{version}-%{release}

%description	devel
The %{name}-devel package contains header files for developing applications
that use %{name}.

%prep
%setup -q
%autopatch -p1

%build
%cmake_qt5 \
	-G Ninja
%ninja_build

%install
%ninja_install -C build

%files
%license LICENSE
%{_docdir}/MoleQueue
%{_bindir}/%{name}
%{_libdir}/%{name}/
%{_libdir}/*.so

%files devel
%{_includedir}/%{name}/
%{_libdir}/cmake/%{name}/
