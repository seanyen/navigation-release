Name:           ros-melodic-navfn
Version:        1.16.2
Release:        0%{?dist}
Summary:        ROS navfn package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/navfn
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-melodic-costmap-2d
Requires:       ros-melodic-geometry-msgs
Requires:       ros-melodic-message-runtime
Requires:       ros-melodic-nav-core
Requires:       ros-melodic-nav-msgs
Requires:       ros-melodic-pluginlib
Requires:       ros-melodic-rosconsole
Requires:       ros-melodic-roscpp
Requires:       ros-melodic-sensor-msgs
Requires:       ros-melodic-tf2-ros
Requires:       ros-melodic-visualization-msgs
BuildRequires:  netpbm-devel
BuildRequires:  ros-melodic-catkin >= 0.5.68
BuildRequires:  ros-melodic-cmake-modules
BuildRequires:  ros-melodic-costmap-2d
BuildRequires:  ros-melodic-geometry-msgs
BuildRequires:  ros-melodic-message-generation
BuildRequires:  ros-melodic-nav-core
BuildRequires:  ros-melodic-nav-msgs
BuildRequires:  ros-melodic-pluginlib
BuildRequires:  ros-melodic-rosconsole
BuildRequires:  ros-melodic-roscpp
BuildRequires:  ros-melodic-rosunit
BuildRequires:  ros-melodic-sensor-msgs
BuildRequires:  ros-melodic-tf2-ros
BuildRequires:  ros-melodic-visualization-msgs

%description
navfn provides a fast interpolated navigation function that can be used to
create plans for a mobile base. The planner assumes a circular robot and
operates on a costmap to find a minimum cost plan from a start point to an end
point in a grid. The navigation function is computed with Dijkstra's algorithm,
but support for an A* heuristic may also be added in the near future. navfn also
provides a ROS wrapper for the navfn planner that adheres to the
nav_core::BaseGlobalPlanner interface specified in nav_core.

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
* Tue Jul 31 2018 David V. Lu!! <davidvlu@gmail.com> - 1.16.2-0
- Autogenerated by Bloom

* Sat Jul 28 2018 David V. Lu!! <davidvlu@gmail.com> - 1.16.1-0
- Autogenerated by Bloom

* Wed Jul 25 2018 David V. Lu!! <davidvlu@gmail.com> - 1.16.0-0
- Autogenerated by Bloom

