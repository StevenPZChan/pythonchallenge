encoded_str = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc \
dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. \
sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

# encoding_dict = {}
# for a in range(ord('a'),ord('y')):
#     encoding_dict[chr(a)]=chr(a+2)
# encoding_dict['y']='a'
# encoding_dict['z']='b'
# encoding_dict[' ']=' '
# encoding_dict['.']='.'
# encoding_dict['(']='('
# encoding_dict[')']=')'
# encoding_dict['\'']='\''
#
# decoded_str = [encoding_dict[c] for c in encoded_str]
# print("".join(decoded_str))
# string.maketrans()

intab = "abcdefghijklmnopqrstuvwxyz"
outtab = "cdefghijklmnopqrstuvwxyzab"
decoded_str = encoded_str.translate(str.maketrans(intab, outtab))
print(decoded_str)
print("map".translate(str.maketrans(intab, outtab)))  # ocr
