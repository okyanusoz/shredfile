# shredfile
Basic tool written in Python to shred files
<b>How it works</b>:
<br>
Shredfile works by writing random bytes to the file you want to shred(it also keeps the same file size). You specify how many passes you want to shred the file. For example if you specify 10 passes, it will repeat the writing random data process 10 times. After it does that, it deletes the file.
<br>
You don't need to install anything because Shredfile only uses <b>os</b>, a library included in Python by default.
<br>
<b>Running Shredfile</b>:
<br>
To run Shredfile, install Python and then download main.py and shredfolder.py(optional, if you want to shred folders aka directories).
<br>
<b>Then type <code>python main.py</code> or <code>python shredfolder.py</code>
<br>
If there are issues, please let me know.
