import cognitive_face as CF

KEY = '227c5be68d844d488f63c123ca4907ea'  # Replace with a valid subscription key (keeping the quotes in place).
CF.Key.set(KEY)

BASE_URL = 'https://uksouth.api.cognitive.microsoft.com/face/v1.0'  # Replace with your regional Base URL
CF.BaseUrl.set(BASE_URL)

# You can use this example JPG or replace the URL below with your own URL to a JPEG image.
img_url = 'https://s3.amazonaws.com/ecommerce-prod.mheducation.com/unitas/corporate/news/press-kit/executive-leadership/catherine-mathis.jpg'
faces = CF.face.detect(img_url)
print(faces)
