import qrcode

url = 'https://github.com/NTFSv6?tab=repositories'
conf = f'''GitHub : 
{url}
'''
img = qrcode.make(conf)
img.save("GitHub.png")
