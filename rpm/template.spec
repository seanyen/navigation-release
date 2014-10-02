Name:           ros-indigo-base-local-planner
Version:        1.11.13
Release:        0%{?dist}
Summary:        ROS base_local_planner package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/base_local_planner
Source0:        %{name}-%{version}.tar.gz

Requires:       eigen3-devel
Requires:       ros-indigo-angles
Requires:       ros-indigo-costmap-2d
Requires:       ros-indigo-dynamic-reconfigure
Requires:       ros-indigo-geometry-msgs
Requires:       ros-indigo-message-generation
Requires:       ros-indigo-nav-core
Requires:       ros-indigo-nav-msgs
Requires:       ros-indigo-pcl-ros
Requires:       ros-indigo-pluginlib
Requires:       ros-indigo-rosconsole
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-rospy
Requires:       ros-indigo-std-msgs
Requires:       ros-indigo-tf
Requires:       ros-indigo-visualization-msgs
Requires:       ros-indigo-voxel-grid
BuildRequires:  eigen3-devel
BuildRequires:  ros-indigo-angles
BuildRequires:  ros-indigo-catkin >= 0.5.68
BuildRequires:  ros-indigo-cmake-modules
BuildRequires:  ros-indigo-costmap-2d
BuildRequires:  ros-indigo-dynamic-reconfigure
BuildRequires:  ros-indigo-geometry-msgs
BuildRequires:  ros-indigo-message-generation
BuildRequires:  ros-indigo-nav-core
BuildRequires:  ros-indigo-nav-msgs
BuildRequires:  ros-indigo-pcl-conversions
BuildRequires:  ros-indigo-pcl-ros
BuildRequires:  ros-indigo-pluginlib
BuildRequires:  ros-indigo-rosconsole
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-rospy
BuildRequires:  ros-indigo-std-msgs
BuildRequires:  ros-indigo-tf
BuildRequires:  ros-indigo-visualization-msgs
BuildRequires:  ros-indigo-voxel-grid

%description
This package provides implementations of the Trajectory Rollout and Dynamic
Window approaches to local robot navigation on a plane. Given a plan to follow
and a costmap, the controller produces velocity commands to send to a mobile
base. This package supports both holonomic and non-holonomic robots, any robot
footprint that can be represented as a convex polygon or circle, and exposes its
configuration as ROS parameters that can be set in a launch file. This package's
ROS wrapper adheres to the BaseLocalPlanner interface specified in the nav_core
package.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p build && cd build
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd build
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Thu Oct 02 2014 David V. Lu!! <davidvlu@gmail.com> - 1.11.13-0
- Autogenerated by Bloom

* Wed Oct 01 2014 David V. Lu!! <davidvlu@gmail.com> - 1.11.12-0
- Autogenerated by Bloom

