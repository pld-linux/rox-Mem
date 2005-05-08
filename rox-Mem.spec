%define _name Mem
%define _platform %(echo `uname -s`-`uname -m|sed 's/i.86/ix86/'`)
Summary:	ROX-Mem displays the current memory usage
Summary(pl):	ROX-Mem wy¶wietla bie¿±ce zu¿ycie pamiêci
Name:		rox-%{_name}
Version:	2.1.3
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://www.kerofin.demon.co.uk/rox/%{_name}-%{version}.tar.gz
# Source0-md5:	58d0fb4d42860ea3c6c2bbd9251bb3a9
Source1:	%{name}.desktop
#Patch0:	%{name}-paths-fix.patch
Patch1:		%{name}-ROX-CLib2-include.patch
Patch2:		%{name}-ROX-apps-paths.patch
Patch3:		%{name}-aclocal.patch
Patch4:		%{name}-Choices-dir.patch
URL:		http://www.kerofin.demon.co.uk/rox/mem.html
BuildRequires:	autoconf
BuildRequires:	glib2-devel >= 2.0.3
BuildRequires:	gtk+2-devel >= 2.0.1
BuildRequires:	libgtop-devel >= 2.6.0
BuildRequires:	libxml2-devel >= 2.4.0
BuildRequires:	pkgconfig >= 0.9.0
BuildRequires:	rox-CLib2-devel >= 2.1.4
Requires:	rox >= 2.2.0-2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appsdir	%{_libdir}/ROX-apps

%description
ROX-Mem can function as a ROX applet or a standalone program and
displays the current real memory usage and the current swap space
usage.

%description -l pl
ROX-Mem mo¿e funkcjonowaæ jako aplet ROXa lub jako oddzielny program.
Wy¶witla on bie¿±ce zu¿ycie pamiêci oraz swapu.

%prep
%setup -q -n %{_name}
#%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
cd src
%{__autoconf}
cd ..
./AppRun --compile

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_appsdir}/%{_name}/{Help,%{_platform}}
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

install .DirIcon *.xml choice_install gtkrc rox_run $RPM_BUILD_ROOT%{_appsdir}/%{_name}
install AppRun AppletRun $RPM_BUILD_ROOT%{_appsdir}/%{_name}
install Help/README $RPM_BUILD_ROOT%{_appsdir}/%{_name}/Help
install %{_platform}/Mem $RPM_BUILD_ROOT%{_appsdir}/%{_name}/%{_platform}
install .DirIcon $RPM_BUILD_ROOT%{_pixmapsdir}/%{name}.png

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Help/{Changes,README,Versions}
%attr(755,root,root) %{_appsdir}/%{_name}/*[Rr]un
%attr(755,root,root) %{_appsdir}/%{_name}/choice_install
%attr(755,root,root) %{_appsdir}/%{_name}/%{_platform}
%dir %{_appsdir}/%{_name}
%{_appsdir}/%{_name}/.DirIcon
%{_appsdir}/%{_name}/*.xml
%{_appsdir}/%{_name}/gtkrc
%{_appsdir}/%{_name}/Help
%{_pixmapsdir}/%{name}.png
%{_desktopdir}/%{name}.desktop
