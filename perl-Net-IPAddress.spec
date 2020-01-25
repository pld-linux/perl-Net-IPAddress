#
# Conditional build:
%bcond_without	tests		# do not perform "make test"

%define		pdir	Net
%define		pnam	IPAddress
Summary:	Net::IPAddress - Functions used to manipulate IP addresses, masks and FQDN's
Name:		perl-Net-IPAddress
Version:	1.10
Release:	1
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/S/SA/SARENNER/Net-IPAddress-%{version}.tar.gz
# Source0-md5:	512117d3f6bcc027bd11f70d71f6f844
URL:		http://search.cpan.org/dist/Net-IPAddress/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Net::IPAddr is a collection of helpful functions used to convert IP
addresses to/from 32-bit integers, applying subnet masks to IP
addresses, validating IP address strings, and splitting a FQDN into
its host and domain parts.

No rocket science here, but I have found these functions to very, very
handy. For example, have you ever tried to sort a list of IP addresses
only to find out that they don't sort the way you expected? Here is
the solution! If you convert the IP addresses to 32-bit integer
addresses, they will sort in correct order.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Net/IPAddress.pm
%{_mandir}/man3/*
