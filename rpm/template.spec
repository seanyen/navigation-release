Name:           ros-melodic-navigation
Version:        1.16.2
Release:        0%{?dist}
Summary:        ROS navigation package

Group:          Development/Libraries
License:        BSD,LGPL,LGPL (amcl)
URL:            http://wiki.ros.org/navigation
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-melodic-amcl
Requires:       ros-melodic-base-local-planner
Requires:       ros-melodic-carrot-planner
Requires:       ros-melodic-clear-costmap-recovery
Requires:       ros-melodic-costmap-2d
Requires:       ros-melodic-dwa-local-planner
Requires:       ros-melodic-fake-localization
Requires:       ros-melodic-global-planner
Requires:       ros-melodic-map-server
Requires:       ros-melodic-move-base
Requires:       ros-melodic-move-base-msgs
Requires:       ros-melodic-move-slow-and-clear
Requires:       ros-melodic-nav-core
Requires:       ros-melodic-navfn
Requires:       ros-melodic-rotate-recovery
Requires:       ros-melodic-voxel-grid
BuildRequires:  ros-melodic-catkin

%description
A 2D navigation stack that takes in information from odometry, sensor streams,
and a goal pose and outputs safe velocity commands that are sent to a mobile
base.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/melodic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/melodic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/melodic

%changelog
* Tue Jul 31 2018 Michael Ferguson <mfergs7@gmail.com> - 1.16.2-0
- Autogenerated by Bloom

* Sat Jul 28 2018 Michael Ferguson <mfergs7@gmail.com> - 1.16.1-0
- Autogenerated by Bloom

* Wed Jul 25 2018 Michael Ferguson <mfergs7@gmail.com> - 1.16.0-0
- Autogenerated by Bloom

