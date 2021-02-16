# Mod Item and Block importer
This is a simple way to add a custom item or block without requiring the knowledge of how to code. It also makes it simpler to add items and blocks and reduce user error.
## Pre-Requirements:
Python 3.x (Tested on 3.9.1) <br>
official python download link: https://www.python.org/downloads/ <br>

GitHub: latest recommended <br>
official github downland link: https://desktop.github.com/ <br>
GitHub CLI is also supported <br>

Git must also be installed on the system you can type `where git` in the command line to see if Git is installed.
## Error Reporting
<b>please follow the error reporting guidelines found in the project root README</b>

## How to use the importer
### Start
To run the importer run the start.py script found in the importer dictionary attempting to run any
other script will result in failure.
If the script fails to run please check you have all the pre-requisites and python is configured correctly.
### Menu
The menu is the main interface and the first thing you see when running the importer, your current branch version will be at the top followed by multiple options such as adding or deleting an item or block.

You can select any option via entering the character enclosed in square brackets e.g. [a]dd item, entering a would transfer you to the adding item interface.

<b>inputs are not case sensitive unless stated.</b>

### Adding Items/Blocks
To add an object follow the on screen instructions, you will be asked to select the object type (item or block) followed by the object name. 

### Editing Items/Blocks
To edit an object select the edit menu from the main menu then follow on the screen instructions.
## Github commit message
On succession the program will generate a GitHub commit message for the user (like a receipt) as the changes will be required to be committed to the branch effect the remote source code.

This could be integrated into the importer in the future.
## Version Compatibility
Currently the importer can detect and fetch the mod Minecraft version in the mcmod.info file. The difference in the forge mod loaders (fml) api is currently unknown however the file writing will be based on a template system.

With a different template for each Minecraft version reducing the risk of any invalid code being written to the source code.
## Currently Supported Versions
1.12.2
