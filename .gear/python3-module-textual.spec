%define _unpackaged_files_terminate_build 1

%define modulename textual
%def_with check

# Common directory for documentation.
%define docdir %_docdir/%name-doc-%version

Name: python3-module-%modulename
Version: 0.85.2
Release: alt1

Summary: Textual is a Rapid Application Development framework for Python
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/textual/
Vcs: https://github.com/Textualize/textual.git
BuildArch: noarch
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-poetry

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-rich
BuildRequires: python3-module-markdown
BuildRequires: python3-module-typing_extensions
BuildRequires: python3-module-pytest-asyncio
BuildRequires: python3-module-linkify-it-py
BuildRequires: python3-module-pytest-textual-snapshot
BuildRequires: python3-module-pytest-xdist
%endif

%description
Textual is a Rapid Application Development framework for Python.
Build sophisticated user interfaces with a simple Python API. Run
your apps in the terminal or a web browser!

%package -n %name-doc
Summary: Documentation for Textual
Group: Documentation
Requires: %name

%description -n %name-doc
Documentation for Textual. Textual is a Rapid Application
Development framework for Python. Build sophisticated user
interfaces with a simple Python API.

%prep
%setup
# for windows
rm src/textual/drivers/win32.py

%build
%pyproject_build

%install
%pyproject_install

# test_snapshots needs GUI mode, tested locally
# In test_input_value_visibility broken "value"
# test_textual_env_var assert None is not None
# test_register_language, test_register_language_existing_language,
# test_language_binary_missing no module tree_sitter_languages
# https://github.com/grantjenks/py-tree-sitter-languages
%check
%pyproject_run_pytest -ra -Wignore \
    -ra tests -k "\
    not test_textual_env_var and \
    not test_register_language and \
    not test_register_language_existing_language and \
    not test_language_binary_missing" \
    --ignore="tests/snapshot_tests/test_snapshots.py" \
    --ignore="tests/input/test_input_value_visibility.py"

%files
%python3_sitelibdir/%modulename
%python3_sitelibdir/%modulename-%version.dist-info
%doc README.md LICENSE

%files doc
%doc docs/* examples/

%changelog
* Tue Nov 12 2024 Elena Dyatlenko <lenka@altlinux.org> 0.85.2-alt1
- Updated to upstream version v0.85.2.
- Add blog to doc

* Mon Oct 28 2024 Elena Dyatlenko <lenka@altlinux.org> 0.85.1-alt1
- Updated to upstream version v0.85.1.
- Group change to Development/Python3.
- Url change to pypi.

* Fri Oct 25 2024 Elena Dyatlenko <lenka@altlinux.org> 0.84.0-alt1
- Updated to upstream version v0.84.0.

* Thu Oct 17 2024 Elena Dyatlenko <lenka@altlinux.org> 0.83.0-alt1
- Updated to upstream version v0.83.0.

* Wed Oct 02 2024 Elena Dyatlenko <lenka@altlinux.org> 0.81.0-alt1
- Updated to upstream version v0.81.0.

* Fri Sep 13 2024 Elena Dyatlenko <lenka@altlinux.org> 0.79.1-alt1
- Updated to upstream version v0.79.1.

* Fri Aug 23 2024 Elena Dyatlenko <lenka@altlinux.org> 0.77.0-alt1
- Updated to upstream version v0.77.0.

* Thu Aug 22 2024 Elena Dyatlenko <lenka@altlinux.org> 0.76.0-alt1
- Updated to upstream version v0.76.0.

* Fri Jul 26 2024 Elena Dyatlenko <lenka@altlinux.org> 0.74.0-alt1
- Updated to upstream version v0.74.0.

* Mon Jul 22 2024 Elena Dyatlenko <lenka@altlinux.org> 0.73.0-alt1
- Updated to upstream version v0.73.0.

* Thu Jul 18 2024 Elena Dyatlenko <lenka@altlinux.org> 0.72.0-alt1
- Updated to upstream version v0.72.0.

* Mon Jun 17 2024 Elena Dyatlenko <lenka@altlinux.org> 0.69.0-alt1
- Updated to upstream version v0.69.0.

* Fri Jun 14 2024 Elena Dyatlenko <lenka@altlinux.org> 0.68.0-alt1
- Updated to upstream version v0.68.0.

* Fri Jun 14 2024 Elena Dyatlenko <lenka@altlinux.org> 0.67.0-alt2
- The documentation separate into a package python3-module-textual-doc.

* Tue Jun 11 2024 Elena Dyatlenko <lenka@altlinux.org> 0.67.0-alt1
- Updated to upstream version v0.67.0.

* Mon Jun 03 2024 Elena Dyatlenko <lenka@altlinux.org> 0.64.0-alt1
- Initial build for Sisyphus.
