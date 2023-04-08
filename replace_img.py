import os
import re
import urllib.request

abc_dir = '.'
pics_base_dir = './images'

if not os.path.exists(pics_base_dir):
    os.makedirs(pics_base_dir)

image_pattern = re.compile(r'(https?://image\.feelncut\.com/[^\'"<>\s]+?\.(jpe?g|gif|png|svg))')

for root, dirs, files in os.walk(abc_dir):
    for filename in files:
        if filename.endswith('.html'):
            filepath = os.path.join(root, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            for match in image_pattern.finditer(content):
                url = match.group(1)
                pic_filename = os.path.basename(url)
                pic_filename = pic_filename.strip()
                pic_file_date = url.replace('https://image.feelncut.com/', '').replace('/' + pic_filename, '')
                pic_file_date = pic_file_date.split('/')
                year = pic_file_date[0]
                month = pic_file_date[1]
                pic_dir = os.path.join(pics_base_dir, year, month)
                pic_filepath = os.path.join(pic_dir, pic_filename)
                # print(pic_dir)

                if not os.path.exists(pic_dir):
                    os.makedirs(pic_dir)

                print(f'Downloading {url} to {pic_filepath}...')
                urllib.request.urlretrieve(url, pic_filepath)

                content = content.replace(url, f'/images/{year}/{month}/{pic_filename}')

            with open(filepath, 'w', encoding='utf-8') as f:
                pass
                f.write(content)

print('Done.')


# for root, dirs, files in os.walk(abc_dir):
#     for filename in files:
#         if filename.endswith('.html'):
#             filepath = os.path.join(root, filename)
#             with open(filepath, 'r', encoding='utf-8') as f:
#                 content = f.read()
            
#             for match in image_pattern.finditer(content):
#                 url = match.group(1)
#                 year = match.group(2)
#                 month = match.group(3)
#                 pic_filename = f"{match.group(4)}.{match.group(5)}"
#                 pic_dir = os.path.join(pics_base_dir, year, month)
#                 pic_filepath = os.path.join(pic_dir, pic_filename)

#                 print(f'Downloading {url} to {pic_filepath}...')
#                 if not os.path.exists(pic_dir):
#                     os.makedirs(pic_dir)
#                 urllib.request.urlretrieve(url, pic_filepath)

#                 content = content.replace(url, f'./pics/{year}/{month}/{pic_filename}')

#             with open(filepath, 'w', encoding='utf-8') as f:
#                 f.write(content)