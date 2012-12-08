%define upstream_name    Crypt-Blowfish_PP
%define upstream_version 1.12

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Crypt::Blowfish_PP - Blowfish encryption algorithm implemented purely in Perl
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/M/MA/MATTBM/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildArch:	noarch

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
%__perl Makefile.PL INSTALLDIRS=vendor
%make
make test

%install
%makeinstall_std

%files
%doc CHANGELOG README
%{perl_vendorlib}/Crypt/Blowfish_PP.pm
%{_mandir}/*/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 1.120.0-4mdv2012.0
+ Revision: 765119
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 1.120.0-3
+ Revision: 763616
- rebuilt for perl-5.14.x

* Sat May 21 2011 Oden Eriksson <oeriksson@mandriva.com> 1.120.0-2
+ Revision: 676843
- rebuild

* Sat Aug 01 2009 Jérôme Quelin <jquelin@mandriva.org> 1.120.0-1mdv2011.0
+ Revision: 405853
- rebuild using %%perl_convert_version

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 1.12-4mdv2009.0
+ Revision: 241194
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.12-2mdv2008.0
+ Revision: 86237
- rebuild


* Wed Sep 13 2006 Oden Eriksson <oeriksson@mandriva.com> 1.12-1mdv2007.0
- rebuild

* Fri Jul 15 2005 Oden Eriksson <oeriksson@mandriva.com> 1.12-1mdk
- initial Mandriva package

