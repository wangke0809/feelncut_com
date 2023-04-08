import os

def alter(file,old_str,new_str):
    """
    替换文件中的字符串
    :param file:文件名
    :param old_str:就字符串
    :param new_str:新字符串
    :return:
    """
    file_data = ""
    with open(file, "r", encoding="utf-8") as f:
        for line in f:
            if old_str in line:
                line = line.replace(old_str,new_str)
            file_data += line
    with open(file,"w",encoding="utf-8") as f:
        f.write(file_data)
        print(file)

for fpathe,dirs,fs in os.walk('./'):
  for f in fs:
    if os.path.join(fpathe,f)[-4:] == 'html':
        a = '''<!-- Added by HTTrack --><meta http-equiv="content-type" content="text/html;charset=utf-8" /><!-- /Added by HTTrack -->'''
        b = '''<a class="hdimg img" href="../../../../index.html">'''
        c = '''<a class="hdimg img" href="../../../../old_index.html">'''
        # alter(os.path.join(fpathe,f),a,'')
        # alter(os.path.join(fpathe,f),'index-2.html','index.html')
        alter(os.path.join(fpathe,f),b,c)

