import random
 
canlilar = [
    "kedi", "köpek", "kuş", "fil", "zebra", "timsah", "kanguru", "ayı", "ördek", "kaplumbağa",
    "sincap", "kurbağa", "kurt", "deve", "suaygırı", "kartal", "papağan", "denizanası", "yılan", "tavuk",
    "aslan", "penguen", "kamplumbaga", "dinozor", "karınca", "örümcek", "kertenkele", "denizyıldızı", "geyik", "kirpi",
    "salyangoz", "sivrisinek", "kelebek", "gelincik", "köstebek", "yusufçuk", "su böceği", "ahtapot", "tırtıl", "karakuş",
    "sarıkanarya", "pelikan", "delfin", "ördekkuşu", "denizkaplumbağası", "sümsük", "kum böceği", "vahşikedi", "güvercin", "toygar",
    "marmoset", "tundra", "kurt", "karleopardı", "kayınortmantavşanı", "himalayatilki", "koala", "gazelle", "gazal", "geceyarısılanı",
    "tıknazkaplumbağa", "tropikalkuş", "fok", "balina", "grikanarya", "karga", "yavruköpek", "baboon", "anaconda", "kudu",
    "salamander", "avurtlu", "aygır", "pudu", "humboldt", "viper", "warthog", "quokka", "caiman", "ptarmigan",
    "loris", "piranha", "gibbon", "leopard", "anemone", "dugong", "puffin", "ant", "antelope", "pigeon"
    # Daha fazla hayvan ekleyebilirsiniz
]
answer = random.choice(canlilar)
alphabet = "abcçdefgğhıijklmnoöpqrsştuüvwxyz"
due = 5
yapilanTahmin = ""
 

adam = [
    """
      --------
      |    |
      |
      |
      |
      |
    """,
    """
      --------
      |    |
      |    O
      |
      |
      |
    """,
    """
      --------
      |    |
      |    O
      |    |
      |
      |
    """,
    """
      --------
      |    |
      |    O
      |   /|
      |
      |
    """,
    """
      --------
      |    |
      |    O
      |   /|\
      |
      |
    """,
    """
      --------
      |    |
      |    O
      |   /|\
      |   /
      |
    """,
    """
      --------
      |    |
      |    O
      |   /|\
      |   / \
      |
    """
]
 
print("Adam Asmaca Oyununa Hoş Geldiniz!")
 
while due > 0:
    kelime = ""
    for harf in answer:
        if harf in yapilanTahmin:
            kelime += harf
        else:
            kelime += "_ "
    
    if kelime == answer:
        print(kelime)
        print("Tebrikler kazandınız!")
        break
    
    print(adam[5 - due])
    print("Hayvan adını tahmin edin:", kelime)
    print(f"Kalan hakkınız: {due}")
    
    tahmin = input("Bir harf tahmin edin: ").lower()
 
    if tahmin in alphabet:
        yapilanTahmin += tahmin
        if tahmin not in answer:
            due -= 1
    else:
        print("Lütfen geçerli bir harf giriniz...")
 
else:
    print("Maalesef kaybettiniz. Doğru kelime:", answer)