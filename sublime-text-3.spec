%global debug_package %{nil}

Name:    sublime-text-3
Summary: Sublime Text 3.
Version: 3114
Release: 1%{?dist}
Source:  http://c758482.r82.cf2.rackcdn.com/sublime_text_3_build_3114_x64.tar.bz2
Patch0:  desktop-icon.patch

Group:   Development/Editors
License: Proprietary
URL:     http://www.sublimetext.com/3

# TODO: Requires isn't right (not sure what it needs)
#Requires:

%description
    Sublime Text is a sophisticated text editor for code, markup and prose.

%prep
%autosetup -n sublime_text_3

%build
cat > subl <<EOF
#!/bin/sh
exec /opt/sublime_text/sublime_text "\$@"
EOF

%install
install -dm755 %{buildroot}/opt/sublime_text
install -m644 -t %{buildroot}/opt/sublime_text \
	changelog.txt \
	python3.3.zip \
	sublime.py \
	sublime_plugin.py
install -m755 -t %{buildroot}/opt/sublime_text \
	crash_reporter \
	plugin_host \
	sublime_text

install -dm755 %{buildroot}/opt/sublime_text/Packages
install -m644 -t %{buildroot}/opt/sublime_text/Packages \
	Packages/*

install -dm755 %{buildroot}/usr/bin
install -m755 -t %{buildroot}/usr/bin \
	subl

for px in 16 32 48 128 256; do
	install -dm755 %{buildroot}/usr/share/icons/hicolor/${px}x${px}/apps
	install -m644 -t %{buildroot}/usr/share/icons/hicolor/${px}x${px}/apps \
		Icon/${px}x${px}/sublime-text.png
	install -dm755 %{buildroot}/opt/sublime_text/Icon/${px}x${px}
	install -m644 -t %{buildroot}/opt/sublime_text/Icon/${px}x${px} \
		Icon/${px}x${px}/sublime-text.png
done;

install -dm755 %{buildroot}/usr/share/applications
install -m644 -t %{buildroot}/usr/share/applications \
	sublime_text.desktop

%files
/opt/sublime_text/*
/usr/bin/subl
/usr/share/applications/sublime_text.desktop
/usr/share/icons/hicolor/*/apps/sublime-text.png
