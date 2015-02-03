Name:           ros-hydro-move-base
Version:        1.11.15
Release:        0%{?dist}
Summary:        ROS move_base package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/move_base
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-hydro-actionlib
Requires:       ros-hydro-base-local-planner
Requires:       ros-hydro-clear-costmap-recovery
Requires:       ros-hydro-costmap-2d
Requires:       ros-hydro-dynamic-reconfigure
Requires:       ros-hydro-geometry-msgs
Requires:       ros-hydro-message-runtime
Requires:       ros-hydro-move-base-msgs
Requires:       ros-hydro-nav-core
Requires:       ros-hydro-nav-msgs
Requires:       ros-hydro-navfn
Requires:       ros-hydro-pluginlib
Requires:       ros-hydro-roscpp
Requires:       ros-hydro-rospy
Requires:       ros-hydro-rotate-recovery
Requires:       ros-hydro-std-msgs
Requires:       ros-hydro-std-srvs
Requires:       ros-hydro-tf
Requires:       ros-hydro-visualization-msgs
BuildRequires:  ros-hydro-actionlib
BuildRequires:  ros-hydro-base-local-planner
BuildRequires:  ros-hydro-catkin
BuildRequires:  ros-hydro-clear-costmap-recovery
BuildRequires:  ros-hydro-cmake-modules
BuildRequires:  ros-hydro-costmap-2d
BuildRequires:  ros-hydro-dynamic-reconfigure
BuildRequires:  ros-hydro-geometry-msgs
BuildRequires:  ros-hydro-message-generation
BuildRequires:  ros-hydro-move-base-msgs
BuildRequires:  ros-hydro-nav-core
BuildRequires:  ros-hydro-nav-msgs
BuildRequires:  ros-hydro-navfn
BuildRequires:  ros-hydro-pluginlib
BuildRequires:  ros-hydro-roscpp
BuildRequires:  ros-hydro-rospy
BuildRequires:  ros-hydro-rotate-recovery
BuildRequires:  ros-hydro-std-msgs
BuildRequires:  ros-hydro-std-srvs
BuildRequires:  ros-hydro-tf
BuildRequires:  ros-hydro-visualization-msgs

%description
The move_base package provides an implementation of an action (see the actionlib
package) that, given a goal in the world, will attempt to reach it with a mobile
base. The move_base node links together a global and local planner to accomplish
its global navigation task. It supports any global planner adhering to the
nav_core::BaseGlobalPlanner interface specified in the nav_core package and any
local planner adhering to the nav_core::BaseLocalPlanner interface specified in
the nav_core package. The move_base node also maintains two costmaps, one for
the global planner, and one for a local planner (see the costmap_2d package)
that are used to accomplish navigation tasks.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/hydro" \
        -DCMAKE_PREFIX_PATH="/opt/ros/hydro" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/hydro

%changelog
* Tue Feb 03 2015 David V. Lu!! <davidvlu@gmail.com> - 1.11.15-0
- Autogenerated by Bloom

* Fri Dec 05 2014 David V. Lu!! <davidvlu@gmail.com> - 1.11.14-0
- Autogenerated by Bloom

* Thu Oct 02 2014 David V. Lu!! <davidvlu@gmail.com> - 1.11.13-0
- Autogenerated by Bloom

* Wed Oct 01 2014 David V. Lu!! <davidvlu@gmail.com> - 1.11.12-0
- Autogenerated by Bloom

