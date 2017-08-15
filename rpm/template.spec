Name:           ros-kinetic-base-local-planner
Version:        1.14.2
Release:        0%{?dist}
Summary:        ROS base_local_planner package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/base_local_planner
Source0:        %{name}-%{version}.tar.gz

Requires:       eigen3-devel
Requires:       ros-kinetic-angles
Requires:       ros-kinetic-costmap-2d
Requires:       ros-kinetic-dynamic-reconfigure
Requires:       ros-kinetic-geometry-msgs
Requires:       ros-kinetic-message-runtime
Requires:       ros-kinetic-nav-core
Requires:       ros-kinetic-nav-msgs
Requires:       ros-kinetic-pcl-ros
Requires:       ros-kinetic-pluginlib
Requires:       ros-kinetic-roscpp
Requires:       ros-kinetic-rospy
Requires:       ros-kinetic-std-msgs
Requires:       ros-kinetic-tf
Requires:       ros-kinetic-voxel-grid
BuildRequires:  eigen3-devel
BuildRequires:  ros-kinetic-angles
BuildRequires:  ros-kinetic-catkin >= 0.5.68
BuildRequires:  ros-kinetic-cmake-modules
BuildRequires:  ros-kinetic-costmap-2d
BuildRequires:  ros-kinetic-dynamic-reconfigure
BuildRequires:  ros-kinetic-geometry-msgs
BuildRequires:  ros-kinetic-message-generation
BuildRequires:  ros-kinetic-nav-core
BuildRequires:  ros-kinetic-nav-msgs
BuildRequires:  ros-kinetic-pcl-conversions
BuildRequires:  ros-kinetic-pcl-ros
BuildRequires:  ros-kinetic-pluginlib
BuildRequires:  ros-kinetic-roscpp
BuildRequires:  ros-kinetic-rospy
BuildRequires:  ros-kinetic-rosunit
BuildRequires:  ros-kinetic-std-msgs
BuildRequires:  ros-kinetic-tf
BuildRequires:  ros-kinetic-voxel-grid

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
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Mon Aug 14 2017 David V. Lu!! <davidvlu@gmail.com> - 1.14.2-0
- Autogenerated by Bloom

* Mon Aug 07 2017 David V. Lu!! <davidvlu@gmail.com> - 1.14.1-0
- Autogenerated by Bloom

* Fri May 20 2016 David V. Lu!! <davidvlu@gmail.com> - 1.14.0-0
- Autogenerated by Bloom

