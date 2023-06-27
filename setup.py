import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sigmaepsilon",                     
    version="0.0.1",                        
    author="SigmaEpsilon",
    author_email = 'bencebalogh@sigmaepsilon.com',
    url = 'https://github.com/sigma-epsilon/sigmaepsilon',                     
    description="A Python ecosystem of libraries for computational engineering",
    long_description=long_description,   
    long_description_content_type="text/markdown",
    packages=["sigmaepsilon"],   
    classifiers=[
        'Development Status :: 5 - Production/Stable',     
        'License :: OSI Approved :: MIT License',   
        'Programming Language :: Python :: 3 :: Only',
		'Operating System :: OS Independent',
        "Topic :: Scientific/Engineering"
    ],                                      
    python_requires='>=3.7',                            
    package_dir={'':'src'},     
)
