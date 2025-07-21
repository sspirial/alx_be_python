weather = input("What's the weather like today? (sunny/rainy/cold):").lower()
recomendation = ""

if weather == 'sunny':
    recomendation = "Wear a t-shirt and sunglasses."
elif weather == 'rainy':
    recomendation = "Don't forget your umbrella and a raincoat."
elif weather == 'cold':
    recomendation = "Make sure to wear a warm coat and a scarf."
else:
    recomendation = "Sorry, I don't have recommendations for this weather."

print(recomendation)