# windows-setup-tool

## project overview

Helper Project for Windows first installation setup customization.<br>
Aka. `windows_setup_tool`, `Windows Setup Tool`.

## Sponsoring

If you like this project and want to support us, we would be very happy to see you as a sponsor on GitHub ❤️<br>
You can find the `Sponsor` button on the top right of the [GitHub project page](https://github.com/toddeTV/windows-setup-tool).<br>
Thanks a lot for the support <3

## dev

### Required Software

You need Python >v3 with `pip` installed on the system.

### initial project setup

1. execute a `git pull`
2. open project in VSCode
3. Install recommended extensions/ plugins:
   - Open Extensions menu in VSCode (`{Ctrl}+{Shift}+{X}`)
   - type in the search `@recommended`
   - install and enable the plugins
   - see file `.vscode/extensions.json` for configuring some of the extensions
   - Restart or reload VSCode
   - Log In to Plugins that need an account
4. In VSCode on the bottom left click your profile image and log in all services (GitHub due to VSCode extensions, ...)<br>
   If the browser to VSCode callback fails, wait for the login popup on the bottom right to timeout (ca. 5 minutes) and
   then on the upcoming popup question
   `You have not yet finished authorizing [...] Would you like to try a different way? (local server)` click `Yes` and
   use this alternative login mechanic.<br>
   (When you do not want to wait for the timeout to happen, you can also click the `Cancel` to trigger the dialog faster.)
5. Create & enable virtual environment:
   1. `python -m venv .venv`
   2. On Windows: Allow Execution Policy
      1. Check current policys: `Get-ExecutionPolicy -List` (default is `Restricted` or `Undefined`)
      2. Use one:
         1. Only for current terminal session (not recommended): `Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned`
         2. Persisted for the current user (recommended): `Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned`
   3. In VSCode `{Ctrl}+{Shift}+{P}` -> `>Python: Select Interpreter` -> select interpreter `.venv`
   4. In VSCode open terminal. Here the virtual environment will open automatically. (Not recommended, but
      alternativally [manually go into virtual environment](#manually-go-into-virtual-environment).)
      1. Test that you are in the virtual environment: `$env:VIRTUAL_ENV` (should output a path with `.venv` at the end)
   6. All commands from now on following are only for inside the virtual environment!
6. Install the dependencies: `pip install -r requirements.txt`
7. Start the main script: `python main.py`

### manually go into virtual environment

Better use VSCode Terminal that automatically starts inside the virtual environment, but if you need it manually, use this:

```
source .venv/bin/activate    # Linux/macOS
.venv\Scripts\activate.bat   # Windows CMD
.venv\Scripts\Activate.ps1   # Windows PowerShell
```

### 

`git ls-files --eol`

## Attribution/ Contribution

Project founder & head of project:

- [Thorsten Seyschab](https://todde.tv)

Honorable mentions to people that helped this project:

- \[currently none\]

Respectable mentions to projects that helped this project:

- \[currently none\]

Used programs/ softwares, services and dependencies - besides the ones in `./requirements.txt`:

- [GitHub Copilot](https://github.com/features/copilot) was used in private mode for programming questions.

Used assets/ materials including images:

- \[currently none\]

## License

Copyright (c) 2025-present, [Thorsten Seyschab](https://todde.tv)

This project, including original code and assets, is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License ([CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/)). Under this license, others are allowed to remix, adapt, and build upon this work non-commercially, provided they credit the project founder and license any derivative works under the same terms.

Please note that this license applies only to the original content authored by the project’s creators. Third-party libraries, assets, and other materials utilized in this project are listed under "Attribution/ Contribution" above and remain the property of their original creators, licensed under their respective terms.

The project founder reserves the right to modify the terms of this license or to offer different licensing arrangements for specific use cases.

For the full license text, please see the [LICENSE](./LICENSE.md) file.

### Need a Different License?

If you are interested in discussing a different licensing arrangement for individual use cases, please feel free to reach out. Custom licensing may be available, but it is not guaranteed.
