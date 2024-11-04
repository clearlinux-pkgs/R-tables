#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v18
# autospec commit: f35655a
#
Name     : R-tables
Version  : 0.9.31
Release  : 29
URL      : https://cran.r-project.org/src/contrib/tables_0.9.31.tar.gz
Source0  : https://cran.r-project.org/src/contrib/tables_0.9.31.tar.gz
Summary  : Formula-Driven Table Generation
Group    : Development/Tools
License  : GPL-2.0
Requires: R-htmltools
Requires: R-knitr
BuildRequires : R-htmltools
BuildRequires : R-knitr
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Output may be in LaTeX, HTML, plain text, or an R
  matrix for further processing.

%prep
%setup -q -n tables
pushd ..
cp -a tables buildavx2
popd
pushd ..
cp -a tables buildavx512
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1724966133

%install
export SOURCE_DATE_EPOCH=1724966133
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
mkdir -p %{buildroot}-v3/usr/lib64/R/library
mkdir -p %{buildroot}-v4/usr/lib64/R/library
mkdir -p %{buildroot}-va/usr/lib64/R/library

mkdir -p ~/.R
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-v3/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --preclean  --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}-v4/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/R/library/tables/DESCRIPTION
/usr/lib64/R/library/tables/INDEX
/usr/lib64/R/library/tables/Meta/Rd.rds
/usr/lib64/R/library/tables/Meta/features.rds
/usr/lib64/R/library/tables/Meta/hsearch.rds
/usr/lib64/R/library/tables/Meta/links.rds
/usr/lib64/R/library/tables/Meta/nsInfo.rds
/usr/lib64/R/library/tables/Meta/package.rds
/usr/lib64/R/library/tables/Meta/vignette.rds
/usr/lib64/R/library/tables/NAMESPACE
/usr/lib64/R/library/tables/NEWS.md
/usr/lib64/R/library/tables/R/tables
/usr/lib64/R/library/tables/R/tables.rdb
/usr/lib64/R/library/tables/R/tables.rdx
/usr/lib64/R/library/tables/doc/index.html
/usr/lib64/R/library/tables/doc/tables.R
/usr/lib64/R/library/tables/doc/tables.Rnw
/usr/lib64/R/library/tables/doc/tables.pdf
/usr/lib64/R/library/tables/help/AnIndex
/usr/lib64/R/library/tables/help/aliases.rds
/usr/lib64/R/library/tables/help/paths.rds
/usr/lib64/R/library/tables/help/tables.rdb
/usr/lib64/R/library/tables/help/tables.rdx
/usr/lib64/R/library/tables/html/00Index.html
/usr/lib64/R/library/tables/html/R.css
/usr/lib64/R/library/tables/todo.txt
