#!/usr/bin/env python
# coding: utf-8

# In[1]:


import setuptools

with open('C:/Users/Hindy/Desktop/Container/README.md', 'r') as fh:
    long_descripion = fh.read()
    
setuptools.setup(
    name='Recurrsive_Feature_Selector', 
    version='0.0.3',
    author='Hindy Yuen', 
    author_email='hindy888@hotmail.com', 
    description='Recurrsively selecting the best features', 
    long_description=long_descripion, 
    long_description_content_type='text/markdown', 
    url='https://github.com/HindyDS/RFS', 
    packages=setuptools.find_packages(), 
    classifiers=[
        'Programming Language :: Python :: 3', 
        'License :: OSI Approved :: MIT License', 
        'Operating System :: OS Independent', 
    ], 
    python_requires='>=3.6', 
)

