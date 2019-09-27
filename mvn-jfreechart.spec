#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-jfreechart
Version  : 1.0.0
Release  : 1
URL      : https://downloads.sourceforge.net/project/jfreechart/1.%20JFreeChart/1.0.0/jfreechart-1.0.0.tar.gz
Source0  : https://downloads.sourceforge.net/project/jfreechart/1.%20JFreeChart/1.0.0/jfreechart-1.0.0.tar.gz
Source1  : https://repo1.maven.org/maven2/jfreechart/jfreechart/1.0.0/jfreechart-1.0.0.jar
Source2  : https://repo1.maven.org/maven2/jfreechart/jfreechart/1.0.0/jfreechart-1.0.0.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-2.1
Requires: mvn-jfreechart-data = %{version}-%{release}
Requires: mvn-jfreechart-license = %{version}-%{release}
BuildRequires : apache-ant
BuildRequires : buildreq-mvn

%description
*******************************
*  JFREECHART: Version 1.0.0  *
*******************************

%package data
Summary: data components for the mvn-jfreechart package.
Group: Data

%description data
data components for the mvn-jfreechart package.


%package license
Summary: license components for the mvn-jfreechart package.
Group: Default

%description license
license components for the mvn-jfreechart package.


%prep
%setup -q -n jfreechart-1.0.0

%build

%install
mkdir -p %{buildroot}/usr/share/package-licenses/mvn-jfreechart
cp licence-LGPL.txt %{buildroot}/usr/share/package-licenses/mvn-jfreechart/licence-LGPL.txt
mkdir -p %{buildroot}/usr/share/java/.m2/repository/jfreechart/jfreechart/1.0.0
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/jfreechart/jfreechart/1.0.0/jfreechart-1.0.0.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/jfreechart/jfreechart/1.0.0
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/jfreechart/jfreechart/1.0.0/jfreechart-1.0.0.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/jfreechart/jfreechart/1.0.0/jfreechart-1.0.0.jar
/usr/share/java/.m2/repository/jfreechart/jfreechart/1.0.0/jfreechart-1.0.0.pom

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/mvn-jfreechart/licence-LGPL.txt
