%define upstream_name    DBIx-Class-Candy
%define upstream_version 0.002000

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Create sugar for your favorite ORM, DBIx::Class
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/DBIx/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(DBIx::Class)
BuildRequires:	perl(Lingua::EN::Inflect)
BuildRequires:	perl(Module::Find)
BuildRequires:	perl(MRO::Compat)
BuildRequires:	perl(String::CamelCase)
BuildRequires:	perl(Sub::Exporter)
BuildRequires:	perl(Test::Deep)
BuildRequires:	perl(Test::More) >= 0.960.0
BuildRequires:	perl(namespace::clean)
BuildArch:	noarch

%description
'DBIx::Class::Candy' is a simple sugar layer for definition of the
DBIx::Class manpage results. Note that it may later be expanded to add
sugar for more 'DBIx::Class' related things. By default
'DBIx::Class::Candy':

* *

  turns on strict and warnings

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes LICENSE README META.json
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.2.0-2mdv2011.0
+ Revision: 657401
- rebuild for updated spec-helper

* Sun Mar 13 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.2.0-1
+ Revision: 644408
- update to new version 0.002000

* Sun Dec 26 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.1.5-1mdv2011.0
+ Revision: 625269
- update to new version 0.001005

* Sat Dec 25 2010 Shlomi Fish <shlomif@mandriva.org> 0.1.4-1mdv2011.0
+ Revision: 624955
- import perl-DBIx-Class-Candy

