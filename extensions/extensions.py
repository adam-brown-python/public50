ex = {"jpg":"image/jpeg","gif":"image/gif","jpeg":"image/jpeg",
      "png":"image/png","zip":"application/zip","pdf":"application/pdf","txt":"text/plain"}

file = input("File Name: ").strip().lower()
if file[-3:] in ex.keys():

    print(ex[file[-3:]])

elif file[-4:] in ex.keys():

    print(ex[file[-4:]])
else:
    print("application/octet-stream")


