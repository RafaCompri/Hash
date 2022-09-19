import hashlib


frase = 'Em 1999 iniciam-se as atividades da Faculdade de Informática - FCI, como o curso de Ciência da Computação.'

sh256 = "c64dca8c81cc379cc4618056e2801201882cbf53d8786dd4108c7aa9775bfa91 "

md5 = "1013976891617a120472e629ccdf3858"

#sha256
print("sha256:")

string_To_hash = hashlib.sha256(frase.encode('utf-8')).hexdigest()

print(string_To_hash)

print()

#MD5
print("MD5:")

string_To_md5 = hashlib.md5(frase.encode('utf-8')).hexdigest()

print(string_To_md5)

print()

if string_To_hash  == sh256:
  print("HASH sh256 Igual!")
else:
  print("HASH sh256 Divergente")

if string_To_md5  == md5:
  print("HASH MD5 Igual!")
else:
  print("HASH MD5 Divergente")


