Name: sailfishos-patch-voicecall-quickaction
BuildArch: noarch
Summary: Adds a quick action to call a specific number
Version: 0.3
Release: 1
Group: System/Patches
License: GPLv3
Source0: %{name}-%{version}.tar.xz
Requires: patchmanager
Requires: sailfish-version >= 2.0.0

%description
%{summary}

%prep
%setup -q -n %{name}-%{version}


%build

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}/usr/share/patchmanager/patches/%{name}
cp -r patch/* %{buildroot}/usr/share/patchmanager/patches/%{name}

mkdir -p %{buildroot}/usr/share/lipstick/quickactions
cp com.jolla.* %{buildroot}/usr/share/lipstick/quickactions

mkdir -p %{buildroot}/usr/share/themes/jolla-ambient/meegotouch/z1.0/icons
cp -r icons/* %{buildroot}/usr/share/themes/jolla-ambient/meegotouch/z1.0/icons

mkdir -p %{buildroot}/usr/share/translations
cp -r translations/* %{buildroot}/usr/share/translations

mkdir -p %{buildroot}/usr/share/jolla-settings/entries
cp -r settings/* %{buildroot}/usr/share/jolla-settings/entries

%pre
if [ -d /var/lib/patchmanager/ausmt/patches/%{name} ]; then
/usr/sbin/patchmanager -u %{name} || true
fi

%preun
if [ -d /var/lib/patchmanager/ausmt/patches/%{name} ]; then
/usr/sbin/patchmanager -u %{name} || true
fi

%files
%defattr(-,root,root,-)
%{_datadir}/patchmanager/patches/%{name}
%{_datadir}/lipstick/quickactions/com.jolla.voicecall.conf
%{_datadir}/themes/jolla-ambient/meegotouch/z1.0/icons
%{_datadir}/translations
%{_datadir}/jolla-settings/entries
