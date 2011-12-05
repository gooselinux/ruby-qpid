Name:           ruby-qpid
Version: 	0.7.946106
Release:        2%{?dist}
Summary:        Ruby language client for AMQP

Group:          Development/Ruby
License:        ASL 2.0
URL:            http://qpid.apache.org/
Source0:        %{name}-%{version}.tar.gz
# svn export http://svn.apache.org/repos/asf/incubator/qpid/trunk/qpid/ruby \
#  ruby-qpid
# tar czf ruby-qpid.tar.gz ruby-qpid
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%{!?ruby_sitelib: %define ruby_sitelib %(ruby -rrbconfig  -e 'puts Config::CONFIG["sitelibdir"]')}
%{!?ruby_sitearch: %define ruby_sitearch %(ruby -rrbconfig -e 'puts Config::CONFIG["sitearchdir"]')}

%define debug_package %{nil}

#BuildArch:      noarch

BuildRequires:  ruby
BuildRequires:  ruby-devel
BuildRequires:	rubygem-rake
BuildRequires:	cyrus-sasl-devel

Requires:       ruby
Requires:       ruby(abi) = 1.8
Requires:	cyrus-sasl

Provides:       ruby(qpid) = %{version}

%description
The Apache Qpid project's Ruby language client for AMQP.

%prep
%setup -q -n %{name}-%{version}

%build
rake build

%install
rm -rf $RPM_BUILD_ROOT
install -dm 755 $RPM_BUILD_ROOT%{ruby_sitelib}/qpid
install -pm 644 lib/qpid/*.rb $RPM_BUILD_ROOT%{ruby_sitelib}/qpid
install -dm 755 $RPM_BUILD_ROOT%{ruby_sitearch}
install -dm 755 $RPM_BUILD_ROOT%{ruby_sitelib}/qpid/spec_cache
install -pm 644 lib/qpid/spec_cache/*.rb_marshal $RPM_BUILD_ROOT%{ruby_sitelib}/qpid/spec_cache
install -dm 755 %{buildroot}%{ruby_sitelib}/qpid/specs
install -pm 644 lib/qpid/specs/*.xml %{buildroot}%{ruby_sitelib}/qpid/specs
install -pm 644 lib/qpid.rb $RPM_BUILD_ROOT%{ruby_sitelib}
install -pm 755 ext/sasl/sasl.so $RPM_BUILD_ROOT%{ruby_sitearch}
# to quiet rpmlint warning
chmod -x LICENSE.txt
rm -fr specs

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{ruby_sitelib}/qpid
%{ruby_sitelib}/qpid.rb
%{ruby_sitearch}/sasl.so
%doc LICENSE.txt NOTICE.txt RELEASE_NOTES

%changelog
* Thu Jun  3 2010 Nuno Santos <nsantos@redhat.com> - 0.7.946106-2
- Resolves: rhbz599685

* Wed May 19 2010 Nuno Santos <nsantos@redhat.com> - 0.7.946106-1
- Rebased to svn rev 946106
- Related: rhbz574881

* Tue Sep 29 2009 Nuno Santos <nsantos@redhat.com> - 0.5.819819-1
- Rebased to svn rev 819819 for F12 beta

* Fri Sep 25 2009 Nuno Santos <nsantos@redhat.com> - 0.5.818599-1
- Rebased to svn rev 818599

* Fri Sep 18 2009 Nuno Santos <nsantos@redhat.com> - 0.5.816781-1
- Rebased to svn rev 816781

* Tue Jul 28 2009 Nuno Santos <nsantos@redhat.com> - 0.5.795209-1
- Rebased to svn rev 795209

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.791584-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jul  6 2009 Nuno Santos <nsantos@redhat.com> - 0.5.791584-1
- Rebased to svn rev 791584

* Thu Jul  2 2009 Nuno Santos <nsantos@redhat.com> - 0.5.790661-1
- Rebased to svn rev 790661

* Mon Jun 22 2009 Nuno Santos <nsantos@redhat.com> - 0.5.787286-1
- Rebased to svn rev 787286

* Wed May 20 2009 Nuno Santos <nsantos@redhat.com> - 0.5.776856-1
- Rebased to svn rev 776856

* Mon May  4 2009 Nuno Santos <nsantos@redhat.com> - 0.5.752600-2
- patch for SASL credentials refresh

* Thu Mar 19 2009 Nuno Santos <nsantos@redhat.com> - 0.5.752600-1
- Rebased to svn rev 752600

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.738618-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Feb  5 2009 Nuno Santos <nsantos@redhat.com> - 0.4.738618-2
- Install SASL support extension

* Thu Jan 29 2009 Nuno Santos <nsantos@redhat.com> - 0.4.738618-1
- Rebased to svn rev 738618

* Wed Dec 10 2008 Andrew Stitcher <astitcher@redhat.com> - 0.3.725356-1
- Updated spec file to work with RHEL 4 and earlier Fedora versions

* Mon Dec  1 2008 Andrew Stitcher <astitcher@redhat.com> - 0.3.722126-1
- Changed version numbering to fit other qpid packages
- Added release notes to doc directory

* Fri Nov 14 2008 Rafael Schloming <rafaels@redhat.com> - 0.2-1
- Updated to work with qpid M4.

* Wed Sep  3 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.1-2
- fix license tag

* Thu Mar 22 2007 Rafael Schloming <rafaels@redhat.com> - 0.1-1
- Initial build
- Comply with Fedora packaging guidelines
