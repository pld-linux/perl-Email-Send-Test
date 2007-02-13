#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Email
%define	pnam	Send-Test
Summary:	Email::Send::Test - captures emails sent via Email::Send for testing
Summary(pl.UTF-8):	Email::Send::Test - przechwytuje dla testu wiadomości wysyłane za pomocą Email::Send
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

%description -l pl.UTF-8
Email::Send::Test to moduł do testowania aplikacji używających modułu
Email::Send do wysyłania poczty elektronicznej. W szczególności
zakłada, że w użyciu jest jakiś rodzaj pliku konfiguracyjnego do
podania "kanału" przekazywania listów albo coś podobnego, co można
łatwo przykryć albo zmienić w skrypcie testowym.

Email::Send::Test to po prostu pułapka. Kiedy listy przychodzą, są
umieszczane w tablicy w nietkniętej postaci. W przypadku wysłania
jednego listu w pułapce będzie jeden. W przypadku wysłania 20, będzie
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
