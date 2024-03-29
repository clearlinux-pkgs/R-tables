#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
#
Name     : R-tables
Version  : 0.9.17
Release  : 24
URL      : https://cran.r-project.org/src/contrib/tables_0.9.17.tar.gz
Source0  : https://cran.r-project.org/src/contrib/tables_0.9.17.tar.gz
Summary  : Formula-Driven Table Generation
Group    : Development/Tools
License  : GPL-2.0
Requires: R-htmltools
Requires: R-knitr
BuildRequires : R-Hmisc
BuildRequires : R-htmltools
BuildRequires : R-kableExtra
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

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1683148751

%install
export SOURCE_DATE_EPOCH=1683148751
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :


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
/usr/lib64/R/library/tables/doc/HTML.R
/usr/lib64/R/library/tables/doc/HTML.Rmd
/usr/lib64/R/library/tables/doc/HTML.html
/usr/lib64/R/library/tables/doc/index.html
/usr/lib64/R/library/tables/doc/knitrTables.R
/usr/lib64/R/library/tables/doc/knitrTables.Rmd
/usr/lib64/R/library/tables/doc/knitrTables.pdf
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
