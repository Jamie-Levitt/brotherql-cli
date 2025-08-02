#!/usr/bin/env bash
set -euo pipefail

PKG_ID="com.jamielevitt.myapp"
VERSION="1.0.0"
OUT_PKG="brotherql-cli-installer-${VERSION}.pkg"

# Clean up
rm -f "$OUT_PKG"

# Build flat package including payload (root/) and scripts/
pkgbuild \
  --identifier "$PKG_ID" \
  --version "$VERSION" \
  --scripts "scripts" \
  --root "root" \
  "$OUT_PKG"

echo "→ Built: $OUT_PKG"
