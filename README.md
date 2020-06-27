# shredfile
Basic tool written in Python to shred files

<b>How it works</b>:
<br>
Shredfile works by writing random bytes to the file you want to shred. You specify how many passes you want to shred the file. For example if you specify 10 passes, it will repeat the writing random data process 10 times. After it does that, it deletes the file.
<br>
You don't need to install anything because Shredfile only uses <b>os</b>, a library included in Python by default.
