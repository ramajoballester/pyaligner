Installation
============

Automatic installation
++++++++++++++++++++++

To install the package, you can use the following command:

.. tabs::

   .. group-tab:: Linux
      Open a terminal and run the following command:

      .. code-block:: bash

         sudo apt update && sudo apt install -y wget ffmpeg
         wget "https://github.com/ramajoballester/pyaligner/releases/latest/download/PyAligner-$(uname)-$(uname -m).sh"
         bash PyAligner-$(uname)-$(uname -m).sh


   .. group-tab:: MacOS
      Open a terminal and run the following command:

      .. code-block:: bash

         brew update && brew install -y wget ffmpeg
         wget "https://github.com/ramajoballester/pyaligner/releases/latest/download/PyAligner-$(uname)-$(uname -m).sh"
         bash PyAligner-$(uname)-$(uname -m).sh

   .. group-tab:: Windows
         
         Not available yet.
         
You can now close the terminal and open a new one to install PyAligner.

PyAligner
---------

Finally, install the PyAligner package:

.. code-block:: bash

   mamba activate pyaligner_env
   pip install pyaligner


PyAligner is now installed and ready to use. Check the :ref:`user guide` 
chapter for more information.


Manual installation
+++++++++++++++++++

Run each command at a time.

Miniforge
---------

.. tabs::

   .. group-tab:: Linux
      Open a terminal and run the following command:

      .. code-block:: bash

         sudo apt update
         sudo apt install -y wget

      Then, install `Miniforge <https://github.com/conda-forge/miniforge?tab=readme-ov-file#install>`_:

      .. code-block:: bash

         wget "https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-$(uname)-$(uname -m).sh"
         bash Miniforge3-$(uname)-$(uname -m).sh
         mamba init

   .. group-tab:: MacOS
      Open a terminal and run the following command:

      .. code-block:: bash

         brew update
         brew install wget

      Then, install `Miniforge <https://github.com/conda-forge/miniforge?tab=readme-ov-file#install>`_:

      .. code-block:: bash

         wget "https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-$(uname)-$(uname -m).sh"
         bash Miniforge3-$(uname)-$(uname -m).sh
         mamba init 

   .. group-tab:: Windows

      Not available yet.


Dependencies
------------

Once Miniforge is installed, you can create a virtual environtment with 
all the dependencies:

.. code-block:: bash

   mamba create -n pyaligner_env -c conda-forge python montreal-forced-aligner pyqt git

Do not forget to activate the environment:

.. code-block:: bash

   mamba activate pyaligner_env


PyAligner
---------

Finally, install the PyAligner package:

.. code-block:: bash

   pip install pyaligner


PyAligner is now installed and ready to use. Check the :ref:`user guide` 
chapter for more information.