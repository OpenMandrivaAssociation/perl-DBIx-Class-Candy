%define upstream_name    DBIx-Class-Candy
%define upstream_version 0.001004

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Create sugar for your favorite ORM, DBIx::Class
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/DBIx/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(DBIx::Class)
BuildRequires: perl(MRO::Compat)
BuildRequires: perl(Sub::Exporter)
BuildRequires: perl(Test::More)
BuildRequires: perl(namespace::clean)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes LICENSE README META.json
%{_mandir}/man3/*
%perl_vendorlib/*


