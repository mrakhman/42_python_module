kata = (19, 42, 21)
# kata = []
# kata = ()
# kata = (1000,)
# kata = (3, 1)

if not isinstance(kata, tuple):
    print("Please use tuple", len(kata))

elif len(kata) < 1:
    print("Tuple is empty")

else:
    nums = ', '.join(str(x) for x in kata)
    print(f"The {len(kata)} numbers are: {nums}")
