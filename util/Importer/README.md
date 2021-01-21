# Mod Item and Block importer

This is a simple way to add a custom item or block without requiring the knowledge of how to code, it also makes it simpler to add items and blocks either way.
The importer will be a simple python script that can be found in "utils>importers", simply run the script and follow the on-screen instructions to use the importer (CLI)

Below is a prelim plan for the importer.

## How to use it
Choose to add either an item or block into the source code
(the current branch opened will dictate the version the change is applied to by default).

Then you will be required to enter the name of the game object
(as more functionality is added more information will be required )

you can then confirm the changes you have made (game objects added etc)

A git commit message will be printed you will then be required
to commit the change to the branch using the message

## How it works
the importer will attempt to access the mcmod.info file on the current branch and get the acceptable mcversion from within the file.

the game object will require a title for the lang and an unlocalized name to be used for registry and texture events
the name will be given in lang format with manipulation required for conversion to unlocalized name.
(there will be a naming convention rule)

simple confirmation code holding the result in an array before applying the actions on the source code

generate a GitHub commit message for the user as the changes will be required to be committed (like a receipt)

note: inputting information from CSV, tables or other used formats can be integrated into the importer

## Version Compatability
currently the importer can detect and fetch the mod minecraft version in the mcmod.info file. 
the difference in the forge mod loaders (fml) api is currently unknown however the file writing will be based on a templating system 
with a different template for each mc version reducing the risk of any invalid code being written to the source code

### Currently Supported Versions
1.12.2
