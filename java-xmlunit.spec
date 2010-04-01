# TODO
# - docs are broken. html docs seem to be incompatibile with our
#   docbook-style-xsl. Does it require earlier version? pdf docs require
#   dblatex command. I have no idea what it is and what should provide it.

%bcond_with	doc		# build docs. Does not work.

%if "%{pld_release}" == "ti"
%bcond_without	java_sun	# build with gcj
%else
%bcond_with	java_sun	# build with java-sun
%endif
#
%include	/usr/lib/rpm/macros.java

%define		srcname	xmlunit
Summary:	XMLUnit - extend JUnit and NUnit to enable unit testing of XML
Summary(pl.UTF-8):	XMLUnit - rozszerzenie JUnita i NUnita o testowanie jednostkowe XML-a
Name:		java-xmlunit
Version:	1.3
Release:	1
License:	BSD
Group:		Libraries
Source0:	http://downloads.sourceforge.net/project/xmlunit/xmlunit%20for%20Java/XMLUnit%20for%20Java%201.3/xmlunit-%{version}-src.zip
# Source0-md5:	8b23f360367f18f393559dc2f0640dbe
URL:		http://xmlunit.sourceforge.net/
BuildRequires:	ant >= 1.5
BuildRequires:	ant-junit
%{!?with_java_sun:BuildRequires:	java-gcj-compat-devel}
%{?with_java_sun:BuildRequires:	java-sun}
BuildRequires:	jaxp_parser_impl
BuildRequires:	jaxp_transform_impl
BuildRequires:	jpackage-utils
BuildRequires:	junit
BuildRequires:	rpm >= 4.4.9-56
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	jaxp_parser_impl
Requires:	jaxp_transform_impl
Requires:	junit
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XMLUnit extends JUnit to enable unit testing of XML. It compares a
control XML document to a test document or the result of a
transformation, validates documents, and compares the results of XPath
expressions.

%description -l pl.UTF-8
XMLUnit rozszerza JUnit o możliwość testowania jednostkowego XML-a.
Porównuje kontrolny dokument XML z dokumentem testowym lub wynikiem
przekształcenia, sprawdza poprawność dokumentów i porównuje wyniki
wyrażeń XPath.

%package javadoc
Summary:	Online manual for %{name}
Summary(pl.UTF-8):	Dokumentacja online do %{name}
Group:		Documentation
Requires:	jpackage-utils

%description javadoc
Documentation for %{name}.

%description javadoc -l pl.UTF-8
Dokumentacja do %{name}.

%description javadoc -l fr.UTF-8
Javadoc pour %{name}.

%prep
%setup -q -n %{srcname}-%{version}

%build
required_jars='jaxp_parser_impl jaxp_transform_impl junit'
CLASSPATH="$CLASSPATH:$(%{_bindir}/build-classpath $required_jars)"
export JAVAC=%{javac}
export JAVA=%{java}

%ant %{?with_doc:users-guide-html} %{?with_doc:users-guide-pdf} javadocs test jar

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javadir}

install build/lib/%{srcname}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{srcname}-%{version}.jar
ln -s %{srcname}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{srcname}.jar

# javadoc
%if %{with javadoc}
install -d $RPM_BUILD_ROOT%{_javadocdir}/%{srcname}-%{version}
cp -a dist/docs/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{srcname}-%{version}
ln -s %{srcname}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{srcname} # ghost symlink
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post javadoc
ln -nfs %{srcname}-%{version} %{_javadocdir}/%{srcname}

%files
%defattr(644,root,root,755)
%doc README* LICENSE.txt
%{_javadir}/*.jar

%if %{with javadoc}
%files javadoc
%defattr(644,root,root,755)
%{_javadocdir}/%{srcname}-%{version}
%ghost %{_javadocdir}/%{srcname}
%endif
