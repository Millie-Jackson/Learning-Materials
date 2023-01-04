# Describes the metadata of your project as well as the packages that need to be installed to run your script. 
# As opposed to requirements.txt, setup.py indicates that your project has likely been packaged and distributed with Distutils, which is the standard for distributing Python modules.

# This indicates that our package(s) is likely to be distributed using setuptools or Distutils. 
# In presence of this file, using pip install . will look for the packages in the directory and will add them to your Python Path the same way you install any other library.