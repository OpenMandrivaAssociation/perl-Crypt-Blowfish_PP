%define upstream_name    Crypt-Blowfish_PP
%define upstream_version 1.12

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:	Crypt::Blowfish_PP - Blowfish encryption algorithm implemented purely in Perl
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/M/MA/MATTBM/%{upstream_name}-%{upstream_version}.tar.bz2

BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
The Crypt::Blowfish_PP module provides for users to use the Blowfish encryption
algorithm in perl. The implementation is entirely Object Oriented, as there is
quite a lot of context inherent in making blowfish as fast as it is. The key is
anywhere between 64 and 448 bits (8 and 56 bytes), and should be passed as a
packed string. The transformation itself is a 16-round Feistel Network, and
operates on a 64 bit block.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc CHANGELOG README
%{perl_vendorlib}/Crypt/Blowfish_PP.pm
%{_mandir}/*/*
