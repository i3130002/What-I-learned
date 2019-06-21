# Add-a-custom-template-to-windows-explorer-new-context-menu

From http://www.drewchapin.com/tutorials/add-a-custom-template-to-windows-explorer-new-context-menu/

#### To have a plain file use :

```Windows Registery
Windows Registry Editor Version 5.00
[HKEY_CLASSES_ROOT\.hta\ShellNew]
"NullFile"=""
```

#### Otherwise to create a template use :

```Windows registery
Windows Registry Editor Version 5.00
[HKEY_CLASSES_ROOT\.hta\ShellNew]
"FileName"="Template.hta"
```

1. Create a file with the same name, `Template.hta` with your custom content. You can check out my [HTML Application Gist](https://gist.github.com/drewchapin/df20f952df566be7978265d176f39bc8) if you want to know what I used.
2. Save the `Template.hta` file to `C:\Windows\ShellNew`.



You also can use my .reg file for easy  access named "plain file creator.reg" placed in the same directory as this file.