weather = input("天候を知りたい場所を入力")
if weather in ["東京","大阪","名古屋"]:
    print(f"{weather}はにわか雨です")
else:
    print(f"{weather}は不明です")