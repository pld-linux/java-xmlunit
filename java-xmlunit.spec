Summary:	XMLUnit - extend JUnit and NUnit to enable unit testing of XML
Summary(pl):	XMLUnit - rozszerzenie JUnita i NUnita o testowanie jednostkowe XML-a
Name:		xmlunit
Version:	1.0
Release:	1
License:	BSD
Group:		Libraries
Source0:	http://dl.sourceforge.net/xmlunit/%{name}%{version}.zip
# Source0-md5:	4f03206acc9ed18bc6cc23fd38b4fc82
URL:		http://xmlunit.sourceforge.net/
BuildRequires:	ant >= 1.5
BuildRequires:	jaxp_parser_impl
BuildRequires:	jaxp_transform_impl
BuildRequires:	jpackage-utils
BuildRequires:	junit
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	jaxp_parser_impl
Requires:	jaxp_transform_impl
Requires:	junit
BuildArch:	noarch
ExclusiveArch:	i586 i686 pentium3 pentium4 athlon %{x8664} noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XMLUnit extends JUnit and NUnit to enable unit testing of XML. It
compares a control XML document to a test document or the result of a
transformation, validates documents, and compares the results of XPath
expressions.

%description -l pl
XMLUnit rozszerza JUnita i NUnita o mo¿liwo¶æ testowania jednostkowego
XML-a. Porównuje kontrolny dokument XML z dokumentem testowym lub
wynikiem przekszta³cenia, sprawdza poprawno¶æ dokumentów i porównuje
wyniki wyra¿eñ XPath.

%prep
%setup -q -n %{name}

%build
required_jars='jaxp_parser_impl jaxp_transform_impl junit'
export CLASSPATH="$CLASSPATH:`/usr/bin/build-classpath $required_jars`"
export JAVAC=%{javac}
export JAVA=%{java}

%ant

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javadir}

install lib/%{name}%{version}.jar $RPM_BUILD_ROOT%{_javadir}
ln -s       %{name}%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README* *.html *.pdf LICENSE.txt
%{_javadir}/*.jar
