from reservoir import ReservoirSampling

rs = ReservoirSampling(5)

ts = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"

result = ''

# for i in range(1000):
for i in ts:
    rs.sample(i)

for i in rs:
    result += i
# print(type(ts))
print(result)
