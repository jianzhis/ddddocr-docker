import ddddocr

ocr = ddddocr.DdddOcr(beta=True)

with open("captcha.png", 'rb') as f:
    image = f.read()

res = ocr.classification(image)
print(res)