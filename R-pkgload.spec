#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-pkgload
Version  : 1.2.0
Release  : 23
URL      : https://cran.r-project.org/src/contrib/pkgload_1.2.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/pkgload_1.2.0.tar.gz
Summary  : Simulate Package Installation and Attach
Group    : Development/Tools
License  : GPL-3.0
Requires: R-cli
Requires: R-crayon
Requires: R-desc
Requires: R-pkgbuild
Requires: R-rlang
Requires: R-rprojroot
Requires: R-rstudioapi
Requires: R-withr
BuildRequires : R-cli
BuildRequires : R-crayon
BuildRequires : R-desc
BuildRequires : R-pkgbuild
BuildRequires : R-rlang
BuildRequires : R-rprojroot
BuildRequires : R-rstudioapi
BuildRequires : R-withr
BuildRequires : buildreq-R
Patch1: fix-bootstrap.patch

%description
and then attaching it. This is a key part of the 'devtools' package as it
    allows you to rapidly iterate while developing a package.

%prep
%setup -q -c -n pkgload
cd %{_builddir}/pkgload
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1614098211

%install
export SOURCE_DATE_EPOCH=1614098211
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
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library pkgload
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library pkgload
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library pkgload
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc pkgload || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/pkgload/DESCRIPTION
/usr/lib64/R/library/pkgload/INDEX
/usr/lib64/R/library/pkgload/Meta/Rd.rds
/usr/lib64/R/library/pkgload/Meta/features.rds
/usr/lib64/R/library/pkgload/Meta/hsearch.rds
/usr/lib64/R/library/pkgload/Meta/links.rds
/usr/lib64/R/library/pkgload/Meta/nsInfo.rds
/usr/lib64/R/library/pkgload/Meta/package.rds
/usr/lib64/R/library/pkgload/NAMESPACE
/usr/lib64/R/library/pkgload/NEWS.md
/usr/lib64/R/library/pkgload/R/pkgload
/usr/lib64/R/library/pkgload/R/pkgload.rdb
/usr/lib64/R/library/pkgload/R/pkgload.rdx
/usr/lib64/R/library/pkgload/WORDLIST
/usr/lib64/R/library/pkgload/help/AnIndex
/usr/lib64/R/library/pkgload/help/aliases.rds
/usr/lib64/R/library/pkgload/help/paths.rds
/usr/lib64/R/library/pkgload/help/pkgload.rdb
/usr/lib64/R/library/pkgload/help/pkgload.rdx
/usr/lib64/R/library/pkgload/html/00Index.html
/usr/lib64/R/library/pkgload/html/R.css
/usr/lib64/R/library/pkgload/tests/testthat.R
/usr/lib64/R/library/pkgload/tests/testthat/test-data.r
/usr/lib64/R/library/pkgload/tests/testthat/test-depend.r
/usr/lib64/R/library/pkgload/tests/testthat/test-description.r
/usr/lib64/R/library/pkgload/tests/testthat/test-dll.r
/usr/lib64/R/library/pkgload/tests/testthat/test-examples.R
/usr/lib64/R/library/pkgload/tests/testthat/test-examples.Rd
/usr/lib64/R/library/pkgload/tests/testthat/test-extraction.R
/usr/lib64/R/library/pkgload/tests/testthat/test-help.r
/usr/lib64/R/library/pkgload/tests/testthat/test-imports.r
/usr/lib64/R/library/pkgload/tests/testthat/test-load-collate.r
/usr/lib64/R/library/pkgload/tests/testthat/test-load-hooks.r
/usr/lib64/R/library/pkgload/tests/testthat/test-load.r
/usr/lib64/R/library/pkgload/tests/testthat/test-metadata.r
/usr/lib64/R/library/pkgload/tests/testthat/test-namespace.r
/usr/lib64/R/library/pkgload/tests/testthat/test-package.R
/usr/lib64/R/library/pkgload/tests/testthat/test-s4-export.r
/usr/lib64/R/library/pkgload/tests/testthat/test-s4-sort.r
/usr/lib64/R/library/pkgload/tests/testthat/test-s4-unload.r
/usr/lib64/R/library/pkgload/tests/testthat/test-shim.r
/usr/lib64/R/library/pkgload/tests/testthat/testCollateAbsent/DESCRIPTION
/usr/lib64/R/library/pkgload/tests/testthat/testCollateAbsent/R/a.r
/usr/lib64/R/library/pkgload/tests/testthat/testCollateAbsent/R/b.r
/usr/lib64/R/library/pkgload/tests/testthat/testCollateAbsent/R/c.r
/usr/lib64/R/library/pkgload/tests/testthat/testCollateExtra/DESCRIPTION
/usr/lib64/R/library/pkgload/tests/testthat/testCollateExtra/R/a.r
/usr/lib64/R/library/pkgload/tests/testthat/testCollateMissing/DESCRIPTION
/usr/lib64/R/library/pkgload/tests/testthat/testCollateMissing/R/a.r
/usr/lib64/R/library/pkgload/tests/testthat/testCollateMissing/R/b.r
/usr/lib64/R/library/pkgload/tests/testthat/testCollateOrder/DESCRIPTION
/usr/lib64/R/library/pkgload/tests/testthat/testCollateOrder/NAMESPACE
/usr/lib64/R/library/pkgload/tests/testthat/testCollateOrder/R/a.r
/usr/lib64/R/library/pkgload/tests/testthat/testCollateOrder/R/b.r
/usr/lib64/R/library/pkgload/tests/testthat/testData/DESCRIPTION
/usr/lib64/R/library/pkgload/tests/testthat/testData/NAMESPACE
/usr/lib64/R/library/pkgload/tests/testthat/testData/R/sysdata.rda
/usr/lib64/R/library/pkgload/tests/testthat/testData/data/a.rda
/usr/lib64/R/library/pkgload/tests/testthat/testData/data/b.r
/usr/lib64/R/library/pkgload/tests/testthat/testDataLazy/DESCRIPTION
/usr/lib64/R/library/pkgload/tests/testthat/testDataLazy/NAMESPACE
/usr/lib64/R/library/pkgload/tests/testthat/testDataLazy/R/sysdata.rda
/usr/lib64/R/library/pkgload/tests/testthat/testDataLazy/data/a.rda
/usr/lib64/R/library/pkgload/tests/testthat/testDataLazy/data/b.r
/usr/lib64/R/library/pkgload/tests/testthat/testDependMissing/DESCRIPTION
/usr/lib64/R/library/pkgload/tests/testthat/testDependMissing/R/a.r
/usr/lib64/R/library/pkgload/tests/testthat/testDependsExists/DESCRIPTION
/usr/lib64/R/library/pkgload/tests/testthat/testDllLoad/DESCRIPTION
/usr/lib64/R/library/pkgload/tests/testthat/testDllLoad/NAMESPACE
/usr/lib64/R/library/pkgload/tests/testthat/testDllLoad/R/a.r
/usr/lib64/R/library/pkgload/tests/testthat/testDllLoad/src/null-test.c
/usr/lib64/R/library/pkgload/tests/testthat/testDllRcpp/DESCRIPTION
/usr/lib64/R/library/pkgload/tests/testthat/testDllRcpp/NAMESPACE
/usr/lib64/R/library/pkgload/tests/testthat/testDllRcpp/R/RcppExports.R
/usr/lib64/R/library/pkgload/tests/testthat/testDllRcpp/src/RcppExports.cpp
/usr/lib64/R/library/pkgload/tests/testthat/testDllRcpp/src/rcpp_hello_world.cpp
/usr/lib64/R/library/pkgload/tests/testthat/testHelp/DESCRIPTION
/usr/lib64/R/library/pkgload/tests/testthat/testHelp/NAMESPACE
/usr/lib64/R/library/pkgload/tests/testthat/testHelp/R/foofoo.r
/usr/lib64/R/library/pkgload/tests/testthat/testHelp/man/foofoo.Rd
/usr/lib64/R/library/pkgload/tests/testthat/testHelp/man/macros/macros.Rd
/usr/lib64/R/library/pkgload/tests/testthat/testHelp/man/testCustomMacro.Rd
/usr/lib64/R/library/pkgload/tests/testthat/testHelp/man/testHelp-package.Rd
/usr/lib64/R/library/pkgload/tests/testthat/testHelp/man/testHelp.Rd
/usr/lib64/R/library/pkgload/tests/testthat/testHelp/man/testSysMacro.Rd
/usr/lib64/R/library/pkgload/tests/testthat/testHooks/DESCRIPTION
/usr/lib64/R/library/pkgload/tests/testthat/testHooks/R/a.r
/usr/lib64/R/library/pkgload/tests/testthat/testImportMissing/DESCRIPTION
/usr/lib64/R/library/pkgload/tests/testthat/testImportMissing/R/a.r
/usr/lib64/R/library/pkgload/tests/testthat/testImportVersion/DESCRIPTION
/usr/lib64/R/library/pkgload/tests/testthat/testImportVersion/NAMESPACE
/usr/lib64/R/library/pkgload/tests/testthat/testImportVersion/R/a.r
/usr/lib64/R/library/pkgload/tests/testthat/testImportVersion/R/b.r
/usr/lib64/R/library/pkgload/tests/testthat/testLoadDir/DESCRIPTION
/usr/lib64/R/library/pkgload/tests/testthat/testLoadDir/R/a.r
/usr/lib64/R/library/pkgload/tests/testthat/testLoadHelpers/DESCRIPTION
/usr/lib64/R/library/pkgload/tests/testthat/testLoadHelpers/NAMESPACE
/usr/lib64/R/library/pkgload/tests/testthat/testLoadHelpers/R/a.r
/usr/lib64/R/library/pkgload/tests/testthat/testLoadHelpers/data/mtcars2.rda
/usr/lib64/R/library/pkgload/tests/testthat/testLoadHelpers/tests/testthat.R
/usr/lib64/R/library/pkgload/tests/testthat/testLoadHelpers/tests/testthat/helpers.R
/usr/lib64/R/library/pkgload/tests/testthat/testLoadHelpers/tests/testthat/test-foo.R
/usr/lib64/R/library/pkgload/tests/testthat/testLoadHooks/DESCRIPTION
/usr/lib64/R/library/pkgload/tests/testthat/testLoadHooks/R/a.r
/usr/lib64/R/library/pkgload/tests/testthat/testLoadLazy/DESCRIPTION
/usr/lib64/R/library/pkgload/tests/testthat/testLoadLazy/NAMESPACE
/usr/lib64/R/library/pkgload/tests/testthat/testLoadLazy/R/bindings.r
/usr/lib64/R/library/pkgload/tests/testthat/testMissingNsObject/DESCRIPTION
/usr/lib64/R/library/pkgload/tests/testthat/testMissingNsObject/NAMESPACE
/usr/lib64/R/library/pkgload/tests/testthat/testMissingNsObject/R/a.r
/usr/lib64/R/library/pkgload/tests/testthat/testNamespace/DESCRIPTION
/usr/lib64/R/library/pkgload/tests/testthat/testNamespace/NAMESPACE
/usr/lib64/R/library/pkgload/tests/testthat/testNamespace/R/a.r
/usr/lib64/R/library/pkgload/tests/testthat/testNamespace/R/b.r
/usr/lib64/R/library/pkgload/tests/testthat/testS3removed/DESCRIPTION
/usr/lib64/R/library/pkgload/tests/testthat/testS3removed/NAMESPACE
/usr/lib64/R/library/pkgload/tests/testthat/testS3removed/R/S3.r
/usr/lib64/R/library/pkgload/tests/testthat/testS3removed2/DESCRIPTION
/usr/lib64/R/library/pkgload/tests/testthat/testS3removed2/NAMESPACE
/usr/lib64/R/library/pkgload/tests/testthat/testS3removed2/R/S3.r
/usr/lib64/R/library/pkgload/tests/testthat/testS4export/DESCRIPTION
/usr/lib64/R/library/pkgload/tests/testthat/testS4export/NAMESPACE
/usr/lib64/R/library/pkgload/tests/testthat/testS4export/R/all.r
/usr/lib64/R/library/pkgload/tests/testthat/testS4import/DESCRIPTION
/usr/lib64/R/library/pkgload/tests/testthat/testS4import/NAMESPACE
/usr/lib64/R/library/pkgload/tests/testthat/testS4import/R/all.r
/usr/lib64/R/library/pkgload/tests/testthat/testS4sort/DESCRIPTION
/usr/lib64/R/library/pkgload/tests/testthat/testS4sort/NAMESPACE
/usr/lib64/R/library/pkgload/tests/testthat/testS4sort/R/classes.r
/usr/lib64/R/library/pkgload/tests/testthat/testS4union/DESCRIPTION
/usr/lib64/R/library/pkgload/tests/testthat/testS4union/NAMESPACE
/usr/lib64/R/library/pkgload/tests/testthat/testS4union/R/classes.r
/usr/lib64/R/library/pkgload/tests/testthat/testShim/A.txt
/usr/lib64/R/library/pkgload/tests/testthat/testShim/C.txt
/usr/lib64/R/library/pkgload/tests/testthat/testShim/DESCRIPTION
/usr/lib64/R/library/pkgload/tests/testthat/testShim/NAMESPACE
/usr/lib64/R/library/pkgload/tests/testthat/testShim/R/a.r
/usr/lib64/R/library/pkgload/tests/testthat/testShim/inst/A.txt
/usr/lib64/R/library/pkgload/tests/testthat/testShim/inst/B.txt
