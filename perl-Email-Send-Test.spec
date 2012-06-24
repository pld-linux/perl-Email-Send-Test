#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Email
%define	pnam	Send-Test
Summary:	Email::Send::Test - captures emails sent via Email::Send for testing
Summary(pl):	Email::Send::Test - przechwytuje dla testu wiadomo�ci wysy�ane za pomoc� Email::Send
Name:		perl-Email-Send-Test
Version:	0.02
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	e7b1ff3a5740fe3b61bb3ae30337f90d
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-ExtUtils-MakeMaker >= 6.24-2
%if %{with tests}
BuildRequires:	perl-Email-Send >= 1.42
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Email::Send::Test is a module for testing applications that use
Email::Send to send email. In particular, it kind of assumes that you
use some sort of configuration file to specify the "channel" to
dispatch mail to, or something else that can be easily overloaded or
altered in the test script.

Email::Send::Test is simple a trap. As emails come in, it just puts
them onto an array totally intact as it was given them. If you send
one email, there will be one in the trap. If you send 20, there will
be 20, and so on.

%description -l pl
Email::Send::Test to modu� do testowania aplikacji u�ywaj�cych modu�u
Email::Send do wysy�ania poczty elektronicznej. W szczeg�lno�ci
zak�ada, �e w u�yciu jest jaki� rodzaj pliku konfiguracyjnego do
podania "kana�u" przekazywania list�w albo co� podobnego, co mo�na
�atwo przykry� albo zmieni� w skrypcie testowym.

Email::Send::Test to po prostu pu�apka. Kiedy listy przychodz�, s�
umieszczane w tablicy w nietkni�tej postaci. W przypadku wys�ania
jednego listu w pu�apce b�dzie jeden. W przypadku wys�ania 20, b�dzie
20 i tak dalej.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} -MExtUtils::MakeMaker -e 'WriteMakefile(NAME=>"Email::Send::Test")' \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/Email/Send/*.pm
%{_mandir}/man3/*
