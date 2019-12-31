import setuptools

with open("README.md", "r") as fh:

    long_description = fh.read()

setuptools.setup(

     name='pymoticon',  

     version='0.1',

     scripts=[] ,

     author="J.R. Robinson",

     author_email="",

     description="Unicode emoticons!",

     long_description=long_description,

   long_description_content_type="text/markdown",

     url="https://github.com/jayaarrgh/pymoticon",

     packages=setuptools.find_packages(),

     classifiers=[

         "Programming Language :: Python :: 3",

         "License :: The Unlicense",

         "Operating System :: OS Independent",

     ],

 )
