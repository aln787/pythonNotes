## Additional notes

### iOS tools
- A-Shell - iOS application to get a command line, allows you to execute python and bash commands locally
  - [iOS-System](200~https://github.com/holzschu/ios_system#adding-more-commands) - Tools that enable the bash like terminal on iOS
- [Carnets](https://github.com/holzschu/Carnets) - A standalone Jupyter notebooks implementation for iOS. This is an additional tool from Nicholas Holzschuch ([holzschu](https://github.com/holzschu)
- Working Copy - Enables you to clone repositories from git, can be used with A-Shell copying files between 
- LibTerm - Additional iOS command line application with some additional features over A-shell
  - Note: A-Shell doesn't have an exit key and on iOS no ctrl key exists in the  keyboard. As a hack was able to run curl -X POST to a running service in A-Shell to stop the program execution.

### Python

#### Testing
- python3 -m "nose"

#### Doc String / Details
- help(<module name>)
- <module name>.<function>.__doc__
- Get functions
   ```
   import inspect
   import <module_to_inspect> as module
   functions = inspect.getmembers(module, inspect.isfunction)
   ```
   - [Additional Options](https://stackoverflow.com/questions/139180/how-to-list-all-functions-in-a-python-module)

#### Builtins
```
>>> import builtins
>>> dir(builtins)
```
