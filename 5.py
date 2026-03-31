from floc_simhash import SimHash

document = "Lorem ipsum dolor sit amet consectetur adipiscing elit"
document1 = "Lorem ipsum dolor sit amet consectetur adipiscing elir"

hashed_document = SimHash(n_bits=128).hash(document)
hashed_document1 = SimHash(n_bits=128).hash(document1)

print(hashed_document)
print(hashed_document1)