Name:           ooreduce
Version:        0.1.0
Release:        1%{?dist}
Summary:        Aggregates stream records into sums, averages, histograms, and groupings.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/ooreduce
Source0:        ooreduce-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
ooreduce is a sovereign, capability-bounded STREAM ACCUMULATE written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/ooreduce
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/ooreduce-uninstall

%files
/usr/bin/ooreduce
/usr/bin/ooreduce-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.1.0-1
- Initial sovereign blueprint scaffolding
