# blur
Python scripts that can blur images and faces within images

These scripts requires OpenCV and Numpy in order to run, which can be downloaded with pip:

  python -m pip install numpy opencv-python
  
 
## Blur entire images
There are three different implementation for this that can be used independently of each other.
The different implementations give the same result, but utilize different algorithms that affect
the execution time.  
Implementation 1 uses native Python and is very slow.  
Implementation 2 uses vectorization and runs very fast on mulitthreaded processors.  
Implementation 3 uses the Numba package and runs significantly faster than implementation 1,
  but is slower than implementation 2 on most modern computers.  

The estimated execution time for all the scripts lies from around 20 sec to 3 min for the demo image (640x480).

### Running the scripts  

<b> Running implementation 1: </b> 

    python3 blur_1.py [file_source] [file_destination]

<b>Running implementation 2: </b> 

    python3 blur_2.py [file_source] [file_destination]

<b>Running implementation 3: </b> 

    python3 blur_3.py [file_source] [file_destination]

<b>Running the unit tests for the three different implementations: </b> 

    python3 test_blur.py

<b>Running the command line interface: </b>  

    python3 blur.py -src [file_source] 

    
## Blur faces in images
Uses the vectorization technique from implementation 2. 
Faces will be detected with Intel's haarcascade xml code and blurred gradually
until they are no longer detectable.

<b> Running the face blurring script: </b>

    python3 blur_faces.py [file_source] [file destination]
    
## Demo
An image, "beatles.jpg", is included for demonstration purposes. The image can be be put as the [file_source] argument.
An example for how to use the scripts can be:

    python3 blur_faces.py beatles.jpg beatles_blurred.jpg
