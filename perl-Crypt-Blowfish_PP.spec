%define modname	Crypt-Blowfish_PP
%define modver	1.12

Summary:	Crypt::Blowfish_PP - Blowfish encryption algorithm implemented purely in Perl
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	12
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://search.cpan.org/CPAN/authors/id/M/MA/MATTBM/%{modname}-%{modver}.tar.bz2
BuildArch:	noarch
BuildRequires:	perl-devel

%description
The Crypt::Blowfish_PP module provides for users to use the Blowfish encryption
algorithm in perl. The implementation is entirely Object Oriented, as there is
quite a lot of context inherent in making blowfish as fast as it is. The key is
anywhere between 64 and 448 bits (8 and 56 bytes), and should be passed as a
packed string. The transformation itself is a 16-round Feistel Network, and
operates on a 64 bit block.

%prep
%setup -qn %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc CHANGELOG README
%{perl_vendorlib}/Crypt/Blowfish_PP.pm
%{_mandir}/man3/*

