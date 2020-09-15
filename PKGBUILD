# Maintainer: Frede Braendstrup <frederikbraendstrup@gmail.com>

pkgname=cmake-list-packages
pkgver=0.1.0
pkgrel=1
pkgdesc="List all installed cmake modules that can be used with find_package"
arch=('x86_64')
depends=('python' 'cmake')
url="https://github.com/FredeEB/cmake-list-packages"
source=("$_pkgname::git+https://github.com/FredeEB/cmake-list-packages.git")
md5sums=('SKIP')

pkgver() {
  cd "$_pkgname"
  printf "%s" "$(git describe --long | sed 's/\([^-]*-\)g/r\1/;s/-/./g')"
}

package() {
  cd "$_pkgname"
  install -Dm 755 cmake-list-packages.py -t "${pkgdir}/usr/bin"
}