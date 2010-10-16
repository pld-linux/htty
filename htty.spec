Summary:	htty is a console application for interacting with HTTP servers
Name:		htty
Version:	1.1.4
Release:	1
License:	MIT
Source0:	http://rubygems.org/downloads/%{name}-%{version}.gem
# Source0-md5:	10168b89e51a4a06a822124b405f73c4
Patch0:		%{name}-paths.patch
Group:		Applications/Console
URL:		http://htty.github.com/
BuildRequires:	rpmbuild(macros) >= 1.484
BuildRequires:	ruby >= 1:1.8.7
BuildRequires:	ruby-modules
%{?ruby_mod_ver_requires_eq}
#BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# nothing to be placed there. we're not noarch only because of ruby packaging
%define		_enable_debug_packages	0

%description
htty is a console application for interacting with HTTP servers. It’s
something of a cross between curl and the Lynx browser.

%package rdoc
Summary:	HTML documentation for %{name}
Summary(pl.UTF-8):	Dokumentacja w formacie HTML dla %{name}
Group:		Documentation
Requires:	ruby >= 1:1.8.7-4

%description rdoc
HTML documentation for %{name}.

%description rdoc -l pl.UTF-8
Dokumentacja w formacie HTML dla %{name}.

%package ri
Summary:	ri documentation for %{name}
Summary(pl.UTF-8):	Dokumentacja w formacie ri dla %{name}
Group:		Documentation
Requires:	ruby

%description ri
ri documentation for %{name}.

%description ri -l pl.UTF-8
Dokumentacji w formacie ri dla %{name}.

%prep
%setup -q -c
%{__tar} xf %{SOURCE0} -O data.tar.gz | %{__tar} xz
find -newer README.markdown -o -print | xargs touch --reference %{SOURCE0}

%patch0 -p0

%build
rdoc --ri --op ri lib
rdoc --op rdoc lib
rm ri/created.rid

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_rubylibdir},%{ruby_ridir},%{ruby_rdocdir},%{_bindir}}
install bin/htty $RPM_BUILD_ROOT%{_bindir}

cp -a lib/* $RPM_BUILD_ROOT%{ruby_rubylibdir}
cp -a ri/* $RPM_BUILD_ROOT%{ruby_ridir}
cp -a rdoc $RPM_BUILD_ROOT%{ruby_rdocdir}/%{name}-%{version}
cp -a VERSION $RPM_BUILD_ROOT%{ruby_rubylibdir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.markdown MIT-LICENSE.markdown History.markdown
%attr(755,root,root) %{_bindir}/htty
%{ruby_rubylibdir}/%{name}.rb
%{ruby_rubylibdir}/%{name}

%files rdoc
%defattr(644,root,root,755)
%{ruby_rdocdir}/%{name}-%{version}

%files ri
%defattr(644,root,root,755)
%{ruby_ridir}/HTTY
