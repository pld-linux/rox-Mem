%define _name Mem
%define _platform %(echo `uname -s`-`uname -m|sed 's/i.86/ix86/'`)
Summary:	ROX-Mem displays the current memory usage
Summary(pl):	ROX-Mem wy¶wietla bie¿±ce zu¿ycie pamiêci
Name:		rox-%{_name}
Version:	1.1.1
Release:	2
License:	GPL
Group:		X11/Applications
Source0:	http://www.kerofin.demon.co.uk/rox/%{_name}-%{version}.tgz
Patch0:		%{name}-libxml-includes.patch
Patch1:		%{name}-paths-fix.patch
URL:		http://www.kerofin.demon.co.uk/rox/utils.html#Mem
BuildRequires:	gtk+-devel
BuildRequires:	libgtop-devel
BuildRequires:	libxml2-devel
BuildRequires:	rox-CLib-devel >= 0.2.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define   _appsdir  %{_libdir}/ROX-apps

%description
ROX-Mem can function as a ROX applet or a standalone program and
displays the current real memory usage and the current swap space
usage.

%description -l pl
ROX-Mem mo¿e funkcjonowaæ jako aplet ROXa lub jako oddzielny program.
Wy¶witla on bie¿±ce zu¿ycie pamiêci oraz swapu.

%prep
%setup -q -n %{_name}
%patch0 -p1
%patch1 -p1

%build
./AppRun --compile

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_appsdir}/%{_name}/{Help,%{_platform}}

rm -f ../install
install App* choice_install rox_run gtkrc $RPM_BUILD_ROOT%{_appsdir}/%{_name}
install Help/README $RPM_BUILD_ROOT%{_appsdir}/%{_name}/Help
install %{_platform}/Mem $RPM_BUILD_ROOT%{_appsdir}/%{_name}/%{_platform}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Help/Versions
%attr(755,root,root) %{_appsdir}/%{_name}/*[Rr]un
%attr(755,root,root) %{_appsdir}/%{_name}/choice_install
%attr(755,root,root) %{_appsdir}/%{_name}/%{_platform}
%{_appsdir}/%{_name}/AppI*
%{_appsdir}/%{_name}/gtkrc
%{_appsdir}/%{_name}/Help
%dir %{_appsdir}/%{_name}
