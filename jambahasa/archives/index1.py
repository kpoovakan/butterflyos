'''import argostranslate.package
import argostranslate.translate

from_code = "en"
to_code = "id"

# Download and install Argos Translate package
argostranslate.package.update_package_index()
available_packages = argostranslate.package.get_available_packages()
package_to_install = next(
    filter(
        lambda x: x.from_code == from_code and x.to_code == to_code, available_packages
    )
)
argostranslate.package.install_from_path(package_to_install.download())

# Translate
translatedText = argostranslate.translate.translate("Hello World", from_code, to_code)
print(translatedText)
#THIS ISNT WORKING??'''

'''import sys
import os
sys.path.insert(0, os.path.abspath("packages"))
import argostranslate.package
import argostranslate.translate
argostranslate.package.install_from_path("translate-en_id-1_9.argosmodel")
argostranslate.package.install_from_path("translate-id_en-1_9.argosmodel")
print(argostranslate.translate.translate("I am not suspicious", "en", "id"))'''

# AHA!! https://github.com/frostdev03/Kamus/tree/main/app/src/main/res/raw