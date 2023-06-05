kata = {
    'Python': 'Guido van Rossum',
    'Ruby': 'Yukihiro Matsumoto',
    'PHP': 'Rasmus Lerdorf',
}
# kata = {}
# kata = {'Python': 'Guido van Rossum'}

if len(kata) < 1:
    print("Dictionary is empty")

else:
    keys = list(kata.keys())
    values = list(kata.values())
    for key in kata:
        print(f"{key} was created by {kata[key]}")
