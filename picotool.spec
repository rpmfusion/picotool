Name:           picotool
Version:        2.3.1
Release:        %autorelease
Summary:        Tool for working with RP-series binaries and devices

License:        BSD-3-Clause
URL:            https://github.com/raspberrypi/picotool
Source0:        https://github.com/raspberrypi/picotool/archive/%{version}/picotool-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pico-sdk-source
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  arm-none-eabi-gcc-cs
BuildRequires:  arm-none-eabi-gcc-cs-c++
BuildRequires:  arm-none-eabi-newlib

%description
picotool is a tool for working with RP2040/RP2350 binaries, and interacting
with RP2040/RP2350 devices when they are in BOOTSEL mode.

%prep
%autosetup -p1

%build
%cmake -DPICO_SDK_PATH=/usr/share/pico-sdk -DUSE_PRECOMPILED=OFF
%cmake_build

%install
%cmake_install
install -Dp udev/60-picotool.rules %{buildroot}%{_prefix}/lib/udev/rules.d/60-picotool.rules

%files
%license LICENSE.TXT
%{_bindir}/picotool
%{_datadir}/picotool/
%{_prefix}/lib/cmake/picotool/
%{_prefix}/lib/udev/rules.d/60-picotool.rules

%changelog
%autochangelog
